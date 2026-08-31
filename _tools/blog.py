#!/usr/bin/env python3
"""Generates the guides section. Run: python3 _tools/blog.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build import write, cta_band, magnet, WA, WA_ICON, PHONE

POSTS = [
    dict(slug='cost-of-land-in-atuma-iga-asaba',
         title='How much does land cost in Atuma-Iga, Asaba? (2026 prices)',
         desc='What plots actually cost at Atuma-Iga in 2026, what drives the price differences between estates, and what should be included before you agree to any figure.',
         card='What plots really cost around Atuma-Iga right now, and why two estates on the same road can differ by three million naira.',
         img='/assets/img/aerial-estate.jpg',
         date='2026-08-12'),
    dict(slug='deed-of-assignment-vs-certificate-of-occupancy',
         title='Deed of Assignment vs Certificate of Occupancy: what Nigerian land buyers should know',
         desc='A plain explanation of the two documents most often confused by Nigerian land buyers, what each one proves, and which questions to ask before you pay.',
         card='The two documents buyers most often confuse, explained plainly, with the questions to ask about each.',
         img='/assets/img/handover.jpg',
         date='2026-08-05'),
    dict(slug='buy-land-in-asaba-from-abroad',
         title='How to buy land in Asaba safely when you live abroad',
         desc='A practical process for buying Nigerian land from the diaspora: virtual inspection, document verification, payment safety and who to involve at each step.',
         card='A step-by-step process for buying from the diaspora without flying home, and the checks that make it safe.',
         img='/assets/img/hero-couple.jpg',
         date='2026-07-28'),
    dict(slug='what-to-check-before-buying-land-delta-state',
         title='What to check before you pay for any land in Delta State',
         desc='A verification checklist for Nigerian land buyers: title documents, survey, government activity, company registration and payment safety.',
         card='A checklist you can use on any estate in Delta State, including ours, before you part with money.',
         img='/assets/img/sign-crop.jpg',
         date='2026-07-20'),
]

# ---------------------------------------------------------------- INDEX
cards = ''
for p in POSTS:
    cards += f'''        <a class="post" href="/blog/{p['slug']}/">
          <div class="post__img"><img src="{p['img']}" alt="" width="1536" height="1024" loading="lazy"></div>
          <h3>{p['title']}</h3>
          <p>{p['card']}</p>
          <span class="post__more">Read the guide</span>
        </a>
'''

write('/blog/',
  "Guides for Nigerian land buyers | CPAL, Asaba",
  "Practical guides for anyone buying land in Asaba and Delta State: what plots cost, which documents matter, how to buy from abroad, and what to verify before you pay.",
  f'''
  <section class="s s--navy" style="padding-bottom:clamp(40px,5vw,60px);">
    <div class="shell">
      <p class="kicker">Guides</p>
      <h1>Straight answers for people buying land.</h1>
      <p class="lede" style="margin-top:18px; max-width:56ch;">Written for buyers in Asaba and Delta
         State, including the questions people are often too polite to ask an estate company directly.
         Use these on us as readily as on anybody else.</p>
    </div>
  </section>

  <section class="s">
    <div class="shell">
      <div class="posts">
{cards}      </div>
    </div>
  </section>
''' + magnet())


# ---------------------------------------------------------------- ARTICLES
def article(p, body):
    return f'''
  <section class="s" style="padding-bottom:clamp(30px,4vw,48px);">
    <div class="shell">
      <div class="article">
        <p class="kicker">Guide</p>
        <h1 style="font-size:clamp(1.9rem,4.6vw,2.7rem);">{p['title']}</h1>
        <p class="lede" style="margin-top:18px;">{p['desc']}</p>
      </div>
    </div>
  </section>

  <section class="s--tight" style="padding-top:0;">
    <div class="shell">
      <div class="article">
{body}
        <p style="margin-top:2.4em;"><a href="/blog/">&larr; All guides</a></p>
      </div>
    </div>
  </section>
'''


BODY = {}

BODY['cost-of-land-in-atuma-iga-asaba'] = '''
        <p>Atuma-Iga sits in Oshimili North Local Government Area, a short drive from Asaba along the
           Otulu or Ubolu axis. It has become one of the more active land markets around the city, and
           prices there now vary widely enough to confuse a first-time buyer.</p>

        <h2>What plots cost right now</h2>
        <p>Based on publicly listed prices on Nigerian property portals as at August 2026, plots in and
           around Atuma-Iga and wider Oshimili North fall roughly into these bands:</p>
        <ul>
          <li>Around <b>&#8358;4.5 million</b> for 464 sqm with a Deed of Assignment and registered
              survey plan, where the estate-wide Certificate of Occupancy is still in progress</li>
          <li>Around <b>&#8358;7.5 million</b> for 450 sqm at a comparable stage of documentation</li>
          <li>Around <b>&#8358;12.5 million</b> for 464 sqm in an estate already holding a full
              Certificate of Occupancy</li>
          <li><b>&#8358;80 million and above</b> for 560 sqm in a premium serviced development such as
              Cubana Millennium City</li>
        </ul>
        <p>Expressed per square metre, that is roughly &#8358;9,700 at the lower end and &#8358;142,900
           at the top. Those are not different markets. They are plots within the same general area,
           priced against different levels of documentation, infrastructure and brand.</p>

        <h2>Why two estates on the same road differ by millions</h2>
        <p>Three things account for most of the gap.</p>
        <h3>1. How far the title has progressed</h3>
        <p>An estate that already holds a full Certificate of Occupancy has completed a process that
           takes time and money, and it prices accordingly. An estate still processing its C of O sells
           for less. Neither is automatically better. What matters is that you are told plainly which
           one you are buying, in writing, before you pay.</p>
        <h3>2. What infrastructure already exists</h3>
        <p>Power, roads, drainage, perimeter walls and gate houses all cost money, and estates that have
           built them recover that in the plot price. Ask specifically which items are installed today
           and which are planned. A rendering of a gate house is not a gate house.</p>
        <h3>3. What is actually included in the quoted price</h3>
        <p>This is where buyers most often lose money without noticing. In some estates the quoted figure
           covers the land only, and documentation, survey and deed fees follow as separate invoices.
           Always ask the question directly: <i>is this price documentation inclusive, and what exactly
           does that include?</i></p>

        <h2>What should be included before you accept any figure</h2>
        <ul>
          <li>The plot itself, with its size stated in square metres, not vague terms like "a plot"</li>
          <li>A Deed of Assignment issued in your name on allocation</li>
          <li>A registered survey plan for your specific plot</li>
          <li>Physical beacons shown to you on the ground</li>
          <li>A written statement of the estate-wide title status, whatever that status is</li>
        </ul>

        <h2>A note on future value</h2>
        <p>You will hear a great deal about appreciation at Atuma-Iga, and it is worth being careful here.
           No company can honestly guarantee what land will be worth later, and any that does is telling
           you something useful about itself.</p>
        <p>What you can do is look at what already exists. The Second Niger Bridge was completed in 2023.
           The Delta State Ministry of Works has a road contract running into the area. Several
           independent developers have committed capital to the same village. Those are facts you can
           verify, and what you conclude from them is your own judgement to make.</p>

        <h2>Before you agree a price anywhere</h2>
        <p>Ask for the price per square metre rather than the headline figure, since that is the only way
           to compare estates fairly. Ask what is included. Ask what the title status is, in writing. And
           inspect the land before any money moves.</p>
'''

BODY['deed-of-assignment-vs-certificate-of-occupancy'] = '''
        <p>These two documents cause more confusion among Nigerian land buyers than anything else, and
           that confusion is expensive. Here is what each one actually is, in plain terms.</p>

        <h2>Certificate of Occupancy, in plain terms</h2>
        <p>Under the Land Use Act, land in each Nigerian state is held in trust by the Governor. A
           Certificate of Occupancy, usually called a C of O, is the document the state issues granting
           the holder a right of occupancy over a particular piece of land, normally for 99 years.</p>
        <p>It is the strongest ordinary evidence of title a private holder can have, because it comes
           from the state itself.</p>

        <h2>Deed of Assignment, in plain terms</h2>
        <p>A Deed of Assignment is the document that transfers an interest in land from one party to
           another. When you buy a plot in an estate, the deed is what moves that plot from the seller
           to you, in your name.</p>
        <p>It is a real, legally significant document. It is the instrument that records your purchase.
           What it is not is a substitute for the state-issued C of O, and any company that presents it
           as one is misleading you.</p>

        <h2>How they work together</h2>
        <p>In a typical Nigerian estate the developer holds, or is processing, a C of O covering the whole
           estate. Individual buyers then receive a Deed of Assignment for their specific plot, along
           with a registered survey plan. Later, a buyer may process their own title documents for their
           individual plot.</p>
        <p>So the honest position for most estate purchases is: you hold a deed and a survey plan in your
           name, and the estate holds or is processing the overarching title.</p>

        <h2>The question that matters</h2>
        <p>Not "do you have a C of O" — almost everyone will say yes to that. Ask instead:</p>
        <p><b>"Is the estate-wide Certificate of Occupancy issued, or still in process? And will you put
           that answer in writing?"</b></p>
        <p>The answer itself is less important than whether they will commit to it on paper. An estate
           with a C of O still in process that says so plainly is a safer counterparty than one that
           blurs the question.</p>

        <h2>Other documents worth asking about</h2>
        <ul>
          <li><b>Registered survey plan</b> — your plot's boundaries, lodged with the state surveyor
              general. Ask for the survey number.</li>
          <li><b>Governor's consent</b> — required for a valid transfer of land already under a right of
              occupancy. Ask whether it applies to your transaction and who is responsible for it.</li>
          <li><b>Excision or gazette</b> — evidence that land has been released from government
              acquisition, relevant in some areas.</li>
          <li><b>Company registration</b> — the seller's RC number, verifiable on the Corporate Affairs
              Commission register.</li>
        </ul>

        <h2>Two things to be careful about</h2>
        <p>First, a receipt is not a title document. Neither is an allocation letter on its own. They
           evidence a payment or an allocation, not ownership.</p>
        <p>Second, take whatever you are given to your own lawyer or surveyor before you pay, not after.
           A few hours of professional review costs a fraction of a plot and is the single best money a
           land buyer spends.</p>
'''

BODY['buy-land-in-asaba-from-abroad'] = '''
        <p>Buying land in Nigeria from abroad is entirely normal and done successfully every day. It is
           also where a disproportionate number of bad stories start, because distance removes the
           checks a local buyer takes for granted.</p>
        <p>Here is a process that keeps those checks in place.</p>

        <h2>1. Establish who you are dealing with</h2>
        <p>Before anything else, confirm the company exists as a company. Ask for the registered name and
           RC number and verify it on the Corporate Affairs Commission register. Ask for a physical office
           address, then confirm somebody can actually visit it.</p>
        <p>A company that is reluctant to give you its registration details has already answered your
           most important question.</p>

        <h2>2. Inspect the land, even from six thousand kilometres away</h2>
        <p>Never buy land you have not seen. Distance is not an exception to this.</p>
        <p>Ask for a live video inspection rather than a recorded tour. On a live call you can direct the
           camera, and that difference matters. Ask them to show you:</p>
        <ul>
          <li>The specific plot, and its beacons</li>
          <li>The access road into the estate</li>
          <li>Any infrastructure they have claimed, such as a transformer</li>
          <li>Any government signage in the area</li>
          <li>The surrounding land, so you see the context and not just a framed shot</li>
        </ul>
        <p>Record the call. A company that objects to being recorded while making factual claims is
           telling you something.</p>

        <h2>3. Send somebody you trust</h2>
        <p>A video call is good. A person on the ground is better. A relative, a friend, or an
           independent surveyor you engage yourself. Ideally somebody with no relationship to the seller
           at all.</p>

        <h2>4. Have the documents reviewed before you pay</h2>
        <p>Ask for the draft Deed of Assignment, the survey plan and the written terms, and send them to
           a Nigerian lawyer you have engaged yourself. Not one recommended by the seller.</p>
        <p>This is the step diaspora buyers most often skip because of time zones and momentum. It is the
           step that would have prevented most of the stories you have heard.</p>

        <h2>5. Pay the company, never a person</h2>
        <p>This is where most diaspora fraud actually happens, and it is worth being blunt about it. The
           estate is often real. The plot is often real. The account number, forwarded through a WhatsApp
           status, a group chat or an enthusiastic agent, is not.</p>
        <p>Rules that protect you:</p>
        <ul>
          <li>Pay only into a corporate account in the company's registered name</li>
          <li>Never pay an individual, and never a realtor, however well you know them</li>
          <li>Confirm account details by calling the company's published office line yourself, on a
              number you found on their website rather than one sent to you</li>
          <li>Treat any urgency around payment as a reason to slow down, not speed up</li>
        </ul>

        <h2>6. Keep your own records</h2>
        <p>Keep the recording of your inspection call, the written terms, proof of payment, and your
           issued documents in one place. If a question arises in five years, you will be glad it is all
           together.</p>

        <h2>A realistic note</h2>
        <p>None of this makes buying from abroad risk-free, and anybody telling you otherwise is selling.
           What it does is remove the specific failures that catch careful people: unverified companies,
           unseen land, unreviewed documents and misdirected payments.</p>
'''

BODY['what-to-check-before-buying-land-delta-state'] = '''
        <p>Use this on any estate in Delta State, including ours. If a company cannot answer these
           comfortably, that itself is the answer.</p>

        <h2>The company</h2>
        <ul>
          <li>What is the registered company name and RC number? Verify it on the Corporate Affairs
              Commission register yourself.</li>
          <li>Where is the physical office, and can you or somebody you trust walk into it?</li>
          <li>Who is the person behind the company, and are they publicly identifiable?</li>
        </ul>

        <h2>The land</h2>
        <ul>
          <li>Which Local Government Area is it actually in? Confirm this independently rather than
              accepting the brochure, as it is more often wrong than you would expect.</li>
          <li>Is there any dispute, family claim or government acquisition affecting the land?</li>
          <li>Can you see the beacons for your specific plot on the ground?</li>
          <li>What is the plot size in square metres, stated precisely?</li>
        </ul>

        <h2>The documents</h2>
        <ul>
          <li>What exactly will you receive, and when?</li>
          <li>Is the estate-wide Certificate of Occupancy issued or in process? Ask for that answer in
              writing.</li>
          <li>Is the survey plan registered, and what is the survey number?</li>
          <li>Is documentation included in the quoted price, or invoiced separately later?</li>
        </ul>

        <h2>The infrastructure</h2>
        <ul>
          <li>Which facilities exist on the ground <i>today</i>, and which are planned?</li>
          <li>Is there any government project committed to the area? Can you photograph the project
              board?</li>
          <li>Who is responsible for internal roads and drainage, and by when?</li>
        </ul>

        <h2>The money</h2>
        <ul>
          <li>What is the full price, and what does it include?</li>
          <li>What is the minimum deposit and the completion window?</li>
          <li>What penalty applies if you default, and in what amount?</li>
          <li>What is the refund policy, and what fee is deducted?</li>
          <li>Which account do you pay into, and is it a corporate account in the company's registered
              name?</li>
        </ul>

        <h2>The three answers that should end a conversation</h2>
        <p>Walk away if you hear any of these:</p>
        <ul>
          <li><b>A guaranteed return or a promised percentage.</b> Land is ownership, not a regulated
              investment product. Companies that promise returns on land have a poor record in this
              country.</li>
          <li><b>Earnings for recruiting other people.</b> If income depends on who you bring in rather
              than what is sold, you are not looking at a property business.</li>
          <li><b>Pressure to pay today.</b> Genuine scarcity is a fact and can be stated calmly. Manufactured
              urgency exists to stop you checking things.</li>
        </ul>

        <h2>Finally, get it reviewed</h2>
        <p>Take every document to your own lawyer or surveyor before any money moves. It costs a small
           fraction of the plot price and it is the single most useful thing a land buyer can do.</p>
'''

for p in POSTS:
    write(f"/blog/{p['slug']}/",
          f"{p['title']} | CPAL",
          p['desc'],
          article(p, BODY[p['slug']]) + cta_band(
              'Questions about Doctor&rsquo;s Residence?',
              'Ask us anything on this list. We would rather answer twenty questions than take a '
              'payment from somebody who is not sure.',
              'I%20read%20one%20of%20your%20guides%20and%20have%20a%20question.',
              'Ask on WhatsApp'),
          og=p['img'])

print('Blog done.')
