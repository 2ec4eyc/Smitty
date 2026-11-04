# The 7-Figure Scaling Ecosystem Framework Using AI: GHL pages

Two paste-ready pages, styled to the Smitty Wealth Enterprises logo (navy, crimson, silver, varsity slab type), built from `FUNNEL_COPY___THE_7-FIGURE_SCALING_ECOSYSTEM_FRAMEWORK_USING_AI.docx`.
Each page is ONE file you paste into ONE GoHighLevel **Custom JS/HTML** element. Fonts, styles, backgrounds and animation are all inside the file. No images to upload: your photos and videos load straight from your GHL media links, and the section backgrounds are drawn in code.

| File | Page |
|---|---|
| `landing.html` | Opt-in / registration page |
| `thank-you.html` | Thank-you / confirmation page |

Preview with stand-in boxes for the photos and videos: `preview/landing.html`, `preview/thank-you.html`, or the `preview/shot-*.png` screenshots.

## Setup in GHL
1. Add a section with **padding 0** and no background. (Full width is best, but the block now stretches edge to edge on its own even inside GHL's centered container.)
2. Add a **Custom JS/HTML** element to it and paste the whole file.
3. Replace the placeholders first:
   - `landing.html`: nothing to replace. The "Webinar | Inner Circle" form (O1r9P5gEdhEQzvUvfPgw) is embedded inline. In GHL, set that form's **On submit** to go to the thank-you page.
   - `thank-you.html`: `CALENDAR_LINK` → your add-to-calendar link, `VSL_VIDEO_URL` → the 90-second video's URL.

## What's on the landing page
Red top bar · hero (pre-headline, H1 "Present But Not Present", subheadline, trust ticks) with the form card on the right and an animated "ecosystem" network behind · scrolling stats ticker · the real problem (Kenny photo + body copy) · 7 fascination bullets · for you / NOT for you · proof (5 results, count-up stats, 4 videos) · DM screenshots + Inner Circle photos · FAQ · final CTA (H5 "Google judgment") · footer. A sticky "Save My Free Seat" button appears on phones once the form scrolls away. All buttons jump to the form.

## Copy choices
- Headline: **H1** (the recommended primary). Buttons use all three CTA variations; H5 is the closing headline.
- Added by me (easy to change): section labels and headings ("The real problem", "On this free training, you'll discover…", "Read this before you register", "What's happened for people in this room" heading styling, "Straight from the DMs", "Hear it from them", "Kenny with the Inner Circle"), the form card text, the "Your host" tag, the green "You're registered" strip, the calendar button label, and the footer disclaimer.
- Left out: the VSL script itself (it's the video on the thank-you page), the live-only bonus placeholder, and the upsell page (all placeholders in the doc).

## Assets used
| Where | Asset |
|---|---|
| Problem section photo | Kenny `6ad5013c…png` |
| Video testimonials | the 4 `.mp4` files (1920×1080, shown 2×2 at 16:9) |
| DM screenshots | the 3 testimonial `.png` files |
| Inner Circle gallery | the 3 Inner Circle `.png` files (small portraits, shown uncropped as framed cards) |

The other 6 Kenny photos aren't used yet; swap any `src` to use a different one.

`python3 src/build-preview.py` rebuilds the preview.

`preview/shot-live-landing-*.png` show the updated block running inside the live GHL page with the real photos (videos show blank only because the headless test browser can't play H.264).

## Brand (from the Smitty Wealth Enterprises logo)
| Role | Hex |
|---|---|
| Navy (dark sections, labels) | `#13284A` → `#0B1A30` |
| Crimson (buttons, highlights, stripes) | `#C21D2B`, bright `#EF4B55` on navy |
| Silver (bevels, rails, text accents) | `#D9DCE1` |
| Light sections | `#F3F4F7` / `#ECEEF2` with faint navy stars |

Type: **Alfa Slab One** (headlines, buttons, big numbers), **Poppins** (small labels, card titles), **Inter** (body).

## Scroll motion (landing page)
- Crimson reading-progress bar along the top.
- Hero: the skyline background and the glowing network drift at different speeds (parallax); the hero copy eases up and fades as you scroll past it.
- Two big "word bands" (System ★ Judgment ★ Time back, and Real people ★ Real numbers ★ Real results) whose rows slide opposite ways as you scroll.
- Sections enter in different ways: the photo and "for you" column from the left, the copy and "not for you" column from the right, results and videos zoom in, DM screenshots tip up into place, bullets rise.
- All of it switches off for visitors with reduced motion on, and nothing stays hidden if the script doesn't run.

The hero background is already linked to your GHL Media copy (https://assets.cdn.filesafe.space/BU5M3MidcixGHbnmd1on/media/6aeadc8534f57914737635b5.jpg). `src/hero-bg.html` draws it and `src/render-hero-bg.sh` renders it to `images/hero-bg.jpg`.

## Form card
The hero card first shows Kenny's photo (`6a6bc2ba…png`, the blue suit "SMITTY the goat" shot) with a **Save My Free Seat** button. Clicking it slides the GHL form up over the photo (the photo blurs behind it); the × closes it again. Every other "Save my seat" button on the page (top bar, section buttons, the sticky phone button) scrolls back to the card and opens the form.

## Thank-you page (same design system)
`thank-you.html` now carries the registration page's full stylesheet and motion script, so both pages share the skyline hero, network lines, ticker, word bands, section styles, progress bar, reveal effects and footer. Its hero puts the check-mark burst and "You're In. Your Seat Is Saved." on the left and the 90-second video in a silver-framed card on the right. Below: the 3 next steps, a word band, why show up live, and a closing calendar CTA ("Show up live. Bring a pen. I'll see you there." from the VSL script).
Placeholders: `CALENDAR_LINK` (3 buttons) and `VSL_VIDEO_URL`. The hero background is already linked.
