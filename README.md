# cpalgroup.com

Website for **Chuks Properties Academy Limited (CPAL)**, Asaba, Delta State. RC 8324784.

Static HTML. No build step, no framework, no dependencies. Netlify publishes the repository root as-is.

## Pages

| Path | Purpose |
|---|---|
| `/` | Home |
| `/estates/doctors-residence/` | Doctor's Residence Estate sales page |
| `/about/` | About CPAL and leadership |
| `/realtors/` | Realtor recruitment |
| `/realtor-hub/` | Realtor sales kit, prospect PDF, rules |
| `/academy/` | CPAL Academy |
| `/contact/` | Contact and inspection booking |

## Fonts

Self-hosted in `/assets/fonts/` as subset WOFF2, roughly 172KB for the whole set. They are **not** loaded
from Google Fonts, deliberately: an external stylesheet is a render blocker, and on a slow or filtered
connection the browser waits for it before painting anything, so the page appears to hang. Do not
reintroduce a `fonts.googleapis.com` link.

## Structure

```
/assets/css/cpal.css     design system, single stylesheet
/assets/img/             photography and logo
/assets/docs/            prospect pack PDF
netlify.toml             headers, caching, redirects
sitemap.xml  robots.txt
```

## Editing content

Everything is plain HTML. The pieces most likely to change:

**Plot availability.** Homepage `index.html`, near the bottom, in the script block:
```js
var TOTAL = 64, SOLD = 20;
```
Also update the visible figures: `board__count` on the homepage, the `Availability` ledger row, and the facts list on the estate page.

**Price.** Search for `4.5M` and `4,500,000`.

**Documentation status.** Each ledger row carries a tag: `tag--ok` (confirmed, green), `tag--wait` (outstanding, rust), `tag--build` (in progress, violet). When the C of O is issued, change that row's tag from `tag--wait` to `tag--ok` and update the wording on every page it appears.

## Content rules

These are not stylistic preferences. They exist to keep CPAL out of misrepresentation claims.

- The Certificate of Occupancy is **in view**, not issued. Never write it as issued anywhere.
- Gate house, security, pipe-borne water and sports facility are **planned**. Never present tense.
- Land is sold as **ownership**. No projected returns, ROI figures or appreciation promises.
- Commission is paid on **property sales only**. No downline or recruitment earnings language.
- Plot counts must match the ground. Do not round.

## Settled: the LGA

Atuma-Iga is in **Oshimili North LGA**, not Aniocha North. Three independent sources agree: the Delta State
Government project board photographed on site, and multiple competing estate listings at Atuma-Iga on Nigerian
property portals. Site copy and meta descriptions use Oshimili North throughout. Still worth confirming against
the registered survey plan before it goes on any printed document.

## Price comparison

The comparison ledgers on the home, estate and realtor-hub pages use publicly listed prices from Nigerian
property portals as at August 2026. Competitors are deliberately unnamed. Re-check these figures every few
months and update the "Listed Aug 2026" stamp when you do. If a competitor drops below CPAL on cost per square
metre, remove the ledger rather than leave a stale claim standing.

## Payment terms (confirmed by Dr Agba, Aug 2026)

- Outright: N4,500,000.
- Instalment: minimum N500,000 deposit. No fixed monthly schedule.
- Balance must clear within six months.
- Past six months: 5% of the property price per month of default (N225,000/month).
- Withdrawal: full payment refunded less 20%. Allow three weeks.

These appear on the estate page, in the realtor hub facts ledger, and on page 06 of the prospect pack.
The penalty is disclosed prominently on purpose. Do not move it into small print.

## Contact numbers

Primary phone and WhatsApp: **0806 789 8622**. Second line: 0902 931 2069.
All `wa.me` links and the floating dock use 0806.

## Videos

Hosted on videas.fr, linked from the estate page and realtor hub. If a link dies, the pages break silently
— check them when updating.

## Outstanding

- Confirm the studio portraits and the Delta TV still are all Dr Chukwuma Agba.
- Doctorate field, book purchase link, and where the decade of real estate experience was spent.
- Realtor minimum requirement.
- Aerial footage and the estate survey layout.
- Do not publish IMG_7863: an armed escort is visible. Meta will reject any ad containing it.

## Deploy

Push to `main`. The host rebuilds on push. No build step, no dependencies.

The contact form collects name, email, phone, location, enquiry type and message. Email and phone are
required and validated (phone counts digits only, 7 to 15, so +234 and diaspora formats all pass). The
phone number is asked for separately because many people use a different line for WhatsApp than for calls. The form does not
post anywhere. It composes the visitor's answers into a WhatsApp message and
opens a chat with 0806 789 8622. Nothing to configure, nothing to monitor, and the enquiry lands where
CPAL already works. To change the destination number, edit the `wa.me` number in the script at the
bottom of `/contact/index.html`.
