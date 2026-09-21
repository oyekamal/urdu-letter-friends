# Urdu Letter Friends · حرف دوست

Interactive Lottie characters that teach children aged 3–6 the Urdu alphabet. Each letter is an animal or object whose body **is** the letter: Alif is a worm, Ba is a duck, Tay is a leaf with two butterflies for its dots. Tap a character and it reacts and says its letter. Everything is generated from code, so a fix is a number and a re-run, and every design choice is tied to a cited reason in `research/`.

**Live review page:** https://oyekamal.github.io/urdu-letter-friends/review/ (tap the characters)

## Why this repo exists

Most "alif bay pay" apps are slop: a static picture, a chant, a coin animation. Kamal's rule for this project is that nothing ships that does not demonstrably help a small child learn to read Urdu, and that the app should be something a child *wants* to open, without dark patterns. So the order of work is: research first, contract second, characters third. See [What the research says](#what-the-research-says) and the three files in `research/`.

## What is in the box

| Path | What |
|---|---|
| `lotties/` | The characters (`alif-worm.json`, `ba-duck.json`, `tay-titli.json`) and `manifest.json`, the single source of truth: letter, sound, mnemonic word, canvas, segments, audio, status |
| `scripts/harf_rig.py` | Shared python-lottie rig: canvas sizes, easing, `face()`, `blink()`, `bob()`, `sway()`, `look()`, `sparkle_burst()`, `export()` with `idle`/`tap` markers. Run it to self-check |
| `scripts/make_tay.py` | The first generated character; copy it for the next letter |
| `scripts/render_frames.py` | Renders N frames with lottie-web in headless Chrome to `review/frames/<name>.png`, the same renderer the app will use |
| `scripts/build_review.py` | Builds `review/index.html` from the manifest |
| `review/` | Review page, frame strips, and the Lottie inspector Kamal uses |
| `audio/names/` | Letter-name clips (pilot machine voice from [urdu-reading-course](https://github.com/oyekamal/urdu-reading-course), CC BY-NC; record a human before release) |
| `research/` | Cited research: early-years letter pedagogy, Orenda/Taleemabad practice and Pakistan ECE curriculum, kids-app engagement and Lottie interactivity |
| `docs/` | App plan and the decision log |
| `.claude/skills/letter-character/` | The Claude Code skill that builds a new letter under the contract (pedagogy gate, motion numbers, verification) |

## The character contract

- One shape layer, flat vector, white ground. No images, masks, gradients or expressions, so it runs on 2 GB Android phones.
- Two canvases: 600×420 for bowl letters, 420×680 for tall letters.
- Two Lottie markers at 30 fps: `idle` (frames 0–90, a 3 s loop) and `tap` (frames 90–180, a 3 s reaction that lands back on the idle pose). The app plays by marker name with `playSegments`, so timing can change without touching app code.
- Motion follows the animation numbers in the skill: rest is at least 40% of the loop, every action has anticipation, overshoot and a settle, blinks are 100/50/100 ms.
- The letter stays readable: dot count and dot position are exact, and the frame-0 still must read as the letter at 64 px.
- The mnemonic word starts with the letter's **sound**, not its name, and is a thing a Pakistani three-year-old knows.

## Build a character

```bash
pip install lottie playwright pillow && playwright install chromium   # once
python3 scripts/harf_rig.py            # self-check
python3 scripts/make_tay.py            # -> lotties/tay-titli.json
python3 scripts/render_frames.py tay-titli 8   # -> review/frames/tay-titli.png, look at it
python3 scripts/build_review.py        # -> review/index.html
python3 -m http.server 8000            # open http://localhost:8000/review/ (fetch needs http, not file://)
```

With Claude Code in this repo: "make the Pay character" invokes the `letter-character` skill, which walks the same steps and refuses to skip the pedagogy gate.

## Use in an app

```js
const anim = lottie.loadAnimation({container, renderer: 'svg', loop: true, autoplay: false, animationData});
anim.addEventListener('DOMLoaded', () => anim.playSegments([0, 90], true));          // idle
stage.onclick = () => { sayLetter(); anim.loop = false; anim.playSegments([90, 180], true);
  anim.addEventListener('complete', function once() { anim.removeEventListener('complete', once);
    anim.loop = true; anim.playSegments([0, 90], true); }); };
```

Segment numbers come from `lotties/manifest.json`, never hard-coded.

## What the research says

_Filled from `research/` once the three research passes land; see that folder for the cited versions._

## Status

| Letter | Character | Status |
|---|---|---|
| ا alif | worm | Kamal's reference, 15 s continuous, no markers yet |
| ب be | duck | Kamal's reference, 6 s loop, no markers yet |
| ت te | leaf + butterflies | generated, in review |

Open decisions for Kamal: dots as creatures or plain dots; tap length (3 s); canvas convention; letter order for the first batch. Tracked in `docs/decisions.md`.

## Licence

Code MIT. Character art and animations CC BY 4.0. Pilot audio inherits CC BY-NC from its TTS model.
