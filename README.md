# cpalgroup.com

Website for **Chuks Properties Academy Limited** (CPAL), Asaba, Delta State. RC 8324784.

Static HTML. No build step, no framework, no dependencies. The host publishes the repository root as-is.

## Pages

| Path | Purpose |
|---|---|
| `/` | Homepage |
| `/estates/doctors-residence/` | Long-form sales page for the estate |
| `/about/` | Company and Dr Chukwuma Agba |
| `/academy/` | CPAL Academy |
| `/realtors/` | Realtor recruitment |
| `/realtor-hub/` | Internal materials for realtors |
| `/contact/` | Contact and enquiry form |
| `/blog/` | Guides (SEO) |

## Content rules — read before editing

These five things must **never** appear on this site. Each one is a legal or regulatory risk,
not a style preference.

1. **Never write the Certificate of Occupancy as issued.** It is in process. Write "in process".
   The site frames this as a *stage in the normal sequence* rather than a shortcoming: every estate
   moves through acquisition, survey, allocation and C of O, and the price rises at each step. That
   framing is why 464 sqm here is N4.5M against N12.5M nearby. Keep that framing; do not revert to
   apologetic wording, and do not remove the honest status.
2. **Never state or imply an investment return, percentage or future value.** Land is sold as
   ownership. Show the bridge, the road contract and the other developers, and let the reader draw
   their own conclusion. This is what the SEC action against PWAN turned on.
3. **Never describe planned facilities in the present tense.** The gate house, perimeter security,
   pipe-borne water and sports facility are planned, not built.
4. **Never round the plot count.** It is 44 of 64 remaining. Accuracy is the argument of this site.
   Update it in: `/index.html` (facts strip, availability block), `/estates/doctors-residence/`
   (facts strip, scarcity band), `/realtor-hub/` (facts table).
5. **Never mention Phase 2.** It has not launched. Mentioning it creates wait-and-see behaviour.

## Contact form

Does not post anywhere. It composes the visitor's answers into a WhatsApp message to 0806 789 8622.
Name, email and phone are required and validated (phone counts digits only, 7–15, so +234 and
diaspora formats pass). To change the destination, edit the `wa.me` number in the script at the
bottom of `/contact/index.html`.

## Lead magnet

The 17-page buyer pack (`/assets/docs/`) is gated behind a WhatsApp message rather than an email
form. The button opens a chat with the request pre-written. CPAL replies with the PDF, which starts
a conversation rather than filling a list nobody works.

## Fonts

Self-hosted in `/assets/fonts/` as subset WOFF2, ~116KB total. They are **not** loaded from Google
Fonts, deliberately: an external stylesheet is a render blocker, and on a slow or filtered connection
the browser waits for it before painting anything. Do not reintroduce a `fonts.googleapis.com` link.

## Videos

Load only when tapped. The poster is a still; the player is injected on click. This keeps the page
light on mobile data and avoids empty frames.

## Rebuilding pages

`_tools/build.py` holds the shared header, footer and CTA components.
`_tools/pages.py` generates about, academy, realtors, realtor-hub and contact.
`_tools/blog.py` generates the guides index and articles.

Run from the project root:

```
python3 _tools/pages.py
python3 _tools/blog.py
```

The homepage and estate page are hand-maintained; edit their HTML directly.

## Adding a blog post

Add an entry to `POSTS` and a matching key in `BODY` in `_tools/blog.py`, then run it. Add the URL
to `sitemap.xml`.

Target local buyer-intent searches rather than broad terms. Working list: cost of land in specific
Asaba areas, document explainers, buying from abroad, verification checklists, land banking in Delta
State, Oshimili North area guides.

## Outstanding from the client

- Dr Agba's doctorate field (earned or honorary)
- Where *Doctor Sales Formula* can be purchased
- Where the decade of experience was spent — the single most valuable addition to `/about/`
- Exact block quantity for the two-plot offer
- Aerial footage and the estate survey layout
