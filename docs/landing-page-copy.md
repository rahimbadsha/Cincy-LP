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

- Eyebrow: Cincinnati's independent health insurance broker **[DRAFT]**
- Headline: **Health insurance help from someone who actually works for you.** **[CLIENT]**
- Subhead: **Local, independent, since 1988. Free consult.** **[CLIENT]**
- Primary CTA: **Book Your Free Consult** → scrolls to booking calendar (`#book`) **[CLIENT]**
- CTA microcopy: Free · 15 minutes · No obligation **[DRAFT]**
- Trust badges: **A+ BBB · Since 1988 · Licensed Nationwide** **[CLIENT]**

Desktop side card ("What happens on your call") **[DRAFT]**:
- Title: Your free 15-minute consult
- We review what you have now (or don't)
- We compare private and Marketplace options side by side
- You get a straight answer — no pressure, no obligation
- Footer line: Built for the self-employed, freelancers & small business owners

---

## Section 2 — Brand Message Video

- Heading: **See what makes us different.** **[CLIENT]**
- Video: muted autoplay, captions on, sound on tap/click **[CLIENT]**
- Sound button label: Tap for sound **[DRAFT]**
- CTA below video: **Book Your Free Consult** **[CLIENT]**
- Video file: **[PLACEHOLDER]** — prototype uses existing YouTube video `gaUNawXf3A8` ("As Seen On Ask the Expert"). Final: MP4 + captions file (.vtt) from client.

---

## Section 3 — Testimonials

- Heading / trust line: **Real Cincinnati families. Real coverage that shows up.** **[CLIENT]**
- Supporting line: Hear it from the people we've helped. **[DRAFT]**
- 2–3 real client testimonial videos **[CLIENT]**
  - Video 1: **[PLACEHOLDER]** — client name, neighborhood, video
  - Video 2: **[PLACEHOLDER]**
  - Video 3: **[PLACEHOLDER]**
- CTA: **Book Your Free Consult** **[CLIENT]**

> Never write fake testimonials or names. Only real client content.

---

## Section 4 — Booking Block (`#book`)

- Heading: Pick a time for your free consult. **[DRAFT]**
- Reassurance: **Free · No obligation · 15 minutes · We work for you, not the insurance carriers.** **[CLIENT]**
- Calendar: HubSpot Meetings embed, full width, minimal fields **[CLIENT]**
  - Prototype link: `https://meetings.hubspot.com/aruhlman/u11?embed=true`
    (the same round-robin link the live /book page uses for Ohio + under-65 health: Ashton, William, Jeff, McKala)
- Phone fallback: Prefer to talk now? Call (513) 800-2255 **[CLIENT]**
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

## Assets (currently hosted on client's Webflow CDN — re-upload to HubSpot File Manager at build time)

- Logo (round badge): `https://cdn.prod.website-files.com/66312bd2817edca74846e0b4/663cdd6e630974f7c335ea5f_CoverCincy%20(1).png`
- BBB A+ seal: `https://cdn.prod.website-files.com/66312bd2817edca74846e0b4/6aa32988ebc7e09d5bc9d1e3_logo.bbb.png`
- USABG 1988 badge: `https://cdn.prod.website-files.com/66312bd2817edca74846e0b4/6aa32989155a2f3aa52f5092_static-logos-usabg-badge-1988.png`

## Open items (ask client)

1. Brand video MP4 + .vtt captions.
2. 2–3 testimonial videos + client names/neighborhoods (with permission).
3. Confirm landing page should book into the `u11` round-robin link — or create a **new, separate** meeting link with minimal fields (don't edit `u11`; the live /book page uses it).
4. OK to include a Privacy Policy link in footer? (Recommended for paid social ads.)
5. HubSpot plan level (user providing).
