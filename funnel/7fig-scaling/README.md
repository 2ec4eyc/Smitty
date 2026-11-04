# The 7-Figure Scaling Ecosystem Framework Using AI: GHL pages

Two paste-ready pages built from `FUNNEL_COPY___THE_7-FIGURE_SCALING_ECOSYSTEM_FRAMEWORK_USING_AI.docx`.
Each page is ONE file you paste into ONE GoHighLevel **Custom JS/HTML** element. Fonts, styles, backgrounds and animation are all inside the file. No images to upload: your photos and videos load straight from your GHL media links, and the section backgrounds are drawn in code.

| File | Page |
|---|---|
| `landing.html` | Opt-in / registration page |
| `thank-you.html` | Thank-you / confirmation page |

Preview with stand-in boxes for the photos and videos: `preview/landing.html`, `preview/thank-you.html`, or the `preview/shot-*.png` screenshots.

## Setup in GHL
1. Add a section, set it to **full width** with **padding 0** and no background.
2. Add a **Custom JS/HTML** element to it and paste the whole file.
3. Replace the placeholders first:
   - `landing.html`: `GHL_FORM_EMBED` → your form's embed code (Sites → Forms → your form → Integrate → Embed). Set the form's **On submit** to go to the thank-you page.
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
| Video testimonials | the 4 `.mp4` files |
| DM screenshots | the 3 testimonial `.png` files |
| Inner Circle gallery | the 3 Inner Circle `.png` files |

The other 6 Kenny photos aren't used yet; swap any `src` to use a different one.

`python3 src/build-preview.py` rebuilds the preview.
