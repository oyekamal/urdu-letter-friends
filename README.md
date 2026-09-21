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

Full synthesis with citations: **[`docs/app-plan.md`](docs/app-plan.md)**. The short version:

**How to teach a 3–6 year old a letter** (`research/01`, `research/02`)
- Sound first, name shown. Letter names "have to do little in reading" in Urdu; the character says "b… bay… batakh".
- The picture must *be* the letter, and its name must start with the letter's sound. That is the embedded-mnemonic effect (Ehri 1984; Roberts & Sadler 2018, d = 1.31), the strongest lever we have. It is also why the Alif worm fails (کیڑا starts with /k/) and why Tay's butterflies pass but its leaf does not.
- One new letter per 3–5 minute lesson, up to three a day, each letter revisited three or more times. Look-alikes (ب ت ن ی) are taught as a contrast set with dot drills.
- Pakistan's ECE curriculum wants letters with their initial sounds, meaningful words, right-to-left awareness and tracing, and warns that rote drilling "cripples" development.
- Learning path in sound-first waves (ب ت ن م ک ل د ا first); alif→ye kept only as the browse view.

**How the app should look** (`research/03`)
- Landscape, one screen, no scrolling, no text in the child path, tap targets at least 2 cm, register on touch-down.
- Every letter always reachable, nothing locked. One consistent "tappable" glow. Okabe–Ito palette, red only for errors.
- Nastaliq for live text, vector shapes for letters inside animations, one real Urdu child-directed voice.

**Engaging without manipulating** (`research/01 §3`, `research/03 §1`)
- About 80% of preschool apps use manipulative design (JAMA Network Open 2022). We use characters with personality, instant cause-and-effect, a completable sticker collection and parent co-play. We refuse streaks, timers, lives, coins, random rewards, notifications, ads, in-app purchases and characters that beg at exit. The app ends its own session every 3–8 minutes.

**How the characters carry all of that** (`docs/app-plan.md §4`)
- The character is the mnemonic, the tap target, the sound source and the trace path. Exact dots, no fake dots from round eyes near strokes, same state set for every letter, one layer under 60 KB, 30 fps on a 2 GB Android phone.

## Status

| Letter | Character | Mnemonic check | Status |
|---|---|---|---|
| ا alif | worm | fails (کیڑا); Alif word is انار | Kamal's reference, decision needed |
| ب be | duck | passes (بطخ) | Kamal's reference, no markers yet |
| ت te | leaf + two butterflies | passes via butterflies (تتلی) | generated, in review |

Open decisions for Kamal are in [`docs/decisions.md`](docs/decisions.md): Alif re-theme, eye style (round eyes near strokes read as extra dots), tap length, marker set, stack. Next build: ن م ک ل د to finish wave 1.

## Licence

Code MIT. Character art and animations CC BY 4.0. Pilot audio inherits CC BY-NC from its TTS model.
