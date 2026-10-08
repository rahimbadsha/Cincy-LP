# Cincy-LP

Conversion-focused landing page for **Cover Cincy**: gets self-employed visitors from paid social to book a free health insurance consultation.

Built as a mobile-first HTML/CSS/JS prototype; it will be converted into a HubSpot template and custom modules once the design is approved.

## Structure

```
landing-page/         Page prototype (index.html, css/, js/, images/)
hubspot/cover-cincy-lp/
  templates/          HubSpot landing page template (HubL)
  modules/            One editable module per section (header, hero, video, reviews, booking, footer, sticky)
  css/, js/           Shared styles and behavior (same as the prototype)
docs/                 Page copy, brand tokens, open items (.md source + browser-viewable .html)
scripts/
  build-docs.py       Rebuild docs/*.html from docs/*.md
  capture.mjs         Full-page high-resolution JPG capture (uses local Google Chrome)
```

## Page sections

1. **Hero**: headline, subhead, primary CTA, trust badges, local broker team
2. **Brand video**: muted autoplay with captions, tap for sound, CTA
3. **Testimonials**: real Google reviews, CTA
4. **Booking**: embedded HubSpot Meetings calendar, phone fallback
5. **Footer**: phone CTA, trust badges, copyright

## Preview locally

```bash
cd landing-page
python3 -m http.server 5500
```

Open http://localhost:5500

## Versions

Each design round is tagged (`v1`, `v2`, …). See all versions:

```bash
git tag -n
```

Open any version: `git checkout v4` (return with `git checkout main`).

## HubSpot build

`hubspot/cover-cincy-lp/` mirrors the `cover-cincy-lp` folder in the HubSpot Design Manager.
Create a landing page from the **Cover Cincy - Booking Landing Page** template; every section is editable in the page editor.
