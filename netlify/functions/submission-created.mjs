/**
 * Meta Conversions API bridge.
 *
 * Netlify calls this automatically every time one of the site forms is
 * submitted successfully. Nothing on the page has to call it, so it still runs
 * when the visitor's browser blocks the pixel — which is the whole point.
 *
 * The browser already sent a Lead event carrying an event_id. This sends the
 * same event_name with the same event_id, so Meta keeps one and drops the other
 * instead of counting the lead twice.
 *
 * Environment variables (Netlify: Site settings > Environment variables):
 *   META_PIXEL_ID        required  e.g. 26786909137584547
 *   META_CAPI_TOKEN      required  Events Manager > Settings > Generate access token
 *   META_API_VERSION     optional  defaults to v21.0
 *   META_TEST_EVENT_CODE optional  set while testing, then REMOVE it
 */

import crypto from 'node:crypto';

const FORMS = {
  'lp-lead': 'Lead',
  subscription: 'Lead',
};

/** Meta requires SHA-256 of the normalised, lowercased value. */
function hash(value) {
  if (!value) return undefined;
  const v = String(value).trim().toLowerCase();
  if (!v) return undefined;
  return crypto.createHash('sha256').update(v).digest('hex');
}

/**
 * Meta wants E.164 digits with no plus sign. Nigerian numbers are usually typed
 * as 08067898622, which has to become 2348067898622 or the match fails.
 */
function normalisePhone(raw) {
  if (!raw) return undefined;
  let d = String(raw).replace(/\D/g, '');
  if (!d) return undefined;
  if (d.startsWith('00')) d = d.slice(2);
  if (d.startsWith('0') && d.length === 11) d = '234' + d.slice(1);
  else if (d.length === 10 && !d.startsWith('234')) d = '234' + d;
  return d.length >= 8 && d.length <= 15 ? d : undefined;
}

function splitName(full) {
  if (!full) return {};
  const parts = String(full).trim().split(/\s+/);
  if (parts.length === 1) return { fn: parts[0] };
  return { fn: parts[0], ln: parts[parts.length - 1] };
}

function pick(data, keys) {
  for (const k of keys) {
    if (data[k] !== undefined && data[k] !== null && String(data[k]).trim() !== '') {
      return String(data[k]).trim();
    }
  }
  return '';
}

export default async (req) => {
  const PIXEL = process.env.META_PIXEL_ID;
  const TOKEN = process.env.META_CAPI_TOKEN;
  const VERSION = process.env.META_API_VERSION || 'v21.0';
  const TEST_CODE = process.env.META_TEST_EVENT_CODE;

  if (!PIXEL || !TOKEN) {
    console.log('CAPI skipped: META_PIXEL_ID or META_CAPI_TOKEN not set');
    return new Response('not configured', { status: 200 });
  }

  let payload;
  try {
    const body = await req.json();
    payload = body.payload || body;
  } catch (err) {
    console.log('CAPI skipped: unreadable submission body');
    return new Response('bad body', { status: 200 });
  }

  const formName = payload.form_name || '';
  const eventName = FORMS[formName];
  if (!eventName) {
    console.log(`CAPI skipped: form "${formName}" is not mapped`);
    return new Response('ignored', { status: 200 });
  }

  const data = payload.data || {};

  const fullName = pick(data, ['full_name', 'name']);
  const phone = normalisePhone(pick(data, ['phone', 'phone_1', 'phone_2']));
  const email = pick(data, ['email']);
  const eventId = pick(data, ['event_id']);
  const pageUrl = pick(data, ['page_url']) || 'https://cpalgroup.com/lp/';
  const fbp = pick(data, ['fbp']);
  const fbc = pick(data, ['fbc']);
  const ip = payload.ip || pick(data, ['ip']);
  const ua = payload.user_agent || pick(data, ['user_agent']);
  const { fn, ln } = splitName(fullName);

  const user_data = {
    em: hash(email),
    ph: hash(phone),
    fn: hash(fn),
    ln: hash(ln),
    country: hash('ng'),
    client_ip_address: ip || undefined,
    client_user_agent: ua || undefined,
    fbp: fbp || undefined,
    fbc: fbc || undefined,
  };
  Object.keys(user_data).forEach((k) => user_data[k] === undefined && delete user_data[k]);

  // Meta needs at least one identifier or the event is unusable.
  const identifiers = ['em', 'ph', 'fbp', 'fbc', 'client_ip_address'];
  if (!identifiers.some((k) => user_data[k])) {
    console.log('CAPI skipped: no usable identifier on this submission');
    return new Response('no identifier', { status: 200 });
  }

  const event = {
    event_name: eventName,
    event_time: Math.floor(Date.now() / 1000),
    action_source: 'website',
    event_source_url: pageUrl,
    user_data,
    custom_data: {
      content_name: "Doctor's Residence buyer pack",
      content_category: 'Land',
      form: formName,
      timeline: pick(data, ['timeline']) || undefined,
      source: pick(data, ['source']) || undefined,
    },
  };
  if (eventId) event.event_id = eventId;
  Object.keys(event.custom_data).forEach(
    (k) => event.custom_data[k] === undefined && delete event.custom_data[k]
  );

  const body = { data: [event] };
  if (TEST_CODE) body.test_event_code = TEST_CODE;

  const url = `https://graph.facebook.com/${VERSION}/${PIXEL}/events?access_token=${encodeURIComponent(TOKEN)}`;

  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    });
    const text = await res.text();
    if (!res.ok) {
      // Logged, not thrown: a CAPI failure must never affect the visitor.
      console.log(`CAPI error ${res.status}: ${text}`);
      return new Response('capi error', { status: 200 });
    }
    console.log(`CAPI sent ${eventName} for "${formName}" (event_id: ${eventId || 'none'}) -> ${text}`);
    return new Response('ok', { status: 200 });
  } catch (err) {
    console.log(`CAPI request failed: ${err && err.message}`);
    return new Response('capi failed', { status: 200 });
  }
};
