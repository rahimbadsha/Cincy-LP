# Cover Cincy Landing Page — Copy & Brand Reference

Source of truth for page text. Items marked **[CLIENT]** come from the client brief (don't change without approval).
Items marked **[DRAFT]** are our supporting copy — client can approve or edit.
Items marked **[PLACEHOLDER]** need real content from the client.

---

## Global

| Element | Copy |
|---|---|
| Page title (SEO) | Free Health Insurance Consult for the Self-Employed \| Cover Cincy **[DRAFT]** |
| Meta description | Local, independent health insurance help since 1988. Book a free 15-minute consult with a licensed Cincinnati broker who works for you, not the carriers. **[DRAFT]** |
| Phone | (513) 800-2255 — `tel:+15138002255` |
| Navigation | None. Logo is not a link. No external links (except privacy policy in footer — see open items). |

---

## Section 1 — Hero

- Headline: **Health insurance help from someone who actually works for you.** **[CLIENT]**
- Subhead: **Local, independent, since 1988. Free consult.** **[CLIENT]**
- Primary CTA: **Book Your Free Consult** → scrolls to booking calendar (`#book`) **[CLIENT]**
- Secondary link: Watch video → scrolls to brand video (`#video`) **[DRAFT]**
- Trust badges: **A+ BBB · Since 1988 · Licensed Nationwide** **[CLIENT]**

Team card (desktop: 2×2 photo grid · mobile: avatar row) **[DRAFT]**:
- Title: Meet your local brokers
- Photos + first names: Ashton, William, McKala, Jeff (real headshots from covercincy.com/insuranceagents)
- Note: One of these licensed brokers will personally take your call.
- ⚠️ Only accurate while the page books into the `u11` round-robin (Ashton West, William Patterson, McKala Bracci, Jeff Gorsuch). Update if the meeting link changes.

Background: Cincinnati skyline at night (public domain, CC0, Wikimedia Commons), dark overlay.

---

## Section 2 — Brand Message Video

- Heading: **See what makes us different.** **[CLIENT]** ("different." in red)
- Feature points **[DRAFT]**:
  - Local Cincinnati team
  - Independent: we compare many carriers
  - Private & Marketplace plans
  - Free, no-obligation advice
- Video: muted autoplay, captions on, sound on tap/click **[CLIENT]**
- Sound button label: Tap for sound **[DRAFT]**
- CTA below video: **Book Your Free Consult** **[CLIENT]**
- Video file: **[PLACEHOLDER]** — prototype uses existing YouTube video `gaUNawXf3A8` ("As Seen On Ask the Expert"). Final: MP4 + captions file (.vtt) from client.

---

## Section 3 — Testimonials

- Heading / trust line: **Real Cincinnati families. Real coverage that shows up.** **[CLIENT]**
- Card layout: video poster → play button → quote → name in red · neighborhood
- Quote per card: **[PLACEHOLDER]** short quote pulled from each client's video
- Poster: **[PLACEHOLDER]** — prototype uses skyline crops; final = real video thumbnails (no stock faces: would read as fake testimonials)
- 2–3 real client testimonial videos **[CLIENT]**
  - Video 1: **[PLACEHOLDER]** — client name, neighborhood, video
  - Video 2: **[PLACEHOLDER]**
  - Video 3: **[PLACEHOLDER]**
- CTA: **Book Your Free Consult** **[CLIENT]**

> Never write fake testimonials or names. Only real client content.

---

## Section 4 — Booking Block (`#book`)

- Heading: Pick a time for your free consult. **[DRAFT]** ("free consult." in red)
- Reassurance: **Free · No obligation · 15 minutes · We work for you, not the insurance carriers.** **[CLIENT]**
- Calendar: HubSpot Meetings embed, full width, minimal fields **[CLIENT]**
  - Prototype link: `https://meetings.hubspot.com/aruhlman/u11?embed=true`
    (the same round-robin link the live /book page uses for Ohio + under-65 health: Ashton, William, Jeff, McKala)
- Phone fallback banner (dark, with McKala's photo) **[CLIENT]** phone / **[DRAFT]** wording:
  - Title: Prefer to talk to a real person now?
  - Text: Call our local office and talk with our team.
  - Phone: (513) 800-2255
- Trust strip: official BBB A+ seal + USA Benefits Group "Established 1988" badge

## Footer
- © {year} Cover Cincy · A USA Benefits Group agency **[DRAFT]**
- Privacy Policy link **[DRAFT — see open items]**

## Mobile sticky bar
- Shows after hero CTA scrolls away, hides when booking block is visible.
- Button: Book Free Consult · Phone icon button → call.

---

## Brand tokens

| Token | Value | Use |
|---|---|---|
| Red | `#A72A2C` | Primary CTA, accents (from live site) |
| Red dark | `#8A2224` | CTA hover |
| Black | `#0F0F10` | Hero / dark sections |
| Ink | `#1A1A1A` | Body text on light |
| Gray 600 | `#5A5A5F` | Secondary text |
| Gray 100 | `#F3F3F4` | Light section background |
| White | `#FFFFFF` | |
| Headings font | Space Grotesk (used on live site) | |
| Body font | Inter | |

Navy `#253A5E` from the live site is intentionally NOT used (brief: gray, black, white, red).

## Header
- Logo + "CoverCincy" (not a link) · "Call us today" + red phone button **[DRAFT]**

## Assets

Local (in `landing-page/images/`, optimized):
- `cincinnati-skyline-night.jpg` / `-sm.jpg` — Wikimedia Commons "Downtown Cincinnati skyline at night", **CC0 public domain** (no attribution required)
- `agent-ashton-west.jpg`, `agent-william-patterson.jpg`, `agent-mckala-bracci.jpg`, `agent-jeff-gorsuch.jpg` — client's own headshots from covercincy.com/insuranceagents

Still hotlinked from client's Webflow CDN (re-upload to HubSpot File Manager at build time):

- Logo (round badge): `https://cdn.prod.website-files.com/66312bd2817edca74846e0b4/663cdd6e630974f7c335ea5f_CoverCincy%20(1).png`
- BBB A+ seal: `https://cdn.prod.website-files.com/66312bd2817edca74846e0b4/6aa32988ebc7e09d5bc9d1e3_logo.bbb.png`
- USABG 1988 badge: `https://cdn.prod.website-files.com/66312bd2817edca74846e0b4/6aa32989155a2f3aa52f5092_static-logos-usabg-badge-1988.png`

## Open items (ask client)

1. Brand video MP4 + .vtt captions.
2. 2–3 testimonial videos + client names/neighborhoods (with permission).
3. Confirm landing page should book into the `u11` round-robin link — or create a **new, separate** meeting link with minimal fields (don't edit `u11`; the live /book page uses it).
4. OK to include a Privacy Policy link in footer? (Recommended for paid social ads.)
5. HubSpot plan level (user providing).
6. Confirm OK to feature Ashton, William, McKala and Jeff's photos on an ad landing page.
