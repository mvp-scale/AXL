# AXL Capture (Chrome extension)

Captures a handful of pages of a site you have permission to work on, exactly as your browser shows them, into one zip that AXL opens offline. Nothing is uploaded: pages are staged in this browser until you export them, and exporting clears them.

## Install (developer mode)
1. Open `chrome://extensions` and turn on **Developer mode** (top right).
2. Click **Load unpacked** and choose this folder (`axl/extension`).
3. Pin **AXL Capture** to the toolbar.

## Capture
Open the site, click the AXL Capture icon, then pick a style:

- **Record as I browse** (default): press **Start recording** and open the pages you want. Each page is captured about 1.5 s after it finishes loading: AXL scrolls it once so lazy images load, then shows "AXL saved this page" at the bottom of the page. Press **Stop recording** when done. Easiest, but it captures every page you open (remove extras from the list) and may catch a page before a slow widget has settled.
- **One page at a time**: go to a page, get it looking how you want (close the cookie banner, open the menu or tab you want shown), then press **Capture this page**. Slower, but you control exactly what each copy shows.

The first time, Chrome asks to let AXL read the site (and the servers its images and fonts come from). Access is per site, not "all websites".

Then **Review & export** shows every page, the number of files saved, and anything that could not be saved. **Export zip** saves `axl-capture-<site>-<date>.zip` to Downloads and clears the staged copy.

## What is in the zip
| Path | What |
|---|---|
| `manifest.json` | site, start page, every page (URL, title, viewport, links to other captured pages, notes), saved and missing files |
| `pages/NN-name.html` | each page as rendered, scripts removed; links to other captured pages point at each other, links to pages you did not capture are marked "Not captured" |
| `assets/` | every image, font and style sheet, stored once |
| `thumbs/` | a screenshot of each page as captured |
| `index.html` | open this after unzipping to browse the copy without AXL |

## How faithful is the copy?
Measured with `axl/tools/runners/capture_check.js` (live page vs offline copy, same viewport, offline browser with no network):

| Site | Pages | Desktop | Tablet | Mobile |
|---|---|---|---|---|
| GOV.UK (home, Driving, Organisations) | 3 | 0.0% of pixels differ | 0.0% | 0.0% |
| vercel.com (home, Pricing, Docs) | 3 | 0–0.7% | 0–3.1% | 0–3.9% |

The offline copy made no requests to the live site in any run. Known limits:
- The copy is a still. Carousels, marquees and animations stop where they were; menus stay open or closed as captured.
- Drawings made by script (canvas/WebGL, e.g. vercel.com's 3D hero) are saved as one image at the size they had when captured; a site that redraws them per screen size will look different at other widths. Capture again in a narrow window if that matters.
- Embedded third-party frames (video players, maps) become labelled placeholders.
- Parts built inside web components (shadow DOM) may be missing; the page's notes say so when that happens.

## Test
`cd axl/tools && node runners/capture_check.js <outdir> <start-url> [<more urls>…]` loads the extension, records the URLs, exports the zip and writes the comparison table plus screenshots to `<outdir>`.
