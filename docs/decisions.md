# Decision log

One line per decision. Open items are Kamal's to close; Kamil proposes, Kamal decides.

| Date | Decision | Status | Why / where |
|---|---|---|---|
| 2026-09-21 | Characters are generated from python-lottie code, not drawn in After Effects | decided | Fix = number + re-run; diffable; the two references were already code-generated (named groups, transform keys) |
| 2026-09-21 | Every character carries `idle` and `tap` Lottie markers; app plays by name | decided | Timing changes never touch app code; `README.md` |
| 2026-09-21 | Two canvases only: 600×420 bowl letters, 420×680 tall letters | proposed | Matches the two references; keeps layout grid simple |
| 2026-09-21 | Dots may be creatures (butterflies) but must rest exactly at dot positions | proposed | Letter readability first; `research/01_early_years_pedagogy.md` |
| 2026-09-21 | Tap reaction length 3 s | proposed | Too long for rapid re-tapping? Test with a child |
| 2026-09-21 | Mnemonic word must start with the letter SOUND, not its name; kid-known object | proposed | `research/02_orenda_taleemabad_practice.md` word table |
| 2026-09-21 | Pilot audio is machine TTS (CC BY-NC); human recording before any release | decided | Licence + every successful literacy app ships human voice |
| 2026-09-21 | First batch letter order | open | Frequency-first (ا ب ک ل م ن, from urdu-reading-course corpus) vs curriculum order (ا ب پ ت …); see research 01/02 |
| 2026-09-21 | App stack (PWA vs Flutter vs React Native) for low-end Android, offline | open | Recommendation in `research/03_kids_app_design_and_interactivity.md` |
| 2026-09-21 | Alif worm mnemonic fails (کیڑا starts with /k/); Alif word = انار, framed as vowel helper | open | research 01 §5, 02 §3; re-theme or keep worm as art with انار spoken |
| 2026-09-21 | Tay: butterflies are the character (تتلی passes), leaf is the perch (پتّا fails) | proposed | research 01 §5 |
| 2026-09-21 | House style for eyes: round eyes near strokes read as extra dots (ب with two eyes reads as ت) | open | research 01 §5; options: one eye, off-stroke, lid-shaped |
| 2026-09-21 | Letter order = sound-first waves for learning, alif→ye for browsing | proposed | research 02 §4.1, docs/app-plan.md §1 |
| 2026-09-21 | Stack = Flutter + dotlottie-flutter, Rive as upgrade path, PWA for review only | proposed | research 03 §3 |
| 2026-09-21 | Marker set grows to idle/tap1/tap2/tap3/sleep/celebrate | proposed | research 03 rule 20 |
| 2026-09-21 | No streaks/timers/lives/coins/notifications/ads/IAP; app ends its own session | decided | research 01 §3, 03 §1 (JAMA 2022: ~80% of preschool apps manipulative) |

