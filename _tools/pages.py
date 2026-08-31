#!/usr/bin/env python3
"""Generates the standard pages. Run: python3 _tools/pages.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import write, cta_band, magnet, WA, WA_ICON, PHONE

print('Building pages...')

# ============================================================ ABOUT
write('/about/',
  "About CPAL | Chuks Properties Academy Limited, Asaba",
  "Chuks Properties Academy Limited, RC 8324784, founded by Dr Chukwuma Agba. Selling land at Atuma-Iga, Delta State, on one principle: every claim checkable before anybody pays.",
  f'''
  <section class="hero">
    <div class="hero__text">
      <div class="hero__place">Chuks Properties Academy Limited</div>
      <h1 class="promise">We sell land the way we would want it sold to us.</h1>
      <p>Registered in Nigeria as RC 8324784, with an office you can walk into in Asaba and a
         founder whose name is on the door.</p>
      <div class="btns">
        <a class="btn btn--gold" href="{WA}I%20would%20like%20to%20know%20more%20about%20CPAL." target="_blank" rel="noopener">{WA_ICON} Talk to us</a>
        <a class="btn btn--ghost" href="/estates/doctors-residence/">See the estate</a>
      </div>
    </div>
    <div class="hero__img" style="background-image:url('/assets/img/launch-day.jpg')"
         role="img" aria-label="Launch day at Doctor's Residence Estate"></div>
  </section>

  <div class="facts">
    <div><b>RC 8324784</b><span>registered in Nigeria</span></div>
    <div><b>Asaba</b><span>office you can visit</span></div>
    <div><b>A decade</b><span>of experience behind it</span></div>
    <div><b>64 plots</b><span>in Phase 1, now selling</span></div>
  </div>

  <section class="s">
    <div class="shell">
      <div class="split split--wide">
        <div>
          <p class="kicker">Leadership</p>
          <h2>Dr Chukwuma Agba</h2>
          <p style="margin-top:6px; color:var(--muted); font-family:'Franklin',sans-serif; font-weight:600;">
             Founder and Chairman, known as the Property Doctor</p>
          <p style="margin-top:20px;">Dr Chukwuma Agba has spent a decade in Nigerian real estate. He
             founded CPAL on a single argument, the one that runs through this whole company: that the
             way to sell Nigerian land is to make every claim checkable before anybody is asked to pay.</p>
          <p>He is the author of <i>Doctor Sales Formula</i>, a book on sales practice, and he read
             physics at the Federal University of Technology, Owerri. He hails from Ideato South Local
             Government Area of Imo State and is a family man with three children.</p>
          <p>He signs off on what appears on this website, including the parts that say a document is
             still outstanding.</p>
        </div>
        <div class="split__img split__img--tall">
          <img src="/assets/img/chairman-crop.jpg" alt="Dr Chukwuma Agba, Founder and Chairman of CPAL"
               loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="s s--navy">
    <div class="shell">
      <p class="kicker">How we work</p>
      <h2>Three rules we do not bend.</h2>
      <div class="rows" style="margin-top:32px;">
        <div class="row">
          <h3>You inspect before you pay</h3>
          <p>Nothing is asked of you until you have stood on the land, seen your beacons and read the
             terms. If you are abroad, we walk the plot on a live video call and you direct the camera.</p>
        </div>
        <div class="row">
          <h3>Every document has an honest status</h3>
          <p>What is issued, we call issued. What is still in progress, we call in progress, in writing,
             before you pay rather than after. Our estate-wide Certificate of Occupancy is still being
             processed and we say so on every page it matters.</p>
        </div>
        <div class="row">
          <h3>Payment goes to the company, never a person</h3>
          <p>Always the corporate account of Chuks Properties Academy Limited, confirmed to you directly
             by our office. Never an individual, never a realtor, however well you know them.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="s">
    <div class="shell">
      <div class="split split--wide">
        <div class="split__img split__img--wide">
          <img src="/assets/img/delta-tv.jpg" alt="Dr Chukwuma Agba on Delta Broadcasting Service" loading="lazy">
        </div>
        <div>
          <p class="kicker">On the record</p>
          <h2>Delta State Television, not a paid advert.</h2>
          <p style="margin-top:16px;">Dr Agba on <i>Morning Ride</i>, Delta Broadcasting Service,
             discussing property in the state.</p>
          <p>Look for the broadcast yourself rather than taking our word for it. That is the whole
             approach: we would rather point you at things you can check than ask you to believe us.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="s s--warm">
    <div class="shell">
      <div class="head">
        <h2>What we do.</h2>
      </div>
      <div class="rows">
        <div class="row">
          <h3>Sell land at Doctor&rsquo;s Residence</h3>
          <p>464 sqm plots at Atuma-Iga, Oshimili North, thirteen minutes from Asaba, with the Deed of
             Assignment and registered survey plan included in the price.</p>
        </div>
        <div class="row">
          <h3>Train realtors through CPAL Academy</h3>
          <p>Free enrolment for our realtors, with a content studio and workspace in Asaba. Commission
             is earned on property sales only.</p>
        </div>
        <div class="row">
          <h3>Supply blocks from our own block industry</h3>
          <p>Which is why buyers taking two plots receive blocks for dwarf fencing as part of the deal.</p>
        </div>
      </div>
    </div>
  </section>
''' + cta_band('Come and meet us.',
    'Our office is at Emegoz Plaza, beside Ezenei Junction along the Asaba-Benin Expressway. '
    'Inspections at the estate run Mondays, Thursdays and Saturdays.',
    'I%20would%20like%20to%20visit%20the%20CPAL%20office.'))

# ============================================================ ACADEMY
write('/academy/',
  "CPAL Academy | Real estate training in Asaba, Delta State",
  "CPAL Academy trains realtors in Asaba. Free enrolment for CPAL realtors, with a content studio, workspace and practical training in selling Nigerian land properly.",
  f'''
  <section class="hero">
    <div class="hero__text">
      <div class="hero__place">CPAL Academy &middot; Asaba</div>
      <h1 class="promise">Learn to sell property properly.</h1>
      <p>Practical training for people who want a real career in Nigerian real estate, not a
         recruitment scheme dressed up as one.</p>
      <div class="btns">
        <a class="btn btn--gold" href="{WA}I%20would%20like%20to%20know%20about%20CPAL%20Academy." target="_blank" rel="noopener">{WA_ICON} Ask about the Academy</a>
        <a class="btn btn--ghost" href="/realtors/">Become a realtor</a>
      </div>
    </div>
    <div class="hero__img" style="background-image:url('/assets/img/handover.jpg')"
         role="img" aria-label="A CPAL representative handing documents to buyers"></div>
  </section>

  <section class="s">
    <div class="shell">
      <div class="head">
        <p class="kicker">What you learn</p>
        <h2>The parts of this job nobody teaches you.</h2>
        <p class="lede">Most people entering Nigerian real estate are handed a flyer and a WhatsApp
           group and told to go and sell. The Academy exists because that is not training.</p>
      </div>
      <div class="rows">
        <div class="row">
          <h3>How land documentation actually works</h3>
          <p>Deed of Assignment, survey plans, Certificate of Occupancy, Governor&rsquo;s consent. What
             each one is, what it proves, and what to tell a buyer who asks. You cannot sell land
             honestly if you do not understand the papers.</p>
        </div>
        <div class="row">
          <h3>How to answer the difficult questions</h3>
          <p>Buyers in this market are careful, and they are right to be. You will learn to answer
             questions about title, disputes and refunds directly, because a straight answer closes
             more sales than a smooth one.</p>
        </div>
        <div class="row">
          <h3>How to find and follow up buyers</h3>
          <p>Where serious buyers actually come from, how to speak to them on WhatsApp without
             sounding like a broadcast, and how to follow up without becoming a nuisance.</p>
        </div>
        <div class="row">
          <h3>How to conduct an inspection</h3>
          <p>Preparing the client, walking the land, showing beacons, handling a live video inspection
             for a buyer abroad, and what never to promise on site.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="s s--navy">
    <div class="shell">
      <p class="kicker">What comes with it</p>
      <h2>Enrolment is free for CPAL realtors.</h2>
      <div class="stack" style="margin-top:30px;">
        <div class="stack__item">
          <span class="stack__tick"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4"><path d="M20 6L9 17l-5-5"/></svg></span>
          <div><b>Free Academy enrolment</b><p>Included when you join CPAL as a realtor.</p></div>
        </div>
        <div class="stack__item">
          <span class="stack__tick"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4"><path d="M20 6L9 17l-5-5"/></svg></span>
          <div><b>Content studio and workspace</b><p>Space in Asaba to record your videos and work,
            with 24/7 wifi.</p></div>
        </div>
        <div class="stack__item">
          <span class="stack__tick"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4"><path d="M20 6L9 17l-5-5"/></svg></span>
          <div><b>Monthly transport allowance</b><p>For realtors actively running inspections.</p></div>
        </div>
        <div class="stack__item">
          <span class="stack__tick"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4"><path d="M20 6L9 17l-5-5"/></svg></span>
          <div><b>10 to 15 percent commission</b><p>Earned on property sales only. There is no
            recruitment income and no downline at CPAL.</p></div>
        </div>
      </div>
    </div>
  </section>
''' + cta_band('Join the next intake.',
    'Tell us a little about yourself and we will explain how the Academy works, what is expected, '
    'and when the next intake begins.',
    'I%20would%20like%20to%20join%20CPAL%20Academy.', 'Ask about the Academy'))

# ============================================================ REALTORS
write('/realtors/',
  "Become a CPAL realtor | 10-15% commission, Asaba, Delta State",
  "Sell for CPAL in Asaba. 10 to 15 percent commission on property sales, free Academy enrolment, content studio and monthly transport allowance. No downline, no recruitment income.",
  f'''
  <section class="hero">
    <div class="hero__text">
      <div class="hero__place">Become a CPAL realtor</div>
      <h1 class="promise">Earn on what you sell, not who you recruit.</h1>
      <p>10 to 15 percent commission on property sales, free Academy training, a content studio in
         Asaba and a monthly transport allowance.</p>
      <div class="btns">
        <a class="btn btn--gold" href="{WA}I%20want%20to%20become%20a%20CPAL%20realtor." target="_blank" rel="noopener">{WA_ICON} Apply on WhatsApp</a>
        <a class="btn btn--ghost" href="tel:{PHONE}">Call 0806 789 8622</a>
      </div>
    </div>
    <div class="hero__img" style="background-image:url('/assets/img/inspection-walk.jpg')"
         role="img" aria-label="Realtors and clients on an inspection walk"></div>
  </section>

  <div class="facts">
    <div><b>10&ndash;15%</b><span>commission on sales</span></div>
    <div><b>Free</b><span>Academy enrolment</span></div>
    <div><b>Monthly</b><span>transport allowance</span></div>
    <div><b>24/7</b><span>wifi and content studio</span></div>
  </div>

  <section class="s">
    <div class="shell">
      <div class="split split--wide">
        <div>
          <p class="kicker">Read this part carefully</p>
          <h2>You earn commission on property sales. Nothing else.</h2>
          <p style="margin-top:18px;">There is no downline at CPAL. No income for signing people up, no
             levels, no matrix, no bonus for building a team beneath you. If somebody has offered you
             that elsewhere, you already know why we do not.</p>
          <p>What you earn here comes from one thing: a buyer inspects a plot, decides to buy it, and
             pays the company. Then you are paid on that sale.</p>
          <p>It is a slower promise than the alternatives. It is also the only one that still works in
             three years.</p>
        </div>
        <div class="split__img split__img--wide">
          <img src="/assets/img/launch-day.jpg" alt="Realtors and buyers at the estate launch" loading="lazy">
        </div>
      </div>
    </div>
  </section>

  <section class="s s--navy">
    <div class="shell">
      <p class="kicker">What you get</p>
      <h2>Everything you need to actually sell.</h2>
      <div class="stack" style="margin-top:30px;">
        <div class="stack__item">
          <span class="stack__tick"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4"><path d="M20 6L9 17l-5-5"/></svg></span>
          <div><b>10 to 15 percent commission</b><p>On the value of each property sale you close.</p></div>
          <span class="stack__val">Per sale</span>
        </div>
        <div class="stack__item">
          <span class="stack__tick"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4"><path d="M20 6L9 17l-5-5"/></svg></span>
          <div><b>Free CPAL Academy enrolment</b><p>Documentation, objection handling, inspections and
            follow-up, taught properly.</p></div>
          <span class="stack__val">Included</span>
        </div>
        <div class="stack__item">
          <span class="stack__tick"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4"><path d="M20 6L9 17l-5-5"/></svg></span>
          <div><b>Content studio and 24/7 wifi</b><p>Record your videos and work from our space in Asaba.</p></div>
          <span class="stack__val">Included</span>
        </div>
        <div class="stack__item">
          <span class="stack__tick"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4"><path d="M20 6L9 17l-5-5"/></svg></span>
          <div><b>Monthly transport allowance</b><p>For realtors actively running inspections.</p></div>
          <span class="stack__val">Monthly</span>
        </div>
        <div class="stack__item">
          <span class="stack__tick"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.4"><path d="M20 6L9 17l-5-5"/></svg></span>
          <div><b>A product you can defend</b><p>Real documents, a government road contract and a price
            you can justify. You will not have to talk around anything.</p></div>
          <span class="stack__val">The best part</span>
        </div>
      </div>
    </div>
  </section>

  <section class="s">
    <div class="shell">
      <div class="head">
        <p class="kicker">How to join</p>
        <h2>Four steps.</h2>
      </div>
      <div class="steps">
        <div class="step"><div><h3>Send us a message</h3><p>Tell us who you are and whether you have
          sold property before. WhatsApp is fastest.</p></div></div>
        <div class="step"><div><h3>Have a conversation</h3><p>We explain how commission works, what is
          expected of you, and what CPAL will and will not do.</p></div></div>
        <div class="step"><div><h3>Complete Academy onboarding</h3><p>So you can answer a buyer&rsquo;s
          hard questions correctly before you are in front of one.</p></div></div>
        <div class="step"><div><h3>Start showing the estate</h3><p>Inspections run Mondays, Thursdays
          and Saturdays. Bring your buyer, or send them and we will host.</p></div></div>
      </div>
      <div class="note" style="margin-top:30px;">
        <p><b>One rule, and it protects you.</b> Never send CPAL account details to a buyer yourself.
           All account details are confirmed to the buyer directly by our office. This keeps you clear
           of any dispute if somebody else in a group chat sends a fake number.</p>
      </div>
    </div>
  </section>
''' + cta_band('Apply to sell for CPAL.',
    'Send us a message and tell us a little about yourself. We reply on WhatsApp.',
    'I%20want%20to%20become%20a%20CPAL%20realtor.%20Here%20is%20a%20little%20about%20me%3A',
    'Apply on WhatsApp'))

# ============================================================ REALTOR HUB
write('/realtor-hub/',
  "Realtor hub | Sales materials for CPAL realtors",
  "Everything a CPAL realtor needs to sell Doctor's Residence: the buyer pack, the estate films, the key facts, and the rules that keep you and your buyer safe.",
  f'''
  <section class="s s--navy" style="padding-top:clamp(44px,6vw,72px);">
    <div class="shell">
      <p class="kicker">Realtor hub</p>
      <h1>Everything you need to sell Doctor&rsquo;s Residence.</h1>
      <p class="lede" style="margin-top:18px;">Send the buyer pack, share the films, quote the facts
         below. If a buyer asks something not answered here, call the office rather than guessing.</p>
      <div class="btns">
        <a class="btn btn--gold" href="/assets/docs/doctors-residence-prospect-pack.pdf" download>Download the buyer pack</a>
        <a class="btn btn--ghost" href="https://chat.whatsapp.com/KX9OtX7Wn69DIXbp55ZgEr?s=cl&amp;p=i&amp;mlu=4" target="_blank" rel="noopener">Join the realtor group</a>
      </div>
    </div>
  </section>

  <section class="s">
    <div class="shell">
      <div class="head">
        <h2>The facts, exactly as they should be quoted.</h2>
        <p class="lede">Do not round these. Accuracy is the whole argument of this estate.</p>
      </div>
      <div class="docs">
        <div class="doc"><b>Estate</b><span>Doctor&rsquo;s Residence, Atuma-Iga, Oshimili North LGA, Delta State</span></div>
        <div class="doc"><b>Plot size</b><span>464 sqm</span></div>
        <div class="doc"><b>Price</b><span>&#8358;4,500,000, documentation inclusive</span></div>
        <div class="doc"><b>Minimum deposit</b><span>&#8358;500,000</span></div>
        <div class="doc"><b>Completion window</b><span>Six months, no fixed monthly schedule</span></div>
        <div class="doc"><b>Late penalty</b><span>5 percent of property price per month of default</span></div>
        <div class="doc"><b>Refund</b><span>Payment less 20 percent admin fee, allow three weeks</span></div>
        <div class="doc"><b>Availability</b><span>44 of 64 plots remaining in Phase 1</span></div>
        <div class="doc"><b>Distance</b><span>13 minutes from Summit Junction, Asaba</span></div>
        <div class="doc"><b>Documents</b><span>Deed of Assignment and registered survey plan on allocation</span><i class="is-ok">Confirmed</i></div>
        <div class="doc"><b>Certificate of Occupancy</b><span>Estate-wide, being processed</span><i class="is-pending">In progress</i></div>
        <div class="doc"><b>On site now</b><span>33KVA transformer, NDDC street lighting, state road under construction</span></div>
        <div class="doc"><b>Two-plot offer</b><span>Free blocks for dwarf fencing, quantity confirmed by the office</span></div>
      </div>
    </div>
  </section>

  <section class="s s--ink">
    <div class="shell">
      <p class="kicker">Share these</p>
      <h2>Four films from the estate.</h2>
      <div class="vids" style="margin-top:28px;">
        <div class="vid">
          <button class="vid__frame vid__play" data-src="https://app.videas.fr/1aaee8a6-f727-4395-bd71-e0a57d6a4fc5/"
                  style="background-image:url('/assets/img/launch-day.jpg')" aria-label="Play: Launching of Doctor's Residence">
            <span class="vid__btn"><svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span>
          </button>
          <div class="vid__cap"><b>Launching of Doctor&rsquo;s Residence</b>
            <span>app.videas.fr/1aaee8a6-f727-4395-bd71-e0a57d6a4fc5</span></div>
        </div>
        <div class="vid">
          <button class="vid__frame vid__play" data-src="https://app.videas.fr/65373e87-aab4-4bef-9329-3a68e940950e/"
                  style="background-image:url('/assets/img/inspection-walk.jpg')" aria-label="Play: Development at Atuma-Iga">
            <span class="vid__btn"><svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span>
          </button>
          <div class="vid__cap"><b>Development at Atuma-Iga is moving fast</b>
            <span>app.videas.fr/65373e87-aab4-4bef-9329-3a68e940950e</span></div>
        </div>
        <div class="vid">
          <button class="vid__frame vid__play" data-src="https://app.videas.fr/bbbb281e-08b6-482c-8da3-19c9696a1aa2/"
                  style="background-image:url('/assets/img/cover-launch.jpg')" aria-label="Play: Launch day, prayer time">
            <span class="vid__btn"><svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span>
          </button>
          <div class="vid__cap"><b>Launch day, prayer time</b>
            <span>app.videas.fr/bbbb281e-08b6-482c-8da3-19c9696a1aa2</span></div>
        </div>
        <div class="vid">
          <button class="vid__frame vid__play" data-src="https://app.videas.fr/26f5f625-efe7-4de6-a87a-09268c4fe7a2/"
                  style="background-image:url('/assets/img/handover.jpg')" aria-label="Play: We treat all our clients as royalty">
            <span class="vid__btn"><svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span>
          </button>
          <div class="vid__cap"><b>We treat all our clients as royalty</b>
            <span>app.videas.fr/26f5f625-efe7-4de6-a87a-09268c4fe7a2</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="s">
    <div class="shell">
      <div class="head">
        <p class="kicker">Rules that protect you</p>
        <h2>Three things you must never do.</h2>
      </div>
      <div class="rows">
        <div class="row">
          <h3>Never send account details yourself</h3>
          <p>All CPAL account details are confirmed to the buyer directly by the office, on a recorded
             call or in writing. If a buyer is defrauded by a number that came from you, you are in the
             middle of it. Route every payment conversation to the office.</p>
        </div>
        <div class="row">
          <h3>Never promise a return, a percentage or a future value</h3>
          <p>We sell land as ownership. Show buyers the bridge, the government road contract and the
             other developers already here, and let them draw their own conclusion. Promising
             appreciation is what put other companies in the news.</p>
        </div>
        <div class="row">
          <h3>Never describe the C of O as issued</h3>
          <p>The estate-wide Certificate of Occupancy is being processed. Say exactly that. What the
             buyer receives now is a Deed of Assignment and a registered survey plan in their name.</p>
        </div>
      </div>
    </div>
  </section>
''' + cta_band('Something you cannot answer?',
    'Call the office rather than guessing. A wrong answer costs a sale and can cost far more than that.',
    'I%20have%20a%20question%20about%20Doctor%27s%20Residence%20from%20a%20buyer.',
    'Message the office'))

# ============================================================ CONTACT
write('/contact/',
  "Contact CPAL | Book an inspection at Doctor's Residence, Asaba",
  "Book an inspection at Doctor's Residence Estate, Atuma-Iga. Inspections Mondays, Thursdays and Saturdays, with live video inspections for buyers abroad. Call 0806 789 8622.",
  f'''
  <section class="hero">
    <div class="hero__text">
      <div class="hero__place">Contact CPAL</div>
      <h1 class="promise">Ask us the difficult questions first.</h1>
      <p>We would rather answer twenty questions than take a payment from somebody who is not sure.</p>
      <div class="btns">
        <a class="btn btn--gold" href="{WA}I%20want%20to%20book%20an%20inspection%20at%20Doctor%27s%20Residence.%20When%20is%20the%20next%20available%20date%3F" target="_blank" rel="noopener">{WA_ICON} Book on WhatsApp</a>
        <a class="btn btn--ghost" href="tel:{PHONE}">Call 0806 789 8622</a>
      </div>
    </div>
    <div class="hero__img" style="background-image:url('/assets/img/inspection-walk.jpg')"
         role="img" aria-label="Clients on an inspection walk at the estate"></div>
  </section>

  <section class="s">
    <div class="shell">
      <div class="split split--wide">
        <div>
          <h2>Send us a message.</h2>
          <p class="lede" style="margin-top:14px;">This opens WhatsApp with your details already
             written, so you keep a copy of the whole conversation on your own phone.</p>

          <form id="waform" novalidate style="margin-top:28px;">
            <div class="field"><label for="name">Full name</label>
              <input id="name" name="name" type="text" required autocomplete="name">
              <span class="err">Please enter your name</span></div>
            <div class="field"><label for="email">Email address</label>
              <input id="email" name="email" type="email" required autocomplete="email" placeholder="So we can send you documents">
              <span class="err">We need a valid email to send the survey plan and deed</span></div>
            <div class="field"><label for="phone">Phone number for calls</label>
              <input id="phone" name="phone" type="tel" required autocomplete="tel" inputmode="tel" placeholder="If it differs from your WhatsApp number">
              <span class="err">Please enter a number we can reach you on</span></div>
            <div class="field"><label for="based">Where are you based</label>
              <input id="based" name="based" type="text" placeholder="City and country" autocomplete="address-level2"></div>
            <div class="field"><label for="topic">What is this about</label>
              <select id="topic" name="topic">
                <option>Book an inspection</option>
                <option>Question about a plot</option>
                <option>Payment and documentation</option>
                <option>Realtor enquiry</option>
                <option>CPAL Academy</option>
              </select></div>
            <div class="field"><label for="message">Your question</label>
              <textarea id="message" name="message" rows="5" required placeholder="Tell us what you would like to know"></textarea>
              <span class="err">Let us know what you would like to ask</span></div>
            <button class="btn btn--gold" type="submit">{WA_ICON} Send on WhatsApp</button>
            <p style="margin-top:14px; font-size:.96rem; color:var(--muted);">We ask for your email
               because the survey plan, the deed and the written terms are sent as attachments, and for
               a phone number in case the line you call on is not the one you use for WhatsApp.</p>
          </form>
        </div>

        <div>
          <div class="note">
            <h3 style="margin-bottom:12px;">Before you pay anyone</h3>
            <p>If your enquiry is about payment, we confirm account details with you directly by call or
               in writing. Never act on account details sent through a status update, a group chat or a
               forwarded flyer. Call the office on 0806 789 8622 and check.</p>
          </div>

          <h3 style="margin-top:34px;">How to reach us</h3>
          <div class="docs" style="margin-top:16px;">
            <div class="doc"><b>Phone and WhatsApp</b><span><a href="tel:{PHONE}" style="color:var(--navy);">0806 789 8622</a></span></div>
            <div class="doc"><b>Second line</b><span><a href="tel:+2349029312069" style="color:var(--navy);">0902 931 2069</a></span></div>
            <div class="doc"><b>Email</b><span><a href="mailto:cpalrealities@gmail.com" style="color:var(--navy);">cpalrealities@gmail.com</a></span></div>
            <div class="doc"><b>Office</b><span>Emegoz Plaza, beside Ezenei Junction, along Asaba-Benin Expressway, Asaba, Delta State</span></div>
            <div class="doc"><b>Inspections</b><span>Mondays, Thursdays and Saturdays. Virtual by arrangement.</span></div>
            <div class="doc"><b>Registration</b><span>RC 8324784</span></div>
          </div>
        </div>
      </div>
    </div>
  </section>
''' + magnet())

print('Done.')
