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
- Under CTA: Free · 15 minutes · No obligation **[CLIENT]**
- Mobile/tablet: headline + subhead centered · Desktop: left-aligned
- Trust badges: **A+ BBB · Since 1988 · Licensed Nationwide** **[CLIENT]**

Team card (desktop: 2×2 photo grid · mobile: avatar row) **[DRAFT]**:
- Title: Meet your local brokers
- Photos + first names: Ashton, William, McKala, Jeff (real headshots from covercincy.com/insuranceagents)
- Note: One of these licensed brokers will personally take your call.
- ⚠️ Only accurate while the page books into the `u11` round-robin (Ashton West, William Patterson, McKala Bracci, Jeff Gorsuch). Update if the meeting link changes.

Background: dark gradient with soft red glow — same style as the footer (no photo).

---

## Section 2 — Brand Message Video

- Heading: **See what makes us different.** **[CLIENT]** ("different." in red)
- Layout: heading → video → CTA (nothing else, per client brief)
- Video: muted autoplay, captions on, sound on tap/click **[CLIENT]**
- Sound button label: Tap for sound **[DRAFT]**
- CTA below video: **Book Your Free Consult** **[CLIENT]**
- Under CTA: Free · 15 minutes · No obligation **[CLIENT]**
- Video file: **[PLACEHOLDER]** — prototype uses existing YouTube video `gaUNawXf3A8` ("As Seen On Ask the Expert"). Final: MP4 + captions file (.vtt) from client.

---

## Section 3 — Testimonials

- Heading: **Real Cincinnati families. Real coverage that shows up.** **[CLIENT]** ("Real coverage that shows up." in red)
- Subheading: ★★★★★ Rated 4.9 out of 5 from 308 Google reviews — snapshot from covercincy.com Google reviews widget on 2026-09-29; update before launch.
- Cards: real Google reviews from covercincy.com homepage (verbatim; names shortened to first name + last initial):

  1. **Taylor K.** · Helped by Ashton
     "Ashton was super knowledgeable and great! He made getting coverage for our family easier than I thought it would be, thank you!"
  2. **Megan R.** · Helped by McKala (excerpt, "…" marks trimmed text)
     "I'm so grateful for the help and guidance I received from McKala… She helped me find the best plan for my daughter and me, and made what could have been a stressful process feel simple and manageable."
  3. **Brian T.** · Helped by William
     "William Patterson was fantastic, he provided several coverage options and solutions to help my family. I highly recommend calling for any health benefit needs."

- CTA: **Book Your Free Consult** **[CLIENT]**
- Under CTA: Free · 15 minutes · No obligation **[CLIENT]**
- Client testimonial **videos** (from brief): **[PLACEHOLDER]** — can be added above the review cards when ready.

> Never write fake testimonials or names. Only real client content.

---

## Section 4 — Booking Block (`#book`)

- Heading: Pick a time for your free consult. **[DRAFT]** ("free consult." in red)
- Reassurance: **Free · No obligation · 15 minutes · We work for you, not the insurance carriers.** **[CLIENT]**
- Calendar: HubSpot Meetings embed, full width, minimal fields **[CLIENT]**
  - Prototype link: `https://meetings.hubspot.com/aruhlman/u11?embed=true`
    (the same round-robin link the live /book page uses for Ohio + under-65 health: Ashton, William, Jeff, McKala)
- Booking panel (gray frame around calendar) **[DRAFT]**:
  - Steps: 1 Pick a day · 2 Choose a time · 3 Add your details
  - Broker faces + "You'll meet with a **licensed local broker**"
  - Below calendar: Can't find a time that works? Call (513) 800-2255 **[CLIENT]** phone fallback
- Calendar look (navy panel, fonts, 45-min duration, Zoom) is set inside HubSpot, not by our page code.

## Footer (one dark section: phone CTA → trust → fade line → copyright)
- Phone CTA (McKala's photo) **[CLIENT]** phone / **[DRAFT]** wording:
  - Title: Prefer to talk to a real person now?
  - Text: Call our local office and talk with our team.
  - Phone: (513) 800-2255
- Trust: official BBB A+ seal + USA Benefits Group "Established 1988" badge
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
- `cincinnati-skyline-night.jpg` / `-sm.jpg` — Wikimedia Commons, **CC0** (no longer used; kept for option)
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
6. ⚠️ **Duration mismatch:** `u11` link is a **45-min Zoom** meeting; brief says **15 minutes**. Need a new, separate 15-min meeting link for this page (don't edit `u11`) — or change the copy.
7. Confirm OK to feature Ashton, William, McKala and Jeff's photos on an ad landing page.
