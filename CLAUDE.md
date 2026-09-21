# Urdu Letter Friends — agent notes

Interactive Lottie letter characters for a kids (3–6) Urdu alphabet app. Read `README.md`, then `research/` before touching any character: the point of this repo is to NOT ship slop that fails children.

- New or changed character → invoke `.claude/skills/letter-character/SKILL.md`. It is the contract (pedagogy gate, rig, motion numbers, verification).
- Never edit `lotties/*.json` by hand; edit `scripts/make_<id>.py` and re-run. Exception: `alif-worm.json` and `ba-duck.json` are Kamal's originals with no generator yet.
- `lotties/manifest.json` is the single source of truth for the review page and (later) the app. `python3 scripts/build_review.py` after changing it.
- Verify with `scripts/render_frames.py` (lottie-web in headless Chrome, the renderer the app uses). Stills are not enough for rhythm: also open `review/index.html`.
- Audio is a pilot machine voice (CC BY-NC). Do not present it as release-ready.
- Commit with a conventional message; no `git add -A`.
