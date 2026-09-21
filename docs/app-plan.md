# Urdu Letter Friends — how the app teaches, looks, hooks, and how the characters fit

This is the synthesis of the three research files in `research/`. Every rule here points back to a cited section there. If a rule and a character disagree, the rule wins until Kamal changes the rule in `docs/decisions.md`.

- `research/01_early_years_pedagogy.md` — how 3–6 year olds learn letters, Urdu script specifics, game-based-learning evidence, app benchmarks, character rules
- `research/02_orenda_taleemabad_practice.md` — how Orenda/Taleemabad teach Urdu early years, Pakistan ECE curriculum outcomes, the 39-letter mnemonic word table, ship order
- `research/03_kids_app_design_and_interactivity.md` — engagement without manipulation, benchmark apps, Lottie/dotLottie/Rive tech, low-end Android, safety, 25 checkable rules

---

## 1. How the app teaches (the pedagogy spine)

**What we are teaching.** Pakistan's ECE curriculum (NC ECCE 2017, SNC 2020, NCP 2022–23) asks a 3–5 year old to: recognise letters with their initial sounds, identify letter sounds through words that have personal meaning, know Urdu reads right to left, and trace, copy and write the letters. It explicitly warns that rote alphabet drilling "cripples" development. (02 §2)

**Sound first, name shown.** Letter-sound knowledge predicts reading; letter names in Urdu "have to do little in reading". Urdu names already embed the sound (be, pe, te), so the character says the *sound* first, then the name, then the word: "b… bay… batakh". The name appears as a label in Nastaliq. (01 §1, 02 §3)

**Embedded picture mnemonics work only if the picture's name starts with the letter's sound.** Ehri 1984, Shmidman & Ehri 2010 (Hebrew), Roberts & Sadler 2018 (d = 1.31). This is the single strongest lever we have and the easiest to get wrong. (01 §1, §5)

**Per-letter lesson loop** (mirrors the Taleemabad lesson-plan spine, 02 §1.2, §4.4), 3–5 minutes, one new letter per lesson, up to three lessons a day, every letter revisited at least three times:

1. Retrieval, 30 s: two already-learned characters appear; child taps the one that says the sound they hear.
2. Hook, no teaching: the new character enters and does something funny. That is all.
3. Sound: the character says its sound three times on three taps, then its name.
4. Letter reveal: the character settles into the letter pose; the Nastaliq glyph fades in over it so the child sees they are the same shape.
5. Word: the mnemonic word is spoken and the object shown (this is where the character's identity pays off).
6. Dots and dress-up: dots highlighted and counted; the four positional forms shown as the character "dressing up" (isolated, initial, medial, final).
7. Trace: body stroke first, dots last, right to left, partial strokes accepted, always ends in success (Sesame 3-step scaffold: encourage → hint → guided path).
8. Automaticity flash, 60 s: mixed letters so far, letters-correct-per-minute logged locally.
9. Natural stop: character waves and yawns, "phir milenge", static home board, no prompt to continue.

**Contrast sets, not isolation.** ب ت ن ی (and later پ ٹ ث) are taught together with dot-discrimination drills, because dot confusions do not fade on their own. Homophone "cousins" (ث/س/ص, ز/ذ/ض/ظ, ت/ط, ح/ہ) come last, framed as "same sound, different dress"; never pretend they have new sounds. (01 §2, 02 §4.1)

**Letter order.** Two orders, one data model. Browse view = canonical alif→ye (what parents, teachers and every qaida expect). Learning path = sound-first waves:

| Wave | Letters | Why |
|---|---|---|
| 1 (Nursery, ship first) | ب ت ن م ک ل د ا | highest frequency, one clean sound each, no homophones; Alif last as the "helper" for a/i/u |
| 2 | پ ٹ س ر و ہ ی ے | retroflex/aspiration contrasts, vowel letters |
| 3 | ج چ خ گ ش ز ف ق غ ع | remaining consonants |
| 4 (KG/Prep, cousins) | ث ح ذ ڈ ڑ ژ ص ض ط ظ ں ھ ء | dot/shape cousins of known sounds; ڑ ں ھ ء ے never start a word, so show them *inside* a word (گاڑی, ماں, ہاتھی) and say so |

**Characters only where they help.** Characters appear on the letter and trace screens. Word and sentence screens use plain glyphs, because mnemonics hurt whole-word learning. (01 §5)

---

## 2. How the app looks for a 3–6 year old

- **Landscape, one screen, no scrolling.** Everything tappable visible at once; if a strip must scroll it scrolls horizontally. (03 rule 22)
- **No text in the child path.** Icons plus spoken labels. Sentences exist only on the parent screen. (03 rule 4)
- **Tap targets ≥ 2 cm (≥ 75 px at 160 dpi), ≥ 8 mm apart, nothing tappable in the bottom 12%.** Children mis-tap 23% of first taps vs 17% for adults and produce almost all "holdover" taps. Register on touch-down, not release. (03 §1, rule 1, 3)
- **Home board** = all letters of the current wave as resting characters, none locked or greyed, one consistent "tappable" glow colour. Tapping a character is the lesson entry. (03 rule 8, 16)
- **Letter screen** = the character large and centred on a white ground (the Lottie canvas), the Nastaliq glyph label, a sound button, a trace button. Nothing else.
- **Colour** never carries meaning alone; palette derived from Okabe–Ito so it survives colour-blindness; red only for errors, never decoration. (03 rule 16, 02 §1.3)
- **Type**: Noto Nastaliq Urdu bold for letters, never Naskh fallback, never letter-spaced, line-height ≥ 2.2, Urdu numerals ۰۱۲ only. Letters inside animations are vector shapes, not live text (Android Nastaliq clipping). (02 §1.3, 03 rule 18)
- **Voice**: one real child-directed Urdu speaker for all 38 letters, interruptible. The current TTS clips are pilot-only. (03 rule 24)
- **Brand-neutral**: no Teemu, no Taleemabad ت-mark, no Rumi dots-and-smile. If a Taleemabad-compatible look is wanted later, borrow the system (Fredoka/Baloo Bhaijaan 2 + Nastaliq, blue/green/yellow story), not the marks. (02 §4.6)

---

## 3. "Addictive enough" without manipulation

Meyer et al. (JAMA Network Open 2022) found manipulative design in about 80% of 133 preschool apps, worse in those used by lower-income children. The goal is a game a child *wants* to open, built from healthy hooks only. (03 §1)

| Healthy hook we use | Dark pattern we refuse |
|---|---|
| Characters with personality and an authored 3-step reaction sequence (tap1 → tap2 → tap3 → rest) | Random reward schedules, loot, coins |
| Cause-and-effect toys: every tap does something within 100 ms | Autoplay, idle attract loops, "watch this" |
| A completable, non-expiring collection of letter friends that rewards *doing* (hear, tap, trace) | Streaks, daily bonuses, timers, lives, "come back tomorrow" |
| The app ends the session itself every 3–8 min; character waves and yawns | Characters begging, crying or guilting at exit |
| Free choice: every letter reachable, nothing locked | Locked/greyed content, progress walls |
| One hint glow after 6–8 s idle, character models the action after 20 s | Auto-advance, nagging |
| Parent co-play card per letter ("find a ب thing in the house") | Notifications, ads, external links, in-app purchases |

Session shape: 3–8 minutes, a natural stopping point each lesson, up to three a day. Research on joint media engagement says learning transfers when a parent plays too, so the parent screen exists to enable co-play, not to sell. (01 §3, 03 rule 12, 23)

---

## 4. How the characters relate to all of this

The character is not decoration on top of the lesson. It *is* the mnemonic, the tap target, the sound source and the trace guide. So the character contract is the pedagogy made concrete:

1. **The picture is the letter.** The character's silhouette overlays the Naskh/Nastaliq glyph; a picture *next to* a letter does not produce the embedded-mnemonic effect. Test: frame-0 still at 64 px reads as the letter. (01 §5)
2. **Dots are exact.** Right count, right position (above/below), body colour, visible in every frame. Dots may become creatures (Tay's butterflies) but rest at the dot positions in `idle`. (01 §5)
3. **No fake dots.** Two round eyes on a ب body reads as ت. Faces must not add dot-like marks on or near letter strokes; one eye, or eyes off the stroke, or lid-shaped eyes. (01 §5) **This affects our current style and needs Kamal's call.**
4. **The word starts with the letter's sound.** Check before drawing, from the table in 02 §3. Current status:
   - ب duck: بطخ batakh, passes.
   - ت butterflies: تتلی titli, passes; the leaf (پتّا) does not, so the butterflies are the character and the leaf is their perch. Consider making the butterflies larger and the leaf quieter.
   - ا worm: کیڑا starts with /k/, fails. Alif's traditional word is انار anaar (pomegranate). Alif is a vowel carrier, not a consonant sound, so the honest framing is "the tall line that starts a-/i-/u-". Proposal: keep the worm's charm as a pomegranate-branch or re-theme; Kamal decides.
5. **Same state set for every letter** so the engine treats all 38 identically. Today: `idle`, `tap`. Target (03 rule 20): `idle`, `tap1`, `tap2`, `tap3`, `sleep`, `celebrate`. `harf_rig.export` will grow markers; the app reads them by name from `lotties/manifest.json`.
6. **Motion carries meaning**: anticipation, action, overshoot, settle, then rest ≥ 40% of the loop; a continuous wiggle reads as noise to a child and to a parent. Reaction ≤ 2 s of action; the current 3 s `tap` segment is at the upper bound and includes the settle. (01 §5, lottie-motion skill)
7. **Sound on every tap**: sound → name → word on the first tap of a session, sound alone afterwards; audio within 100 ms, animation within one frame. (03 rule 1, 2)
8. **Trace path comes from the same geometry**: the body stroke of the generator (`make_<id>.py`) is the trace path, so the child traces exactly what the character is. Dots traced last.
9. **Performance budget per character**: one layer, ≤ 60 KB, no masks/mattes/blur/images, ≤ 2 instances alive, ≥ 30 fps on a 2 GB Android 11 device. (03 rule 19, 21)

---

## 5. Stack and delivery

Recommendation (03 §3): **Flutter + dotlottie-flutter** (state machines and pointer hit-testing in the file, one codebase, low-end Android friendly), **Rive as the upgrade path** if 60 fps on old devices becomes the blocker (Callstack measured Rive ~60 fps vs Lottie ~17 fps on an old Android), **PWA only as the review/demo surface** (this repo's `review/`). Offline-first: all 38 letters, sounds and words bundled ≤ 25 MB, zero network calls in the child path, minSdk 24–26.

Safety collapses to one path (03 §4): collect nothing, no accounts, no analytics, no ads/IAP/external links; a single parent screen behind an Urdu-numeral reading gate; a privacy policy that says exactly that. That satisfies COPPA 2025, GDPR-K and Google Play Families at once.

Release gate: run the healthy-hooks table above as a checklist and the 25 rules in 03 §5, record the pass in `review/`.

---

## 6. What changes right now because of the research

| Item | Change | Owner |
|---|---|---|
| Alif worm | Mnemonic fails (کیڑا). Decide: re-theme to انار, or keep worm as art with انار as the spoken word | Kamal |
| Tay | Butterflies become the character; leaf is the perch; enlarge butterflies | Kamil, after Kamal's call on dots |
| Eyes | Two round eyes near strokes = fake dots. Decide house style: one eye, off-stroke eyes, or lid-shaped | Kamal |
| Markers | Grow from `idle`/`tap` to `idle`/`tap1`/`tap2`/`tap3`/`sleep`/`celebrate` in `harf_rig.py` | Kamil |
| Wave 1 | Build ن م ک ل د next (ب ت exist), words from the 02 §3 table | Kamil |
| Audio | Record one child-directed Urdu speaker before any child test | Kamal |
| Curriculum PDFs | NCP 2022–23 grid and SNC ECCE PDFs were blocked from download; quotes are from indexed snippets. Re-verify against ncc.gov.pk before citing publicly | Kamil |
