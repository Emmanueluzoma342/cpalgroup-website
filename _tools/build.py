#!/usr/bin/env python3
"""
Builds the CPAL pages from shared chrome plus per-page body content.
Run:  python3 _tools/build.py
"""
import os, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
WA = 'https://wa.me/2348067898622?text='
PHONE = '+2348067898622'

WA_ICON = ('<svg width="19" height="19" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
           '<path d="M12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.4 1.3 4.9L2 22l5.2-1.3c1.4.8 3 1.2 4.8 1.2 5.5 0 '
           '10-4.5 10-10S17.5 2 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3.1.8.8-3-.2-.3c-.9-1.4-1.3-3-1.3-4.6C3.5 '
           '7.3 7.3 3.5 12 3.5s8.5 3.8 8.5 8.5-3.8 8.2-8.5 8.2z"/></svg>')

NAV = [('/estates/doctors-residence/', 'The estate'),
       ('/about/', 'About'),
       ('/academy/', 'Academy'),
       ('/realtors/', 'Realtors'),
       ('/blog/', 'Guides'),
       ('/contact/', 'Contact')]


def head(title, desc, path, og='/assets/img/hero-couple.jpg'):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/assets/img/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="canonical" href="https://cpalgroup.com{path}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="/assets/css/cpal.css">
</head>
<body>
'''


def header(current):
    links = ''
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ''
        links += f'      <a href="{href}"{cur}>{label}</a>\n'
    return f'''<header class="top">
  <div class="shell top__in">
    <a class="brand" href="/"><img src="/assets/img/cpal-logo.png" alt="CPAL" width="120" height="36"></a>
    <button class="burger" id="burger" aria-label="Menu" aria-expanded="false"><span></span></button>
    <nav class="nav" id="nav">
{links}      <a class="nav__cta" href="{WA}I%20want%20to%20book%20an%20inspection%20at%20Doctor%27s%20Residence." target="_blank" rel="noopener">Book an inspection</a>
    </nav>
  </div>
</header>

<main>
'''


FOOTER = f'''</main>

<footer class="foot">
  <div class="shell">
    <div class="foot__grid">
      <div>
        <h4>CPAL</h4>
        <p style="color:#9DB2CA;">Chuks Properties Academy Limited, RC 8324784.<br>
           Emegoz Plaza, beside Ezenei Junction, along Asaba-Benin Expressway, Asaba, Delta State.</p>
      </div>
      <div>
        <h4>Pages</h4>
        <ul>
          <li><a href="/estates/doctors-residence/">The estate</a></li>
          <li><a href="/about/">About CPAL</a></li>
          <li><a href="/academy/">Academy</a></li>
          <li><a href="/realtors/">Become a realtor</a></li>
          <li><a href="/blog/">Guides</a></li>
        </ul>
      </div>
      <div>
        <h4>Talk to us</h4>
        <ul>
          <li><a href="tel:{PHONE}">0806 789 8622</a></li>
          <li><a href="tel:+2349029312069">0902 931 2069</a></li>
          <li><a href="mailto:info@cpalgroup.com">info@cpalgroup.com</a></li>
          <li><a href="/contact/">Book an inspection</a></li>
        </ul>
      </div>
    </div>
    <div class="foot__base">
      <span>Land is sold as ownership. CPAL does not offer investment returns.</span>
      <span>Designed and built by <a href="https://swellbridgedigital.com" target="_blank" rel="noopener">Swellbridge Digital</a></span>
    </div>
  </div>
</footer>

<div class="sticky">
  <a class="btn btn--gold" href="{WA}I%20want%20to%20book%20an%20inspection%20at%20Doctor%27s%20Residence." target="_blank" rel="noopener">{WA_ICON} WhatsApp</a>
  <a class="btn btn--ghost" href="tel:{PHONE}">Call</a>
</div>

<a class="wa" href="{WA}Hello%20CPAL%2C%20I%20saw%20your%20website." target="_blank" rel="noopener">
  {WA_ICON}<span>Chat with CPAL</span></a>

<script>
(function(){{
  'use strict';
  document.querySelectorAll('.vid__play').forEach(function (el) {{
    el.addEventListener('click', function () {{
      var f = document.createElement('iframe');
      f.src = el.dataset.src;
      f.setAttribute('allow','autoplay; fullscreen; picture-in-picture');
      f.setAttribute('allowfullscreen','');
      f.setAttribute('title', el.getAttribute('aria-label') || 'Video');
      el.replaceWith(f);
    }});
  }});
  var b = document.getElementById('burger'), n = document.getElementById('nav');
  if (b && n) b.addEventListener('click', function(){{
    var open = n.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  }});
}})();
</script>
</body>
</html>
'''


def cta_band(heading, text, wa_msg, label='Book an inspection'):
    return f'''
  <section class="s s--navy">
    <div class="shell">
      <div class="split">
        <div>
          <h2>{heading}</h2>
          <p class="lede" style="margin-top:16px;">{text}</p>
          <div class="btns">
            <a class="btn btn--gold" href="{WA}{wa_msg}" target="_blank" rel="noopener">{WA_ICON} {label}</a>
            <a class="btn btn--ghost" href="tel:{PHONE}">Call 0806 789 8622</a>
          </div>
        </div>
        <div class="split__img split__img--wide">
          <img src="/assets/img/handover.jpg" alt="Documents handed over on the land"
               width="1920" height="1280" loading="lazy">
        </div>
      </div>
    </div>
  </section>
'''


def magnet(kicker='Free buyer pack'):
    return f'''
  <section class="s s--warm">
    <div class="shell">
      <div class="magnet">
        <div class="magnet__body">
          <p class="kicker">{kicker}</p>
          <h2>Get the 17-page buyer pack.</h2>
          <p>Everything a serious buyer needs before parting with money, including the parts most
             companies would rather you skimmed.</p>
          <ul class="magnet__list">
            <li>Every document you receive, and the honest status of each one</li>
            <li>The full price comparison against neighbouring estates</li>
            <li>Payment terms in full, including the late penalty</li>
            <li>What is built on site today and what is still only planned</li>
            <li>A checklist to verify us, or any estate, before you pay</li>
          </ul>
          <div class="btns">
            <a class="btn btn--gold" href="{WA}Please%20send%20me%20the%20Doctor%27s%20Residence%20Buyer%20Pack." target="_blank" rel="noopener">{WA_ICON} Send it to me on WhatsApp</a>
          </div>
          <p style="margin-top:14px; font-size:.96rem; color:#8FA5BE;">Tap and your message is already
             written. We reply with the pack, and you can ask anything from there.</p>
        </div>
        <div class="magnet__img">
          <img src="/assets/img/pack-cover.jpg" alt="Cover of the Doctor&rsquo;s Residence buyer pack"
               width="910" height="1287" loading="lazy">
        </div>
      </div>
    </div>
  </section>
'''


def write(path, title, desc, body, current=None, og='/assets/img/hero-couple.jpg'):
    out = ROOT / path.lstrip('/') / 'index.html' if not path.endswith('.html') else ROOT / path.lstrip('/')
    out.parent.mkdir(parents=True, exist_ok=True)
    canonical = path if path.endswith('/') else path + '/'
    html = head(title, desc, canonical, og) + header(current or canonical) + body + FOOTER
    out.write_text(html)
    print(f'  {out.relative_to(ROOT)}  ({len(html)//1024}KB)')


if __name__ == '__main__':
    print('build helpers ready — import from page scripts')
