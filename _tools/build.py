#!/usr/bin/env python3
"""Build the CPAL site. Shared chrome, per-page bodies."""
import os, pathlib, re

ROOT = pathlib.Path('/home/claude/cpal')
WA = "https://wa.me/2349029312069"
WA_INSPECT = WA + "?text=I%20would%20like%20to%20book%20an%20inspection%20at%20Doctor%27s%20Residence%20Estate."
WA_REALTOR = WA + "?text=I%20want%20to%20join%20the%20CPAL%20realtor%20community."
GROUP = "https://chat.whatsapp.com/KX9OtX7Wn69DIXbp55ZgEr?s=cl&amp;p=i&amp;mlu=4"

NAV = [
    ("/estates/doctors-residence/", "Doctor's Residence"),
    ("/about/", "About CPAL"),
    ("/academy/", "Academy"),
    ("/realtors/", "Become a realtor"),
    ("/contact/", "Contact"),
]

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://cpalgroup.com{path}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="/assets/img/launch-day.jpg">
<link rel="preload" href="/assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/newsreader-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/cpal.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="masthead">
  <div class="shell masthead__in">
    <a class="masthead__logo" href="/" aria-label="CPAL home"><img src="/assets/img/cpal-logo.png" width="910" height="238" alt="Chuks Properties Academy Limited"></a>
    <nav aria-label="Primary">{nav}</nav>
    <a class="btn btn--solid btn--sm masthead__cta" href="{wa_inspect}" target="_blank" rel="noopener">Book an inspection</a>
  </div>
</header>
<main id="main">
"""

FOOT = """</main>
<footer class="foot">
  <div class="shell">
    <div class="foot__grid">
      <div>
        <img src="/assets/img/cpal-logo.png" width="910" height="238" alt="CPAL">
        <p style="font-size:0.94rem; max-width:34ch;">Chuks Properties Academy Limited. Verified property sales, real estate training and consultancy in Delta State, Nigeria.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/estates/doctors-residence/">Doctor's Residence Estate</a></li>
          <li><a href="/about/">About CPAL</a></li>
          <li><a href="/academy/">CPAL Academy</a></li>
          <li><a href="/realtors/">Become a realtor</a></li>
          <li><a href="/realtor-hub/">Realtor hub</a></li>
          <li><a href="/contact/">Contact and inspections</a></li>
        </ul>
      </div>
      <div>
        <h4>Office</h4>
        <ul>
          <li>Emegoz Plaza, beside Ezenei Junction</li>
          <li>Asaba-Benin Expressway, Asaba</li>
          <li>Delta State, Nigeria</li>
          <li><a href="tel:+2349029312069">0902 931 2069</a></li>
          <li><a href="mailto:cpalrealities@gmail.com">cpalrealities@gmail.com</a></li>
        </ul>
      </div>
    </div>
    <div class="foot__base">
      <span>&copy; 2026 Chuks Properties Academy Limited &middot; RC 8324784</span>
      <span>Land is sold as ownership. CPAL does not offer investment returns.</span>
    </div>
  </div>
</footer>
<a class="dock" href="{wa}" target="_blank" rel="noopener" aria-label="Chat with CPAL on WhatsApp">
  <svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.4 1.3 4.9L2 22l5.2-1.3c1.4.8 3 1.2 4.8 1.2 5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18.2c-1.6 0-3.1-.4-4.4-1.2l-.3-.2-3.1.8.8-3-.2-.3c-.9-1.4-1.3-3-1.3-4.6C3.5 7.3 7.3 3.5 12 3.5s8.5 3.8 8.5 8.5-3.8 8.2-8.5 8.2z"/><path d="M17.5 14.4c-.3-.1-1.7-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.7 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.2-.5-2.3-1.4-.9-.8-1.4-1.7-1.6-2-.2-.3 0-.5.1-.6l.5-.5c.1-.2.2-.3.3-.5 0-.2 0-.4 0-.5 0-.1-.7-1.6-.9-2.2-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1 2.9 1.2 3.1c.1.2 2 3.1 4.9 4.3.7.3 1.2.5 1.6.6.7.2 1.3.2 1.8.1.6-.1 1.7-.7 1.9-1.4.2-.7.2-1.2.2-1.4-.1-.1-.3-.2-.6-.3z"/></svg>
  <span>Chat with CPAL</span>
</a>
<script>
(function () {{
  var io = new IntersectionObserver(function (es) {{
    es.forEach(function (e) {{ if (e.isIntersecting) {{ e.target.classList.add('is-in'); io.unobserve(e.target); }} }});
  }}, {{ threshold: 0.1 }});
  document.querySelectorAll('.band > .shell > *').forEach(function (el) {{ el.classList.add('reveal'); io.observe(el); }});
}})();
</script>
</body>
</html>
"""


def nav_html(current):
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ''
        out.append(f'<a href="{href}"{cur}>{label}</a>')
    return "".join(out)


def page(path, title, desc, body):
    html = HEAD.format(title=title, desc=desc, path=path, nav=nav_html(path), wa_inspect=WA_INSPECT)
    html += body
    html += FOOT.format(wa=WA)
    target = ROOT / path.strip('/') / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding='utf-8')
    print('built', path)


# =====================================================================
# ESTATE: Doctor's Residence
# =====================================================================

ESTATE = """
<section class="hero">
  <div class="shell">
    <div class="hero__body">
      <div>
        <p class="marker">Doctor's Residence Estate &middot; Atuma-Iga, Delta State</p>
        <h1 class="d1">Thirteen minutes from Asaba, with the documents on the table <em>before your money moves</em>.</h1>
        <p class="lede">464 square metres. &#8358;4.5 million, documentation inclusive. Outright or spread across three to six months. Inspect it in person, or walk it by video call from wherever you are.</p>
        <div class="row">
          <a class="btn btn--solid" href="WA_INSPECT" target="_blank" rel="noopener">Book an inspection</a>
          <a class="btn btn--ghost" href="WA_LINK" target="_blank" rel="noopener">Ask a question</a>
        </div>
      </div>
      <figure class="plate">
        <img src="/assets/img/inspection-walk.jpg" width="960" height="540" alt="Inspection walk on the access road at Doctor's Residence Estate, Atuma-Iga.">
        <figcaption><b>Phase 1, along the road.</b> 44 of 64 plots remaining. Inspections Mondays, Thursdays and Saturdays.</figcaption>
      </figure>
    </div>

    <div class="ledger">
      <div class="ledger__top"><span>Doctor's Residence &mdash; documentation record</span><span>Updated August 2026</span></div>
      <div class="ledger__r"><span >Company registration</span><span >Chuks Properties Academy Ltd &middot; RC 8324784</span><span class="tag tag--ok">Registered</span></div>
      <div class="ledger__r"><span >Deed of Assignment</span><span >Issued to the buyer on allocation</span><span class="tag tag--ok">Confirmed</span></div>
      <div class="ledger__r"><span >Survey plan</span><span >Registered survey plan, per plot</span><span class="tag tag--ok">Confirmed</span></div>
      <div class="ledger__r"><span >Certificate of Occupancy</span><span >Estate-wide C of O</span><span class="tag tag--wait">In view</span></div>
      <div class="ledger__r"><span >Internal road</span><span >Delta State Ministry of Works, Rural &amp; Riverine Roads</span><span class="tag tag--build">Under construction</span></div>
      <div class="ledger__r"><span >Street lighting</span><span >Commissioned by NDDC</span><span class="tag tag--build">In progress</span></div>
      <div class="ledger__r"><span >Power</span><span >33KVA transformer installed on site</span><span class="tag tag--ok">On site</span></div>
      <div class="ledger__r"><span >Availability</span><span >Phase 1, along the road &middot; 44 of 64 plots remaining</span><span class="tag tag--ok">Selling</span></div>
    </div>
  </div>
</section>

<section class="s">
  <div class="shell">
    <p class="marker">Read this part slowly</p>
    <h2 class="display measure">If you are sending money home for land, you already know somebody it happened to.</h2>
    <div class="measure" style="margin-top:1.5rem;">
      <p>Paid for a plot from abroad. Sent the money to a number somebody vouched for. Got a receipt, then a photograph, then excuses, then silence. Or worse, got the land and found out four years later that the papers never existed.</p>
      <p>That is not a rare story in Nigerian real estate. It is common enough that many people in the diaspora have simply decided to wait until they can come home and stand on the land themselves.</p>
      <p>We think that is a reasonable decision, and we have built our process around it. You do not have to trust us. You have to be able to check us.</p>
    </div>
  </div>
</section>

<section class="s s--warm">
  <div class="shell">
    <p class="marker">Verify before you pay</p>
    <h2 class="display measure">Six things you can check without leaving your house.</h2>
    <div class="cols" style="margin-top:2.75rem;">
      <div class="tilex"><h3 class="d3">The company is registered</h3><p>Chuks Properties Academy Limited, RC 8324784. Look that number up yourself at the Corporate Affairs Commission.</p></div>
      <div class="tilex"><h3 class="d3">The road is a government project</h3><p>The Atuma-Iga internal road is under construction by the Delta State Ministry of Works. The project board stands on site and is photographed below. Contractor: RCT Nigeria Ltd, Benin.</p></div>
      <div class="tilex"><h3 class="d3">The survey plan is registered</h3><p>Every plot carries a registered survey plan. Send it to your own surveyor before you commit.</p></div>
      <div class="tilex"><h3 class="d3">The Deed is real and dated</h3><p>Issued to you on allocation, in your name, not a promise of one later.</p></div>
      <div class="tilex"><h3 class="d3">The C of O is in view, and we say so</h3><p>The estate-wide Certificate of Occupancy is in progress, not issued. Any company that tells you a C of O is finished when it is not has told you everything you need to know about them.</p></div>
      <div class="tilex"><h3 class="d3">You can walk the land by video</h3><p>Live call, our phone, your instructions. Ask for the beacon. Ask to see the transformer. Ask us to walk to the boundary.</p></div>
    </div>
  </div>
</section>

<section class="s">
  <div class="shell split">
    <div>
      <p class="marker">The location</p>
      <h2 class="d2">Why Atuma-Iga.</h2>
      <p style="margin-top:1.2rem;">Thirteen minutes from Summit Junction, Asaba. Accessible from the Otulu axis or from Ubolu. Close to Cubana Millennium City, and close to the newly constructed Second Niger Bridge, which changed the movement of people and money through Asaba in a way that has not finished playing out.</p>
      <p>Asaba is a state capital still expanding outward. We are not going to quote you a percentage return, because we do not sell land as an investment product and no honest company can promise you one. What we will say is that the road, the power and the bridge are facts, and you can go and look at all three.</p>
    </div>
    <figure class="plate">
      <img src="/assets/img/delta-road-project-signboard.jpg" width="828" height="1271" alt="Delta State Government project signboard for construction of the Atuma-Iga internal road.">
      <figcaption><b>Delta State Government project board, Atuma-Iga.</b> Client: Ministry of Works, Rural &amp; Riverine Roads. Contractor: RCT Nigeria Ltd, Benin, Edo State.</figcaption>
    </figure>
  </div>
</section>

<section class="s s--dark">
  <div class="shell">
    <div class="cols">
      <div>
        <p class="marker">Standing there today</p>
        <ul class="facts">
          <li><span>Power</span><span>33KVA transformer installed</span></li>
          <li><span>Lighting</span><span>Commissioned by NDDC</span></li>
          <li><span>Internal road</span><span>Delta State, under construction</span></li>
          <li><span>Access</span><span>Graded road into the estate</span></li>
        </ul>
      </div>
      <div>
        <p class="marker">Planned, and not yet built</p>
        <ul class="facts">
          <li><span>Gate house</span><span>Planned</span></li>
          <li><span>Perimeter security</span><span>Planned</span></li>
          <li><span>Pipe-borne water</span><span>Planned</span></li>
          <li><span>Sports facility</span><span>Planned</span></li>
        </ul>
      </div>
    </div>
    <div class="call" style="margin-top:2.5rem; max-width:72ch;">
      We list these separately on purpose. Every item on the right is planned for Doctor's Residence, and none of it is finished. When one is finished, it moves to the left.
    </div>
  </div>
</section>

<section class="s">
  <div class="shell">
    <p class="marker">Price and payment</p>
    <h2 class="d2">&#8358;4.5 million for 464 square metres, documentation inclusive.</h2>
    <p class="lede measure" style="margin-top:1.2rem;">Documentation inclusive means the Deed of Assignment and registered survey plan are covered in the price. You will not receive a second invoice for the papers after you have paid for the land.</p>

    <div class="cols" style="margin-top:2.5rem;">
      <div class="tilex"><h3 class="d3">Outright payment</h3><p>Full amount. Allocation and documentation processed immediately.</p></div>
      <div class="tilex"><h3 class="d3">Instalment plan</h3><p>Spread across three to six months. NEEDS_INSTALMENT</p></div>
    </div>

    <div class="call" style="margin-top:2.5rem;">
      <strong>Buy two plots and the blocks for your fencing come from us.</strong><br>
      CPAL owns a block industry. Buy two plots at Doctor's Residence and we supply the blocks you need for dwarf fencing on your property, at no additional cost. Speak to the office on 0902 931 2069 for exact quantities.
      <br><br>
      Fencing is the thing most people postpone and then regret. An unfenced plot invites encroachment, and by the time you fly home to deal with it you are dealing with a person, not a boundary.
    </div>
  </div>
</section>

<section class="s s--warm">
  <div class="shell">
    <p class="marker">The questions people actually ask</p>
    <h2 class="display measure">Before you send anybody money.</h2>
    <ol class="index" style="margin-top:2.5rem;">
      <li><h3 class="d3">Can I buy without coming to Nigeria?</h3><p>Yes. Video inspection, documents sent to you and to your lawyer for review, payment to the corporate account, documentation issued in your name. Many buyers do it this way. Nobody is asked to skip a step because of distance.</p></li>
      <li><h3 class="d3">What does "C of O in view" actually mean?</h3><p>The estate-wide Certificate of Occupancy is being processed and has not been issued. Your Deed of Assignment and registered survey plan are what you hold in the meantime, and they are real, registered documents. We would rather tell you this plainly than have you discover it later.</p></li>
      <li><h3 class="d3">Who exactly do I pay?</h3><p>Chuks Properties Academy Limited, corporate account only. Not a realtor. Not a representative. Not a number sent to you in a WhatsApp status. Call the office on 0902 931 2069 and confirm the details with us directly before you send anything.</p></li>
      <li><h3 class="d3">What if I pay and then need to withdraw?</h3><p>You are refunded 80 percent of what you paid. A 20 percent administrative fee is deducted. This is written into the agreement you sign, so you will have read it before you commit. NEEDS_REFUND</p></li>
      <li><h3 class="d3">Can my family member inspect for me?</h3><p>Yes. Send whoever you trust. We will walk them through the same inspection, and you can join the call while they are on site.</p></li>
      <li><h3 class="d3">How many plots are left?</h3><p>Phase 1 runs along the road and holds 64 plots. Twenty have been sold. Forty-four remain. We update this page as that changes.</p></li>
    </ol>
  </div>
</section>

<section class="s s--dark">
  <div class="shell" style="text-align:center;">
    <h2 class="d2" style="max-width:22ch; margin-inline:auto;">The land is there. The road is under construction. The papers are ready to be shown.</h2>
    <p class="lede" style="margin:1.4rem auto 2rem; max-width:46ch;">The only thing left is for you to look at it. Mondays, Thursdays and Saturdays on site, or a video call scheduled around your time zone.</p>
    <div style="display:flex; gap:0.8rem; justify-content:center; flex-wrap:wrap;">
      <a class="btn btn--gold" href="WA_INSPECT" target="_blank" rel="noopener">Book an inspection</a>
      <a class="btn btn--light" href="/contact/">Contact the office</a>
    </div>
  </div>
</section>
"""

# =====================================================================
# ABOUT
# =====================================================================

ABOUT = """
<section class="hero">
  <div class="shell">
    <p class="marker">About CPAL</p>
    <h1 class="d1" style="max-width:20ch;">We started a real estate company in a country where people have learned to <em>expect the worst</em>.</h1>
    <p class="lede" style="margin-top:1.6rem; max-width:52ch;">Chuks Properties Academy Limited was founded on 26 March 2026 in Asaba, Delta State. Verified property sales, real estate training, and consultancy.</p>
  </div>
</section>

<section class="s">
  <div class="shell split">
    <div>
      <p class="marker">Why we started</p>
      <h2 class="d2">Nigeria has two deficits, and only one of them gets quoted.</h2>
    </div>
    <div class="measure">
      <p>The housing deficit is the statistic everyone knows. The second one sits on top of it: a large number of Nigerians who can afford land will not buy it, because they no longer believe the papers.</p>
      <p>They are not being irrational. They have watched it happen to people they know.</p>
      <p>We believe owning property should not be reserved for people with enormous financial resources, and it should not require a leap of faith either. Those two things are connected. When trust collapses, the only people who can safely buy land are the ones rich enough to absorb losing the money. Everybody else waits.</p>
      <p>CPAL was created to make verified property ownership accessible, and to give buyers the confidence, transparency and protection they deserve.</p>
    </div>
  </div>
</section>

<section class="s s--warm">
  <div class="shell">
    <p class="marker">How we work</p>
    <h2 class="display measure">Four rules we do not bend.</h2>
    <div class="cols" style="margin-top:2.75rem;">
      <div class="tilex"><h3 class="d3">Inspection before payment</h3><p>Always in that order, whether you live in Asaba or in Toronto. If you cannot come, we walk the plot on a live video call and you direct the camera.</p></div>
      <div class="tilex"><h3 class="d3">Documentation stated openly</h3><p>Every estate page carries a documentation record with a status against each item, including the ones that are not finished. The Certificate of Occupancy is in view, and it says so in the record.</p></div>
      <div class="tilex"><h3 class="d3">Corporate account only</h3><p>No payments to individuals, ever, for any reason. Not to a realtor, not to a representative, not to a number forwarded in a group chat.</p></div>
      <div class="tilex"><h3 class="d3">No investment language</h3><p>We sell land as ownership. We do not promise returns, percentages or guaranteed appreciation, because nobody can honestly promise those things.</p></div>
    </div>
  </div>
</section>

<section class="s">
  <div class="shell split">
    <div>
      <p class="marker">Leadership</p>
      <h2 class="d2">Dr Chukwuma Agba</h2>
      <p class="mono" style="color:var(--ink-soft); margin:0.6rem 0 1.4rem;">FOUNDER AND CHAIRMAN &middot; CPAL</p>
      <p>Known in the industry as the Property Doctor, Dr Chukwuma Agba has spent a decade in Nigerian real estate. NEEDS_TRACK_RECORD</p>
      <p>He is the author of <em>Doctor Sales Formula</em>, a book on sales practice. NEEDS_BOOK_LINK</p>
      <p>He read physics at the Federal University of Technology, Owerri, and hails from Ideato South Local Government Area of Imo State. He is a family man with three children.</p>
      <p style="color:var(--ink-soft);">He founded CPAL on the argument that runs through this entire company: that the way to sell Nigerian land is to make every claim checkable before anybody is asked to pay.</p>
    </div>
    <div class="call">
      NEEDS_FOUNDER_PHOTO
    </div>
  </div>
</section>

<section class="s s--warm">
  <div class="shell">
    <p class="marker">What we do</p>
    <div class="cols" style="margin-top:2rem;">
      <div class="tilex"><h3 class="d3">Property sales</h3><p>Verified, documented land in Delta State. Doctor's Residence Estate at Atuma-Iga is our current offering.</p><p><a href="/estates/doctors-residence/">See the estate</a></p></div>
      <div class="tilex"><h3 class="d3">CPAL Academy</h3><p>Real estate training for people entering the profession. Free for every CPAL realtor.</p><p><a href="/academy/">About the Academy</a></p></div>
      <div class="tilex"><h3 class="d3">Consultancy</h3><p>Guidance for buyers and developers on title, survey, documentation and acquisition.</p><p><a href="/contact/">Talk to us</a></p></div>
    </div>
  </div>
</section>

<section class="s s--dark">
  <div class="shell">
    <div class="measure">
      <p class="marker">A note on our age</p>
      <h2 class="d2">We were registered in March 2026. We are new, and you should factor that in.</h2>
      <p style="margin-top:1.4rem;">What we will not do is manufacture a history we do not have. Instead we have made everything about CPAL checkable: our RC number, our office address, our estate, our documentation status and the government project board on our site. Verify every one of them before you deal with us.</p>
      <p class="mono" style="margin-top:1.6rem; color:var(--gold-soft);">EMEGOZ PLAZA, BESIDE EZENEI JUNCTION, ASABA-BENIN EXPRESSWAY, ASABA, DELTA STATE &middot; RC 8324784</p>
    </div>
  </div>
</section>
"""

# =====================================================================
# REALTORS
# =====================================================================

REALTORS = """
<section class="hero">
  <div class="shell">
    <div class="hero__body">
      <div>
        <p class="marker">Realtor positions &middot; Asaba, Delta State</p>
        <h1 class="d1">You did not lie to those people. But you are the one <em>still taking their calls</em>.</h1>
        <p class="lede">CPAL is opening realtor positions in Asaba. Ten to fifteen percent commission on sales, free academy enrolment, a monthly transport allowance, and inventory with the documentation shown in the open.</p>
        <div class="row">
          <a class="btn btn--solid" href="WA_REALTOR" target="_blank" rel="noopener">Join the realtor community</a>
          <a class="btn btn--ghost" href="/realtor-hub/">See the sales kit</a>
        </div>
      </div>
      <figure class="plate">
        <img src="/assets/img/inspection-walk.jpg" width="960" height="540" alt="CPAL representatives walking clients through Doctor's Residence Estate.">
        <figcaption><b>Inspection day at Doctor's Residence.</b> Realtors bring buyers to site on Mondays, Thursdays and Saturdays.</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="s">
  <div class="shell measure">
    <p>If you have sold Nigerian real estate for any length of time, you know the position.</p>
    <p>You believed the company. You brought your family, your church, your old classmates. You told them it was safe because you were told it was safe. And when the allocation did not come, or the papers did not come, or the regulator said something in the newspaper, you were the one they called. Not the company. You.</p>
    <p>Some of you are still answering those calls. Some of you have stopped picking up. Either way, the thing you actually lost was not the commission. It was the ability to walk into a room and be believed.</p>
    <p><strong>That is what this is about.</strong></p>
  </div>
</section>

<section class="s s--warm">
  <div class="shell">
    <p class="marker">What we are offering</p>
    <h2 class="display measure">Inventory you can defend in front of your own mother.</h2>
    <div class="cols" style="margin-top:2.75rem;">
      <div class="tilex"><h3 class="d3">Documentation you can show</h3><p>Every plot carries a registered survey plan and a Deed of Assignment issued on allocation. The estate page publishes a documentation record with the status of every item, including the C of O, clearly marked as in view. You will never have to soften a fact to make a sale here.</p></div>
      <div class="tilex"><h3 class="d3">10 to 15 percent commission</h3><p>Paid on property sales. If you bring a buyer and the buyer closes, you earn. That is the entire structure.</p></div>
      <div class="tilex"><h3 class="d3">Free CPAL Academy enrolment</h3><p>Title, survey, allocation, documentation, objection handling. The things that make you sound like a professional instead of somebody reading a flyer.</p></div>
      <div class="tilex"><h3 class="d3">Monthly transport allowance</h3><p>Getting to site and getting to clients costs money before you have earned any. We cover part of that.</p></div>
      <div class="tilex"><h3 class="d3">Free media resources</h3><p>24/7 wifi and access to physical resources at our office for producing your own content.</p></div>
      <div class="tilex"><h3 class="d3">A ready sales kit</h3><p>Status graphics, teaching posts, follow-up scripts and a prospect PDF you can send today. All of it free in the realtor hub.</p></div>
    </div>
  </div>
</section>

<section class="s s--dark">
  <div class="shell">
    <div class="measure">
      <p class="marker">Read this part carefully</p>
      <h2 class="d2">Commission is paid on property sales. Nothing else.</h2>
      <p style="margin-top:1.4rem;">You do not earn from recruiting other realtors. There is no downline, no matrix, no team override, no promotion structure tied to how many people you bring in.</p>
      <p>We are saying this plainly because the model that pays you for recruitment is the model that got this industry into its current condition, and we are not going to rebuild it under a new name.</p>
      <p>You earn when land is sold to a real buyer who inspected it. That is the only way money moves here.</p>
    </div>
  </div>
</section>

<section class="s">
  <div class="shell split">
    <div>
      <p class="marker">Who we are looking for</p>
      <h2 class="d2">Experienced realtors who want a company they can stand behind.</h2>
      <p style="margin-top:1.2rem;">We are starting in Asaba and the surrounding Delta State corridor. If you have been selling already and you are looking for inventory with documentation you can show a client without flinching, this is for you.</p>
      <p class="mono" style="color:var(--ink-soft);">NEEDS_REQUIREMENT</p>
    </div>
    <ol class="index">
      <li><h3 class="d3">Join the realtor community</h3><p>Estate updates, price changes, inspection schedules and new sales materials are posted there first.</p></li>
      <li><h3 class="d3">Get your sales kit</h3><p>The realtor hub gives you graphics, scripts, teaching content and a prospect PDF you can send today.</p></li>
      <li><h3 class="d3">Enrol at CPAL Academy</h3><p>Free. Understand properly what you are selling.</p></li>
      <li><h3 class="d3">Bring your first buyer to inspection</h3><p>Mondays, Thursdays or Saturdays on site, or a video call for a client abroad.</p></li>
    </ol>
  </div>
</section>

<section class="s s--warm">
  <div class="shell" style="text-align:center;">
    <h2 class="d2" style="max-width:24ch; margin-inline:auto;">Sell something you would put your own name on.</h2>
    <p style="margin:1.3rem auto 2rem; max-width:44ch; color:var(--ink-soft);">Join the CPAL realtor community and pick up the sales kit today.</p>
    <a class="btn btn--solid" href="WA_REALTOR" target="_blank" rel="noopener">Join the realtor community</a>
  </div>
</section>
"""

# =====================================================================
# REALTOR HUB
# =====================================================================

HUB = """
<section class="hero">
  <div class="shell">
    <p class="marker">CPAL realtor hub</p>
    <h1 class="d1" style="max-width:22ch;">Everything you need to sell Doctor's Residence, <em>in one place</em>.</h1>
    <p class="lede" style="margin-top:1.5rem; max-width:52ch;">A PDF to send to prospects, graphics for your status, teaching posts, follow-up scripts and the current estate facts. Free, no login, updated as the estate changes.</p>

    <div class="call" style="margin-top:2rem; max-width:64ch;">
      <strong>Not in the CPAL realtor community yet?</strong><br>
      Estate updates, inspection schedules and new materials are posted there first.
      <span style="display:inline-block; margin-top:0.8rem;"><a class="btn btn--gold" href="GROUP_LINK" target="_blank" rel="noopener">Join the WhatsApp community</a></span>
    </div>
  </div>
</section>

<section class="s">
  <div class="shell split">
    <div>
      <p class="marker">Send this to a prospect</p>
      <h2 class="d2">The Doctor's Residence prospect pack.</h2>
      <p style="margin-top:1.2rem;">One PDF. Everything a serious buyer asks before they commit: location, price, plot size, payment plans, what is on the ground, what is planned, the documentation status and how inspection works.</p>
      <p>Send it on WhatsApp when someone says "send me details". It will do more work than a flyer, because it answers the questions instead of shouting the price.</p>
      <p><a class="btn btn--solid" href="/assets/docs/doctors-residence-prospect-pack.pdf" download>Download the prospect pack</a></p>
    </div>
    <div class="ledger">
      <div class="ledger__top"><span>Current facts &mdash; check before you quote</span><span>August 2026</span></div>
      <div class="ledger__r" style="grid-template-columns:0.8fr 1fr;"><span >Price</span><span >&#8358;4,500,000 &middot; documentation inclusive</span></div>
      <div class="ledger__r" style="grid-template-columns:0.8fr 1fr;"><span >Plot size</span><span >464 sqm</span></div>
      <div class="ledger__r" style="grid-template-columns:0.8fr 1fr;"><span >Availability</span><span >Phase 1 &middot; 44 of 64 plots remaining</span></div>
      <div class="ledger__r" style="grid-template-columns:0.8fr 1fr;"><span >Payment</span><span >Outright, or 3 to 6 months</span></div>
      <div class="ledger__r" style="grid-template-columns:0.8fr 1fr;"><span >Title</span><span >Deed of Assignment, registered survey plan</span></div>
      <div class="ledger__r" style="grid-template-columns:0.8fr 1fr;"><span >C of O</span><span >In view. Not issued.</span></div>
      <div class="ledger__r" style="grid-template-columns:0.8fr 1fr;"><span >Withdrawal</span><span >80 percent refunded, 20 percent admin fee</span></div>
      <div class="ledger__r" style="grid-template-columns:0.8fr 1fr;"><span >Inspections</span><span >Mon, Thu, Sat &middot; virtual available</span></div>
      <div class="ledger__r" style="grid-template-columns:0.8fr 1fr;"><span >Sales line</span><span >0902 931 2069</span></div>
    </div>
  </div>
</section>

<section class="s s--dark">
  <div class="shell">
    <p class="marker">Five rules</p>
    <h2 class="display measure">Break these and you are selling the way the last company sold.</h2>
    <ol class="index" style="margin-top:2.25rem;">
      <li><h3 class="d3">Quote the price on this page and nothing else</h3><p>If a client has been given a different figure, send them here.</p></li>
      <li><h3 class="d3">Never say the C of O is issued</h3><p>It is in view. Say in view. A client who finds out later will not blame CPAL, they will blame you.</p></li>
      <li><h3 class="d3">Never describe the gate house, water or sports facility as built</h3><p>They are planned. The transformer, the NDDC lighting and the state road are what is on the ground.</p></li>
      <li><h3 class="d3">Never collect payment yourself</h3><p>Buyers pay the CPAL corporate account only. Not your account, not for safekeeping, not for any reason.</p></li>
      <li><h3 class="d3">Never send account details by status or group chat</h3><p>Tell the buyer to call the office on 0902 931 2069 and confirm directly.</p></li>
    </ol>
  </div>
</section>

<section class="s">
  <div class="shell">
    <p class="marker">Status graphics</p>
    <h2 class="display measure">Post these. They are already correct.</h2>
    <p class="lede measure" style="margin-top:1.1rem;">Every graphic carries the accurate price, plot size and documentation status. Nothing here overstates what is built.</p>
    <div class="cols" style="margin-top:2.5rem;">
      <div class="tilex"><h3 class="d3">Price and plot card</h3><p>&#8358;4.5M, 464 sqm, documentation inclusive.</p></div>
      <div class="tilex"><h3 class="d3">Location and access card</h3><p>13 minutes from Summit Junction, Otulu and Ubolu access.</p></div>
      <div class="tilex"><h3 class="d3">Documentation status card</h3><p>Deed, survey, C of O in view. The honest version.</p></div>
      <div class="tilex"><h3 class="d3">What is on site now card</h3><p>Transformer, NDDC lighting, state road under construction.</p></div>
      <div class="tilex"><h3 class="d3">Two-plot block offer card</h3><p>Buy two plots, blocks for dwarf fencing supplied.</p></div>
      <div class="tilex"><h3 class="d3">Inspection day card</h3><p>Mondays, Thursdays, Saturdays. Plus a virtual inspection version for diaspora clients.</p></div>
    </div>
    <p class="mono" style="margin-top:2rem; color:var(--ink-soft);">NEEDS_GRAPHICS</p>
  </div>
</section>

<section class="s s--warm">
  <div class="shell">
    <p class="marker">Teach, do not shout</p>
    <h2 class="display measure">Content that makes people trust you before you ever pitch them.</h2>
    <p class="lede measure" style="margin-top:1.1rem;">Post one of these two or three times a week. They are written so you can post them as your own words.</p>
    <ol class="index" style="margin-top:2.25rem;">
      <li><h3 class="d3">What a Deed of Assignment actually is</h3><p>And why it is not the same thing as a Certificate of Occupancy.</p></li>
      <li><h3 class="d3">What "C of O in view" means</h3><p>And why a company that hides it is telling you something.</p></li>
      <li><h3 class="d3">How to read a survey plan before you pay</h3><p>Beacons, boundaries, and what to send to your own surveyor.</p></li>
      <li><h3 class="d3">Why you should never pay for land into a personal account</h3><p>The single most common way people lose money in this market.</p></li>
      <li><h3 class="d3">Five questions to ask any estate company before you send money</h3><p>If they cannot answer all five, walk away.</p></li>
      <li><h3 class="d3">How to buy land in Nigeria from abroad without getting burned</h3><p>The diaspora post. This one travels furthest.</p></li>
      <li><h3 class="d3">What encroachment is, and why fencing early matters</h3><p>Sets up the two-plot block offer without pitching it.</p></li>
    </ol>
  </div>
</section>

<section class="s">
  <div class="shell">
    <p class="marker">Scripts</p>
    <h2 class="display measure">What to say when they say that.</h2>
    <div class="cols" style="margin-top:2.5rem;">
      <div class="tilex"><h3 class="d3">"Send me details"</h3><p>Give price and plot size, send the prospect pack, then ask one qualifying question instead of waiting.</p></div>
      <div class="tilex"><h3 class="d3">"It is too expensive"</h3><p>Reframe to cost per square metre, and to what documentation inclusive removes from the bill.</p></div>
      <div class="tilex"><h3 class="d3">"I have been scammed before"</h3><p>Do not defend the industry. Agree with them, then walk them to the documentation record and the government project board.</p></div>
      <div class="tilex"><h3 class="d3">"Let me think about it"</h3><p>The inspection invite, not the follow-up nag.</p></div>
      <div class="tilex"><h3 class="d3">The client is abroad</h3><p>How to offer and run a video inspection, and how to include their family member on the call.</p></div>
      <div class="tilex"><h3 class="d3">Follow-up sequence</h3><p>Day 1, day 3, day 7, day 14 and day 30 messages that do not sound like a robot.</p></div>
    </div>
    <p class="mono" style="margin-top:2rem; color:var(--ink-soft);">NEEDS_SCRIPTS</p>
  </div>
</section>

<section class="s s--dark">
  <div class="shell">
    <p class="marker">Estate footage</p>
    <h2 class="display measure">Video you can repost.</h2>
    <p class="mono" style="margin-top:1.4rem; color:var(--gold-soft);">NEEDS_VIDEO</p>
  </div>
</section>
"""

# =====================================================================
# ACADEMY
# =====================================================================

ACADEMY = """
<section class="hero">
  <div class="shell">
    <p class="marker">CPAL Academy</p>
    <h1 class="d1" style="max-width:22ch;">Most Nigerian realtors were handed a flyer and told to <em>go and sell</em>.</h1>
    <p class="lede" style="margin-top:1.5rem; max-width:52ch;">CPAL Academy trains realtors to understand title, survey, allocation and documentation. Free enrolment for every CPAL realtor.</p>
  </div>
</section>

<section class="s">
  <div class="shell split">
    <div>
      <p class="marker">Why it exists</p>
      <h2 class="d2">A realtor who can read a survey plan cannot be used.</h2>
    </div>
    <div class="measure">
      <p>The reason so many buyers were misled is not that every realtor was dishonest. A large number of them simply did not know. They repeated what the company told them, in good faith, to people who trusted them, and they found out at the same time everybody else did.</p>
      <p>Training is not a bonus we attach to the commission. It is the reason the word academy is in our name.</p>
    </div>
  </div>
</section>

<section class="s s--warm">
  <div class="shell">
    <p class="marker">What you learn</p>
    <div class="cols" style="margin-top:2rem;">
      <div class="tilex"><h3 class="d3">Title documents</h3><p>What each one is, what it is not, and what a buyer actually receives at each stage.</p></div>
      <div class="tilex"><h3 class="d3">Survey plans and boundaries</h3><p>Beacons, boundaries, and how to check a plan before a client pays.</p></div>
      <div class="tilex"><h3 class="d3">Allocation</h3><p>What should happen between payment and possession, and how long it should take.</p></div>
      <div class="tilex"><h3 class="d3">Government documentation</h3><p>What a Certificate of Occupancy is, how it is obtained, and how long it realistically takes.</p></div>
      <div class="tilex"><h3 class="d3">Honest selling</h3><p>How to present a property fully without overstating a single thing about it.</p></div>
      <div class="tilex"><h3 class="d3">Selling to diaspora clients</h3><p>Running a virtual inspection, and handling objections from buyers who have been burned before.</p></div>
    </div>
    <p class="mono" style="margin-top:2rem; color:var(--ink-soft);">NEEDS_ACADEMY_FORMAT</p>
  </div>
</section>

<section class="s">
  <div class="shell" style="text-align:center;">
    <h2 class="d2" style="max-width:22ch; margin-inline:auto;">Free for every CPAL realtor.</h2>
    <p style="margin:1.3rem auto 2rem; max-width:44ch; color:var(--ink-soft);">Join the realtor community and your enrolment is included.</p>
    <a class="btn btn--solid" href="/realtors/">Become a CPAL realtor</a>
  </div>
</section>
"""

# =====================================================================
# CONTACT
# =====================================================================

CONTACT = """
<section class="hero">
  <div class="shell">
    <div class="hero__body">
      <div>
        <p class="marker">Contact CPAL</p>
        <h1 class="d1">Ask us the <em>difficult questions</em> first.</h1>
        <p class="lede">We would rather answer twenty questions than take a payment from someone who is not sure.</p>
        <div class="row">
          <a class="btn btn--solid" href="WA_LINK" target="_blank" rel="noopener">Chat on WhatsApp</a>
          <a class="btn btn--ghost" href="tel:+2349029312069">Call 0902 931 2069</a>
        </div>
      </div>
      <div class="ledger">
        <div class="ledger__top"><span>Contact record</span><span>CPAL</span></div>
        <div class="ledger__r" style="grid-template-columns:0.7fr 1fr;"><span >Office</span><span >Emegoz Plaza, beside Ezenei Junction, along Asaba-Benin Expressway, Asaba, Delta State</span></div>
        <div class="ledger__r" style="grid-template-columns:0.7fr 1fr;"><span >Phone</span><span >0902 931 2069</span></div>
        <div class="ledger__r" style="grid-template-columns:0.7fr 1fr;"><span >Email</span><span >cpalrealities@gmail.com</span></div>
        <div class="ledger__r" style="grid-template-columns:0.7fr 1fr;"><span >Inspections</span><span >Mondays, Thursdays, Saturdays &middot; virtual by arrangement</span></div>
        <div class="ledger__r" style="grid-template-columns:0.7fr 1fr;"><span >Registration</span><span >RC 8324784</span></div>
      </div>
    </div>
  </div>
</section>

<section class="s">
  <div class="shell split">
    <div>
      <h2 class="d2">Send us a message.</h2>
      <p style="margin-top:1.2rem; color:var(--ink-soft);">We reply on WhatsApp unless you tell us otherwise.</p>
      <div class="call" style="margin-top:1.75rem;">
        <strong>Before you pay anyone.</strong> If your enquiry is about payment, we confirm account details with you directly by call or in writing. Never act on account details sent to you through a status update, a group chat or a forwarded flyer. Call the office on 0902 931 2069 and check.
      </div>
    </div>

    <form id="waform" novalidate>
      <div class="field"><label for="name">Full name</label><input id="name" name="name" type="text" required></div>
      <div class="field"><label for="email">Email address</label><input id="email" name="email" type="email" required autocomplete="email" placeholder="So we can send you documents"><span class="err">We need a valid email to send the survey plan and deed</span></div>
      <div class="field"><label for="phone">Phone number for calls</label><input id="phone" name="phone" type="tel" required autocomplete="tel" inputmode="tel" placeholder="If it differs from your WhatsApp number"><span class="err">Please enter a number we can reach you on</span></div>
      <div class="field"><label for="based">Where are you based</label><input id="based" name="based" type="text" placeholder="City and country"></div>
      <div class="field"><label for="topic">What is this about</label>
        <select id="topic" name="topic">
          <option>Book an inspection</option>
          <option>General enquiry</option>
          <option>Realtor enquiry</option>
        </select>
      </div>
      <div class="field"><label for="message">Your question</label><textarea id="message" name="message" rows="5"></textarea></div>
      <button class="btn btn--solid" type="submit">Send message</button>
    </form>
  </div>
</section>
"""


def main():
    estate = (ESTATE.replace('WA_INSPECT', WA_INSPECT)
                    .replace('WA_LINK', WA)
                    .replace('NEEDS_INSTALMENT', '<!-- NEEDS: deposit amount and monthly breakdown for the 3-month and 6-month plans -->Speak to the office on 0902 931 2069 for the deposit and monthly schedule.')
                    .replace('NEEDS_REFUND', '<!-- NEEDS: refund processing timeline, and what happens on instalment default -->'))
    page('/estates/doctors-residence/',
         "Doctor's Residence Estate, Atuma-Iga | 464 sqm from N4.5M | CPAL",
         "Doctor's Residence Estate, Atuma-Iga, Delta State. 464 sqm plots at N4.5M, documentation inclusive. 44 of 64 plots remaining. Deed of Assignment and registered survey plan. Physical and virtual inspections.",
         estate)

    about = (ABOUT.replace('NEEDS_TRACK_RECORD', '<!-- NEEDS: which companies, which estates, how many transactions. This single detail is the most valuable line on the page. -->')
                  .replace('NEEDS_BOOK_LINK', '<!-- NEEDS: link to where the book can be bought -->')
                  .replace('NEEDS_FOUNDER_PHOTO', '<strong>Photograph pending.</strong> A portrait of Dr Agba goes here. For a company registered five months ago, a real face on this page carries more weight than anything else on it.'))
    page('/about/',
         "About CPAL | Chuks Properties Academy Limited, Asaba",
         "Chuks Properties Academy Limited, founded 26 March 2026 in Asaba, Delta State. Verified property sales, real estate training and consultancy. RC 8324784.",
         about)

    realtors = (REALTORS.replace('WA_REALTOR', WA_REALTOR)
                        .replace('NEEDS_REQUIREMENT', '<!-- NEEDS: confirmed minimum requirement. Recommend: active realtor with prior sales experience, or complete CPAL Academy onboarding before commission-bearing status. -->'))
    page('/realtors/',
         "Become a CPAL Realtor | 10 to 15 percent commission, Asaba",
         "CPAL is opening realtor positions in Asaba. 10 to 15 percent commission on property sales, free CPAL Academy enrolment, monthly transport allowance and a full sales kit.",
         realtors)

    hub = (HUB.replace('GROUP_LINK', GROUP)
              .replace('NEEDS_GRAPHICS', 'Download links go live as each graphic is produced.')
              .replace('NEEDS_SCRIPTS', 'Full scripts are published here as they are written.')
              .replace('NEEDS_VIDEO', 'ESTATE FOOTAGE PENDING'))
    page('/realtor-hub/',
         "CPAL Realtor Hub | Sales kit for Doctor's Residence",
         "Free sales kit for CPAL realtors. Prospect PDF, status graphics, teaching content, follow-up scripts and current estate facts for Doctor's Residence Estate.",
         hub)

    page('/academy/',
         "CPAL Academy | Real estate training in Asaba, Delta State",
         "CPAL Academy trains realtors in title, survey, allocation and documentation. Free enrolment for every CPAL realtor.",
         ACADEMY.replace('NEEDS_ACADEMY_FORMAT', 'Format and schedule are confirmed on enrolment. Speak to the office on 0902 931 2069.'))

    page('/contact/',
         "Contact CPAL | Book an inspection in Asaba, Delta State",
         "Contact Chuks Properties Academy Limited. Emegoz Plaza, beside Ezenei Junction, Asaba-Benin Expressway, Asaba. Inspections Mondays, Thursdays and Saturdays.",
         CONTACT.replace('WA_LINK', WA))


if __name__ == '__main__':
    main()
