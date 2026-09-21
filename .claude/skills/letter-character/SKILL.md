---
name: letter-character
description: Build or revise one Urdu letter character Lottie for the kids app (an animal/object whose body IS the letter, with idle + tap segments), using scripts/harf_rig.py, then verify frames in lottie-web and update the manifest + review page. Use for "make the Pay character", "new letter lottie", "fix the duck's tap", "add ج".
---

# Letter Character

One Lottie per letter. The character's body is the letter shape; the dots are part of the character. Generated in code so a fix is a number and a re-run.

## Before drawing (pedagogy gate — read research/ first, do not skip)
1. Pick the mnemonic word from `research/02_orenda_taleemabad_practice.md` (table of traditional + improved words). The word must START WITH THE LETTER'S SOUND, not its name, and be something a 3-year-old in Pakistan knows.
2. The letter shape stays faithful: bowl depth, dot count and dot POSITION (above/below) exactly as the letter. A child must be able to see ت in the picture at a glance (test: shrink the frame-0 render to 64 px; still recognisable?).
3. Dots stay dots in the resting pose. They may become creatures (butterflies) but must settle back to dot positions in `idle`.
4. One tap = one reaction + the letter sound. No menus, no text, no timers, no lives. Rules in `research/03_kids_app_design_and_interactivity.md`.

5. **No fake dots.** Two round eyes on a ب body reads as ت. One eye, eyes off the stroke, or lid-shaped eyes; never a round mark on or near a stroke that is not a real dot (research 01 §5).
6. **Check the word before drawing, and record it** in `lotties/manifest.json` under `mnemonic_check` (passes / fails + why). The worm for Alif failed this (کیڑا); do not repeat it.
7. Read `docs/app-plan.md` §4 for how the character feeds the lesson (sound → name → word on tap, trace path = body stroke).

8. **Shape test before sound test is even worth running**: the object must ALREADY look like the letter (Kamal's duck rule). Score 1–3 in `docs/mnemonic-shape-fit.md`; only a 3 (or a 2 with Kamal's ok) gets drawn. Meem-fish and Noon-orange were 1s and got rejected.

## Build
```bash
cp scripts/make_tay.py scripts/make_<id>.py     # copy the closest existing generator
python3 scripts/make_<id>.py                     # writes lotties/<file>.json (must print size < 60 KB)
python3 scripts/render_frames.py <file> 8        # review/frames/<file>.png — LOOK at it
python3 scripts/build_review.py                  # after adding the letter to lotties/manifest.json
```
Canvas: `WIDE` (600x420) for bowl letters, `TALL` (420x680) for ا ل ک. Markers: `idle` 0–90, `tap` 90–180 at 30 fps (`harf_rig.export` writes them).

## Motion rules (from the lottie-motion skill; numbers, not vibes)
- Idle → anticipation → action → overshoot → settle → idle. Rest ≥ 40% of the loop.
- Idle: 1–4 px bob, one cycle per 3 s; sway ≤ 3°; blink 100/50/100 ms at frames 40 and 170 (`blink()`).
- Tap: anticipation 10–15% opposite direction, overshoot 5–10%, one settle bounce, back to the exact idle pose by frame 165 so the segment boundary is seamless.
- Secondary action (sparkles, ripple) lags primary by 3 frames (`sparkle_burst`).
- Easing `STD` everywhere; `HOLD` for show/hide; linear only for spins.

## python-lottie gotchas (these have all bitten)
- First shape in a group renders ON TOP. Pass shapes top → bottom.
- One Fill/Stroke per group; it styles everything above it.
- Same-frame keyframes are REPLACED silently: `keys()` asserts strictly increasing frames.
- One-keyframe animated property renders nothing in lottie-web: use a static value.
- Keep everything inside the canvas at every frame (the first Tay flight left the canvas).
- Filled shapes only, round caps, no gradients/masks/images/expressions (low-end Android).

## Verify (mandatory before "done")
1. `render_frames.py` contact sheet: letter recognisable at f0, nothing clipped, tap returns to idle pose.
2. Open `review/index.html` (or the GitHub Pages URL) and watch at 1x; tap it 5 times fast — no glitch, no stuck state.
3. File < 60 KB, one layer, markers present: `python3 -c "import json;d=json.load(open('lotties/<file>.json'));print(len(d['layers']),d['markers'])"`.
4. Add the row to `lotties/manifest.json` with `status: review`; Kamal moves it to `approved`.
