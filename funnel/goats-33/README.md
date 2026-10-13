# Goat's 33: GoHighLevel funnel (registration + thank-you)

Design follows the go.bizlaunch.io bridge-sale page: white and blush sections with black ones in between, heavy uppercase headlines with a red phrase, red label pills, glowing red buttons, chevron step tabs, a dark bio card and an offer card beside the form.

Preview: open `preview/registration.html` and `preview/thank-you.html`, or look at the `preview/shot-*.png` screenshots.

## 1. Upload Smitty's photo
Upload `images/smitty-hero.jpg` (800×984) to GHL **Media** and copy its URL. In `registration/02-hero.html`, replace `SMITTY_PHOTO_URL` with that URL. In `registration/07-why.html`, replace `SMITTY_WHY_PHOTO_URL` with the URL of the photo you want in the story section (it can be a different photo).

**Hero background:** upload `backgrounds/hero-section.jpg` (1920×1400, soft blush with red and gold glows) and set it on the **hero section** of both pages (Section → Background → Image, **Cover**, position **Top center**, section **full width**). The hero block itself is transparent, so this shows edge to edge. No image? Use the solid color `#FFF5F5`.
Every other block paints its own background, so leave those GHL section backgrounds empty. The waitlist header is transparent too, so it shows whatever you set on its section (white `#FFFFFF` matches the design).

## 2. Paste the global styles (once per page)
**Page Settings → Custom CSS**: paste all of `registration/00-global-styles.css` on **both** pages, replacing any earlier version.

If the page shows plain Times-style fonts, black text on black, or buttons with no red, the global CSS isn't loading. Check it's pasted in Custom CSS, complete, and the page is saved.

## 3. Build the registration page
Set every section and row to **full width, padding 0**. Each "Code" step is a **Custom JS/HTML** element with that file pasted in.

1. **Top bar** → Code `01-top-bar.html` (also loads the fonts and the scroll fade-in)
2. **Hero** (background image `hero-section.jpg`, full width) → Code `02-hero.html`
3. **What you get** → Code `03-what-you-get.html`
4. **Key dates** → Code `04-key-dates.html`
5. **Waitlist** (section background `#FFFFFF`):
   1. Code `05-waitlist-header.html`
   2. A **2-column row** (bottom padding about 80px): left column Code `06-waitlist-offer.html`, right column your **GHL Form**
6. **Why I'm doing this** → Code `07-why.html`
7. **Who it's for** → Code `08-final-cta.html`
8. **Footer** → Code `09-footer.html`

Every button jumps to `#wf-register`, the waitlist header right above the form. Nothing to configure.

## 4. Style the GHL form to match
Fields: **First name** (required), **Email** (required), **Phone** (optional; label it "Phone (optional, for text reminders when doors open)").

| Setting | Value |
|---|---|
| Form background | `#FFFFFF`, border `#ECE4E4`, radius 16px, padding 24px |
| Field background / border | `#FBF8F8` / `#E3D6D7`, radius 10px, height 52px |
| Label / text | `#111111`, font Inter |
| Button text | `I'm In For 33 →` |
| Button | `#F0001C` (hover `#C20017`), white text, font Poppins 800, uppercase, radius 10px, full width |
| On submit | Go to the thank-you page and trigger the workflow that emails the free 3-report credit check |

## 5. Build the thank-you page
Same Custom CSS as above, full width, padding 0.

1. **Top bar** → Code `thank-you/01-top-bar.html`
2. **You're in** (background image `hero-section.jpg`) → Code `thank-you/02-confirmed.html` (green "You're registered" strip + hero)
3. **What happens next** → Code `thank-you/03-next-steps.html`
4. **Perks locked in** → Code `thank-you/04-perks-locked.html`
5. **Footer** → Code `registration/09-footer.html` (same footer)

The calendar buttons save an all-day event for **Monday, Oct 19** (doors open): Google Calendar opens in a new tab, "Apple / Outlook" downloads an `.ics` file. No time is set because the doors-open time isn't decided yet.

## Brand
| Role | Hex |
|---|---|
| Red (buttons, highlights, top bar) | `#F0001C` |
| Deep red (hover) | `#C20017` |
| Black sections / dark cards | `#0B0B0B` / `#161616` |
| Blush / grey sections | `#FFF4F4` / `#F5F5F5` |
| Text | `#111111`, muted `#5E5E5E` |
| Green ticks | `#16A34A` |

Fonts: **Poppins** 800–900 (headlines, buttons), **Inter** (body). Smitty's signature is an inline SVG traced from Allura, so it needs no font.

## Copy I added
Everything else is your copy word for word. These short lines are mine and easy to change:
- Hero labels "🎂 Birthday month" and "33 moves · 33 days · $330"; photo tag "Smitty · just turned 33"; note under the button; the four green ticks
- Section labels and headlines: "In 33 days, you'll…", "Mark your calendar", "Get on the list before doors open", "Real talk. I learned it the hard way.", "Tired of guessing about credit? Let's get you fundable."
- Card eyebrows (Credit / Business / Funding), the "33 days. One move a day." callout, the offer card's "For my birthday month only" and price line, the bio chips
- All thank-you page copy

## Rebuilding the preview
`python3 src/build-preview.py` stitches the blocks into `preview/`.
