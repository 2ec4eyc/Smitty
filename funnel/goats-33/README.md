# Goat's 33: registration page for GoHighLevel

Preview: open `preview/registration.html` in a browser, or look at `preview/shot-desktop.png` and `preview/shot-mobile.png`.

## 1. Upload the backgrounds
Upload everything in `backgrounds/` to GHL **Media**:

| File | Use on | Size |
|---|---|---|
| `hero-desktop.jpg` | Hero section (desktop) | 1920×2600 (tall so it covers the hero, waitlist header, form and perks) |
| `hero-mobile.jpg` | Hero section (mobile) | 1080×5270 (tall on purpose: the hero is a long section on phones) |
| `light-section.jpg` | "Why I'm doing this" section | 1920×1080 |
| `dark-section.jpg` | "Who it's for" section | 1920×1080 |

In each section: **Section → Background → Image**, size **Cover**, position **Center**. For the hero, set the mobile image in the mobile view if your builder supports a separate mobile background. Otherwise use `hero-desktop.jpg` for both. The balloons and confetti sit along the sides, so the text column stays clear either way.

## 2. Paste the global styles (once)
**Page Settings → Custom CSS**: paste all of `registration/00-global-styles.css`, replacing anything from an earlier version.
It's plain CSS. It loads the fonts and holds the brand colors (`--wf-red` and the rest) and all styling. To change a color later, edit it there once.

If the page shows black text, plain Times-style fonts or buttons with no red, the global CSS isn't loading. Check it's pasted in Custom CSS, complete, and the page is saved.

## 3. Build the page (top to bottom)
For every section and row, set **padding to 0** and **full width**, because the blocks bring their own spacing.
Each "Code" step below means a **Custom JS/HTML** element with that file pasted in.

1. **Section: Top bar** → Code `01-top-bar.html`
2. **Section: Hero** (background `hero-desktop.jpg`), one column, four elements stacked:
   1. Code `02-hero.html`
   2. Code `02b-waitlist-header.html`
   3. **GHL Form element** (your waitlist form, see step 4)
   4. Code `03-waitlist-perks.html`
3. **Section: Why** (background `light-section.jpg`) → Code `04-why.html`
4. **Section: Who it's for** (background `dark-section.jpg`) → Code `05-who-its-for.html`
5. **Section: Footer** → Code `06-footer.html`

The "I'm In For 33 →" button in the top bar and the "Save My Spot →" button jump to the form. They target `#wf-register`, the waitlist header right above the form. Nothing to configure.

## 4. Style the GHL form to match
Fields: **First name** (required), **Email** (required), **Phone** (optional; label it "Phone (optional, for text reminders when doors open)").

| Setting | Value |
|---|---|
| Form background | `#FFFFFF`, corner radius 14px, padding 24px, max width 520px, centered |
| Field background / border | `#FBF8F8` / `#E3D6D7`, radius 10px, height 52px |
| Label / text color | `#121212`, font Inter |
| Button text | `I'm In For 33 →` |
| Button color / hover | `#F0001C` / `#B80018`, text `#FFFFFF`, bold, uppercase, radius 10px, full width |
| On submit | Send them to your thank-you page and trigger the workflow that emails the free 3-report credit check |

## Brand colors (taken from partnerwithsmitty.com/class)
| Role | Hex |
|---|---|
| Gold (birthday accent: headline foil, balloons, confetti) | `#F2B937` |
| Red (buttons, highlights) | `#F0001C` |
| Deep red (hover, accents) | `#B80018` |
| Near-black (dark sections) | `#0A0606` |
| Bars / footer | `#111111` |
| Blush (callouts) | `#FBEFEF` |
| Text on light | `#121212` |

Fonts: **Plus Jakarta Sans** (headlines), **Inter** (body), **Allura** (signature).

## Copy I added
Everything else is your copy word for word. These short lines are mine and are easy to change:
- Hero pill: "Birthday month · 33 days · $330"
- Above the form: "Join the waitlist" / "Phone is optional, for text reminders when doors open."
- Why headline: "Real talk. I learned it the hard way." and the stat row (33 days · 1 move a day · ~20 minutes each)
- Who it's for headline: "Tired of guessing about credit? Let's get you fundable."

## Editing the backgrounds
`src/bg.html` draws them and `src/render-backgrounds.sh` saves them as JPGs. `src/build-preview.py` rebuilds the preview from the block files.

---

# Thank-you page (after they join the waitlist)

Preview: `preview/thank-you.html`, or `preview/shot-thank-you-desktop.png` / `shot-thank-you-mobile.png`.

In GHL, add a new step to the funnel after the registration page and set the waitlist form's **On submit** to go to it.

1. **Page Settings → Custom CSS**: paste the same `registration/00-global-styles.css` (it holds the styles for both pages).
2. Build these sections (padding 0, full width):
   1. **Top bar** (background `#111111`) → Code `thank-you/01-top-bar.html`
   2. **You're in** (background `dark-section.jpg`) → Code `thank-you/02-confirmed.html`
   3. **What happens next** (background `light-section.jpg`) → Code `thank-you/03-next-steps.html`
   4. **Perks locked in** (background `dark-section.jpg`) → Code `thank-you/04-perks-locked.html`
   5. **Footer** (background `#111111`) → Code `registration/06-footer.html` (same footer)

No new images: it reuses the backgrounds you already uploaded.

The "Add To Calendar" buttons save an all-day event for **Monday, Oct 19** (doors open). Google Calendar opens in a new tab; "Apple / Outlook" downloads an `.ics` file. No time is set because the exact doors-open time isn't decided; send it and I'll add it.
