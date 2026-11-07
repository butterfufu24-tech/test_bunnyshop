# BUNNY SHOP

An English-language, editorial storefront for **BUNNY SHOP** — small-batch stoneware, glass
and linen from twelve workshops in Thailand. Dark edition: near-black ink, warm-white type,
and an iridescent accent kept to hairlines, underlines and one serif price mark.

The whole site is **one self-contained HTML file** — seven fonts and nine photographs embedded
as data URIs. No network requests, no dependencies, no build step needed to view it.

![Hero](docs/preview-hero.jpg)

## Live site

`index.html` at the repo root is the deployable page. To publish it:

1. Push this repo to GitHub.
2. **Settings → Pages → Source: Deploy from a branch → `main` / `root`.**
3. It goes live at `https://<user>.github.io/<repo>/`.

There is also a ready-made Action in `.github/workflows/pages.yml` if you prefer
**Settings → Pages → Source: GitHub Actions** instead.

Locally, any static server works:

```bash
python3 -m http.server 8000     # → http://localhost:8000
```

## Contents

| Path | What it is |
| --- | --- |
| `index.html` | **The deliverable.** Open it anywhere, offline. |
| `v3/src/01-head.html` | Design system: tokens, type scale, header, hero, sections, cards, seconds tile, studio, notes, gift sets, FAQ, signup, footer, bag drawer, keyframes, reduced motion |
| `v3/src/02-body.html` | Markup: hero → statement → collection → seconds tile → studio → quote bleed → notes → gift sets → questions → signup → footer + drawer |
| `v3/src/03-js.html` | Vanilla JS, no dependencies |
| `v3/fonts/` | Bricolage Grotesque 300/500, Instrument Serif roman + italic, Inter Tight 300/400/500 — latin subsets (7 woff2) |
| `v3/opt/` | Graded WebP photography used in the build (9 files) |
| `v3/raw/` | Source imagery, straight from generation |
| `v3/build3.py` | Inlines fonts + images into `index.html` |
| `v1/`, `v2/` | Earlier editions (v1 Thai, v2 Swiss light) — kept for reference, each with its own build script |
| `qa/` | Playwright + axe scripts used to sign the build off |

## Build

```bash
python3 v3/build3.py     # writes index.html at the repo root
```

`build3.py` base64-embeds every font and image into `{{TOKEN}}` slots and **aborts** if any
token is left unresolved, so a broken asset path fails loudly instead of shipping a page with
`{{IMG_HERO}}` in the markup. V3 build is byte-reproducible.

## Design notes

- **Ink, not black.** `#08080A` base, three raised surfaces (`#0E0E12`, `#16161C`, `#20202A`),
  hairlines at 8.5% and 16% white, plus a `.055` film-grain overlay so flat fields never read
  as dead pixels.
- **Type as structure.** Bricolage Grotesque at display sizes (hero to 120 px), Instrument
  Serif italic for the one emotive phrase and the pull quotes, Inter Tight for reading, mono
  labels for indices and metadata.
- **One light source.** A soft beam crosses the headline; three faint radial glows sit behind
  the hero. It should read as a lamp in a dark room — nothing else in the page glows.
- **Iridescence at the edge only.** `--ir1`–`--ir5` (sky, lilac, pink, sand, mint) appear on
  1 px rules, the free-shipping bar, the "most given" badge and the `−40%` mark. Never as a fill.
- **Photography.** Dim tungsten side-light, one object on raw slate, deep shadow to the right.
- **Motion.** 14 px rise + fade reveals on a stagger, curtain wipe for media, 0.6 s
  `cubic-bezier(.16,1,.3,1)`. Everything collapses under `prefers-reduced-motion`.

![Collection](docs/preview-collection.jpg)

## What works

- Sticky header that picks up blur + border past the fold, scroll-spy with `aria-current`.
- Category filter chips — filtering reflows to a 3-up grid, hides the seconds tile, and
  announces the count in a live region.
- Bag: add from any card or set, quantity, remove, empty state, subtotal / shipping / total,
  free shipping over $120, persists in `localStorage` (`bunnyshop_v3_bag`). Drawer with scrim,
  `Esc`, focus trap and scroll lock.
- Gift sets: one-off ↔ circle member toggle swaps all three prices ($96/$148/$210 →
  $82/$126/$179) and the add-to-bag prices with them.
- FAQ accordion, newsletter validation, stat counters, mobile menu with `inert` + scroll lock.

## Sign-off

Verified in Chromium via Playwright at 1440 × 900 and 390 × 844:

- **0 axe violations** (WCAG 2.0/2.1 A + AA + best practice, both viewports)
- 48/48 reveals fire, no horizontal overflow, 0 console or page errors
- Bag persists across reloads; drawer opens on button, closes on scrim and `Esc`
- Reduced-motion pass renders every section fully visible with no animation

Re-run it yourself:

```bash
npm i playwright@1.65.0 axe-core && npx playwright install chromium linux
node qa/shoot.js && node qa/axe.js && node qa/behavior.js
```

## Notes

Static demo: checkout, tax handling and the newsletter post are front-end only. Photography
and copy are fictional. Third-party font licences are in [FONTS.md](FONTS.md).
