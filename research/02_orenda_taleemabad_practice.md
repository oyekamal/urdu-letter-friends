# 02 — How Orenda/Taleemabad teach early years, and what Pakistan officially expects

*Research note for urdu-letter-friends. Written 2026-09-21. Sources are the Orenda private skills repo (pedagogy/brand content only, no credentials), the public `rumi-platform` repo, and the official/secondary documents cited inline. Anything I could not open first-hand is marked **[unverified]**.*

---

## 1. What Orenda / Taleemabad actually do

### 1.1 The two products and two brands

| | **Taleemabad** (company + Smart Learning Program) | **Rumi** (teacher companion) |
|---|---|---|
| Audience | Children K-5 and their schools/government | Teachers, on WhatsApp |
| What it is | "digitized the national curriculum into engaging, accessible content … interactive games and educational cartoons", "1.5 million registered users" (taleemabad.com/home). The Learning App: "Our localized characters take conventional learning material like writing, phonics, vocabulary, spelling, rhyming, basic maths, and counting, and bring them to life" — with an explicit **Urdu Alif–Yay strand** (writing, identification, vocabulary, spelling, phonics) and a cartoon cast (e.g. "Pinky") ([App Store listing](https://apps.apple.com/pk/app/taleemabad-learning-app/id1573435969)). UNESCO's GEM 2022 report describes it as "cartoon-based mobile phone applications to teach the national curriculum" ([unesdoc](https://unesdoc.unesco.org/ark:/48223/pf0000383550), snippet only). | Open-source WhatsApp assistant: lesson plans, reading assessments, coaching, quizzes, voice, 9 languages ([github.com/Orenda-Project/rumi-platform](https://github.com/Orenda-Project/rumi-platform)). |
| Brand | Blue `#3860C1` / Green `#17C65D` / Yellow `#EFAF22`; Fredoka + Poppins; Baloo Bhaijaan 2 for Urdu H1; Noto Nastaliq Urdu body; **Teemu** the green parrot; 3D "Higher Perspective" icons | Navy `#001F3F` + one warm accent (gold `#F5B301` decks / coral `#F06E42` product); SF Pro/Inter; the dots-and-smile mark; "Apple-restrained, the product is the hero" |

Sources: `agent-skills-taleemabad/skills/taleemabad-brand/SKILL.md` and `reference/{color-tokens,typography,mascot-and-iconography}.md`; `skills/rumi-brand/SKILL.md`. A Taleemabad ECE lead's LinkedIn mentions setting "the early years curriculum for (Play group, Nursery and Kindergarten)" for Taleemabad Schools **[unverified — search snippet only]**.

The brand skills are emphatic that the two are **different brands, never blended**, and the Rumi skill says its old hand-drawn illustration style is "deprecated". Neither brand has a documented child-facing letter-character style; Teemu is the only child-facing character in the brand book.

### 1.2 Lesson shape

- **Rumi's generated lesson plans** use a nine-part 5E structure: objectives & success criteria → overview → materials → Engage → Explore → Explain → Elaborate (guided practice) → Evaluate (formative) → differentiation (`rumi-platform/docs/features/lesson-plans.md`).
- **The curriculum-baked LP corpus** (the skill that produced ~2,000 government-textbook-faithful lessons) adds the rules that matter for us:
  - *Every* lesson opens with a **2–6 min cumulative spaced-retrieval warm-up** of *prior* lessons, then a **hook that does not teach** ("Openings hook; they do not teach"), then gradual release (I do → We do → You do), a 3-part check-for-understanding, an exit task. (`curriculum-baked-lesson-plans/reference/research/enrichment-elements.md`, `reference/render-laws.md` law 12)
  - **Urdu-specific spine** (same file, "Urdu — the same science, two script-specific twists"): `arkaan_saazi` = *print-free phonemic awareness → grapheme with all 4 positional forms → dot-discrimination drill → aeraab → blend pointed syllables*, plus a **daily ~5-min automaticity flash**. Rationale quoted: "Many graphemes differ only by dots … RAN [rapid automatised naming] is the strongest predictor of Urdu reading fluency."
  - The **~9 non-joiners (ا د ڈ ذ ر ڑ ز ژ و)** "have no left half-form and break the chain" — teach *with* joining, not separately.
  - Aeraab present and explicitly taught in G1–3, faded by frequency later. (For ages 3–6 this means: isolated letters and pointed CV syllables only.)
- **Rumi's reading assessment** treats "Letters (KG)" as its lowest level and scores **letters correct per minute** against DIBELS-derived norms; Urdu KG spring median = 36 LCPM, but the Urdu rows are explicitly "L2 adjusted – 30% lower" from English norms, i.e. not Urdu-normed (`rumi-platform/docs/flows/reading-assessment-flow-v2.json`; `bot/database/migrations/010_add_lcpm_benchmarks.sql`). Useful as a ceiling target, not a standard.

### 1.3 "Do not" rules for children's material (from the production skills)

1. **Nastaliq throughout, never Naskh** for Urdu — "if you cannot match Nastaliq, leave the space blank rather than render Naskh"; the shapes row uses **tatweel** to show positional forms because that is what the child's textbook prints (`render-laws.md` §1a–1c).
2. **Never letter-space Nastaliq**; `line-height ≈ 2`, `word-spacing .15em` (`taleemabad-brand/reference/typography.md`).
3. **Urdu numerals ۰۱۲۳۴۵۶۷۸۹**, never Arabic-Indic ٠١٢٣ (`pedagogical-worksheet-imagegen/SKILL.md`).
4. **Gender-neutral register**, corpus-wide ("Never استانی صاحبہ or anything gender-locked") (`render-laws.md` §6).
5. **Brand-neutral naming inside content** — story characters, places and signage never carry the company or product name (`render-laws.md` §13).
6. **Phone-first type**: Urdu-medium body ≥3.4% of page height; "if a section will not fit, the card grows and the illustration shrinks — never the words" (§5).
7. **Never render a language translated into itself**; one register per line (§1d).
8. Honorifics are never dropped (ﷺ, ؓ) where a name appears (worksheet skill rule 23e).
9. Taleemabad UX copy: sentence case, imperative verbs, British spelling, no icons in buttons, icon-only targets ≥48 px (`editorial-and-ux-writing.md`).
10. Colour: `#E94E5A` red is **error only**; never white text on yellow; secondary colours ≤40% of a design (`color-tokens.md`).

---

## 2. What Pakistan officially expects (ages 3–5)

### 2.1 National Curriculum for ECCE 2017 (federal; the Punjab 2017 text is near-identical)

Scope: "pre-schoolers (age 04-05 years)", with a footnote that the framework "has the scope to expand and pre-primary grade for age 03-04 years can also be derived", noting SDG-4 points to two years (03–05). Six key learning areas; Language & Literacy competencies (pp. 19–27 of the PDF at [pafec.org](https://www.pafec.org/wp-content/uploads/2019/01/ECCE-22-09-17.pdf)):

- C1 (listening/speaking) g. "**Recognition of letters with their initial sounds**"; h. differentiate sounds in the environment; teachers "use phonic rhymes and sounds in audio/video form. Children will learn the rhyme and will identify letters with their initial sounds."
- C3 c. "Appreciate the concept of words rhymes and syllables."
- C5 c. "**Know that Urdu is read from right to left**", d. English left to right.
- C6 d. "Begin to recognise letters of the Alphabet"; f. "**Identify letter sounds through words that have personal meaning**"; g. "**Associate initial letter sounds with names of objects in their classroom environment**"; h. "Think of a variety of objects beginning with a single letter of the alphabet."
- C7 (writing) a. "Make marks and scribble", c. "Hold a pencil correctly", e–f. trace/copy shapes and "vertical, horizontal and wavy lines and simple patterns", g. "**Trace copy and write the letter of Urdu alphabet**", i. write own name in Urdu and English.

The pedagogical stance is explicit: "Learning to read and write the Alphabet … is just one component … **Over emphasis on this component especially through rote memorization … cripples not only their language development, but also their cognitive capacities**" (p. 8 area), and "It is the process and not the production of the learning that is more important at this stage!" (§2.2).

### 2.2 SNC ECCE 2020 (Grade Pre-I, age 4–5)

ITA's line-by-line comparison shows the SNC "follows up on the same competencies and ELOs" as 2017 and often matches Punjab 2017 "word-for-word"; a one- **or** two-year programme is allowed but two years is not mandated ([ITA, 2020](https://itacec.org/document/2021/8/ECCE_in_Single_National_Curriculum.pdf), pp. 2, 9–10). The SNC Pre-I text itself (mirror: [Slideshare](https://www.slideshare.net/slideshow/sncecce-preipdf/253165504); official PDF at mofept.gov.pk, TLS error at time of writing) keeps the same seven literacy competencies and adds "making new words through **blending sounds**" (C1 l), "Recognise their names in print (Urdu & English)", and "Trace, copy and write the letter of Urdu alphabet" / English / regional language. **No letter order or letter subset is specified anywhere** — only "letters of the Alphabet".

ITA's literacy reviewer (Aliya Hashim) criticised exactly what our app must not repeat: "recognition of letters and sounds … has taken precedence over the oral blending and segmenting skills … **The teaching of letters visually through flashcards is best reserved till after the oral sound skills are secure**", the curriculum "misses … phonemic awareness development", and recommends "Systematic, Synthetic Phonics … a clear progression of sounds" (ITA annex pp. 1–3).

### 2.3 National Curriculum of Pakistan 2022–23, ECE progression grid (3–4 vs 4–5)

The NCP replaced the SNC label and — for the first time federally — splits ECE SLOs into **3–4 and 4–5 year columns**. From search-indexed snippets of the grid ([Scribd](https://www.scribd.com/document/885161510/1-NCP-ECE-PG), [ncc.gov.pk SLO PDF](https://ncc.gov.pk/SiteImage/Misc/files/(link)+SNC+-+Early+Childhood+Education+(ECE)+-+Required+Standards+and+SLOs.pdf)) **[partially verified — PDFs blocked from this sandbox]**:

- 3–4: "Recognize the letters and their sounds"; **4–5** `ECE-00-B3b-01`: "**Recognise and name letters of the languages being taught (graphemes) and know the most common sound that each letter represents**".
- `ECE-00-B3b-04`: "Identify objects/words which have the same sound in the beginning, middle and end"; also "Recognize sounds (phonemes)", "sound of digraphs within words", "Read consonant-vowel-consonant (CVC) words" (4–5, presumably English).
- `ECE-00-B4-0x`: 3–4 "Trace letters of the language/s being taught" → 4–5 "Trace, copy and write the letters of the [languages being taught]".

Net: **Nursery (3–4)** = oral sound play, recognise some letters and their sounds, tracing strokes; **KG/Prep (4–5)** = name *and* sound of each letter, initial-sound matching, trace/copy/write letters, write own name. Sindh's 2018 curriculum has had the two-band split since 2018 (ITA p. 2).

---

## 3. Common Pakistani KG practice and the mnemonic tradition

**Practice.** Public-sector teachers "follow the alphabetical approach … they first teach them the names of the letters", then spell words aloud ("jor": آم = "alif mud aa meem sakin"); "students … don't know the sounds of the letters … **Letter names in Urdu have to do little in reading**" ([Zulfiqar Ali, 2024](https://www.linkedin.com/pulse/why-do-children-pakistans-public-sector-schools-learn-zulfiqar-ali-lcwjf)). The Pakistan Reading Project (USAID) built its Urdu materials on "the frequency of letters/syllables and words" with letter-sound flash cards and syllable charts ([pakreading.org.pk](https://pakreading.org.pk/en/resources/publications/reading-learning-material)) — the frequency-based alternative to alif-bay-pay order. Private schools still overwhelmingly introduce letters one per day in alphabet order with a tracing sheet each (e.g. [Shamim School Playgroup worksheets](https://www.shamimschool.com/urdu-alphabets-alif-bay-pay-اردو-حروف-تہجی-printable-worksheets-for-class-playgroup/), 37–38 letters).

**Name vs sound.** Urdu letter names (بے، پے، تے …) are the consonant plus /e/, so the chant *does* carry the sound, unlike English "double-u". The real problems are different: (a) **alif** carries no consonant, so "الف سے انار" teaches a vowel-carrier as if it were /a/ and collides with آم; (b) **ڑ ں ھ ء ے never begin a word**, so every "X se Y" for them is a position mismatch; (c) **homophone sets** — ت/ط, ث/س/ص, ز/ذ/ض/ظ, ح/ہ, (ق/ک in casual speech), ع/ا — have one sound each, so for those letters the word is a *spelling* mnemonic, not phonics; (d) many traditional words are Arabic loans no 4-year-old says.

**Traditional word per letter** (a widely used qaida list, from [aiocrafters/Urdu-Qaida-Complete-Workbook](https://github.com/aiocrafters/Urdu-Qaida-Complete-Workbook); alternates in brackets are common chant variants from my own knowledge of the "Alif se Anar" rhyme tradition — **verify before shipping**):

| # | Letter | Name | Traditional word | Flag |
|---|---|---|---|---|
| 1 | ا | alif | انار anar (pomegranate) | vowel carrier, not a consonant sound; teach as "the tall line that starts a-/i-/u-" |
| 2 | ب | be | بکری bakri (goat) [بطخ batakh duck] | ok — duck already chosen |
| 3 | پ | pe | پتنگ patang (kite) [پنکھا pankha] | ok |
| 4 | ت | te | تتلی titli (butterfly) [تختی takhti] | ok — butterfly matches project |
| 5 | ٹ | ṭe | ٹماٹر ṭamaṭar (tomato) [ٹوکری ṭokri] | ok; retroflex, contrast with ت |
| 6 | ث | se | ثواب sawab (reward) [ثمر samar] | abstract/Arabic; homophone of س |
| 7 | ج | jeem | جہاز jahaz (plane) | ok |
| 8 | چ | che | چڑیا chiṛya (sparrow) [چھتری chhatri] | ok |
| 9 | ح | baṛi he | حلوہ halwa [حقہ **hukka**] | hukka = smoking pipe, not kid-friendly; homophone of ہ |
| 10 | خ | khe | خرگوش khargosh (rabbit) | ok |
| 11 | د | daal | درخت darakht (tree) [دروازہ] | ok |
| 12 | ڈ | ḍaal | ڈبہ ḍabba (box) [ڈھول ḍhol] | ok |
| 13 | ذ | zaal | ذرا zara (a little) [ذخیرہ] | not imageable; homophone of ز |
| 14 | ر | re | رنگ rang (colour) [ریل rail, رسی] | ok |
| 15 | ڑ | ṛe | گاڑی gaṛi / پہاڑ pahaṛ | **never word-initial** — medial/final only |
| 16 | ز | ze | زمین zameen [زینہ, زیبرا] | ok-ish; زیبرا more imageable |
| 17 | ژ | zhe | ژالہ zhala (hail) | rare letter, rare word |
| 18 | س | seen | سیب seb (apple) | ok |
| 19 | ش | sheen | شیر sher (lion) | ok |
| 20 | ص | suad | صابن sabun (soap) | ok; homophone of س |
| 21 | ض | zuad | ضیافت ziyafat [ضرب zarb] | abstract; homophone of ز |
| 22 | ط | toe | طوطا tota (parrot) | ok; homophone of ت |
| 23 | ظ | zoe | ظرف zarf (vessel) [ظلم **zulm**] | zulm = oppression; both weak |
| 24 | ع | ain | عینک ainak (glasses) | ok; sound ≈ vowel onset |
| 25 | غ | ghain | غبارہ ghubara (balloon) | ok |
| 26 | ف | fe | فوارہ fawwara (fountain) | ok |
| 27 | ق | qaaf | قلم qalam (pen) | ok |
| 28 | ک | kaaf | کتاب kitab (book) [کبوتر kabootar] | ok |
| 29 | گ | gaaf | گلاب gulab (rose) [گائے gaye] | ok |
| 30 | ل | laam | لیموں lemon [لالٹین] | ok |
| 31 | م | meem | مچھلی machhli (fish) [مور] | ok |
| 32 | ن | noon | نارنگی narangi [نان] | ok |
| 33 | ں | noon ghunna | — | never initial; teach as nasal "tail" (ماں) |
| 34 | و | wao | ورزش warzish (exercise) | abstract; vowel/consonant dual role |
| 35 | ہ | choṭi he | ہاتھی hathi (elephant) | ok |
| 36 | ھ | do-chashmi he | — | never initial; aspiration marker (بھ، پھ) |
| 37 | ء | hamza | — | no word |
| 38 | ی | ye | یاقوت yaqoot (ruby) [یکہ yakka] | both obscure |
| 39 | ے | baṛi ye | — | never initial |

Count note: qaidas print 37–40 letters depending on whether آ, ں, ھ, ء, ے are counted ([Wikipedia](https://en.wikipedia.org/wiki/Urdu_alphabet)); Rumi's code assumes 38.

---

## 4. Recommendations for urdu-letter-friends

1. **Two orders, one data model.** Keep the canonical alif→ye order as the browse view (that is what SNC/NCP, every qaida, and Taleemabad's "Alif–Yay" strand use, so parents and teachers expect it), but make the **learning path** a sound-first order:
   - *Wave 1 (Nursery, ship first):* ب ت ن م ک ل د ا — high-frequency, one sound each, no homophone yet, three of the project's characters already here. Alif comes last in the wave, framed as the "helper" for a/i/u.
   - *Wave 2:* پ ٹ س ر و ہ ی ے (retroflex/aspiration contrasts, the vowel letters).
   - *Wave 3:* ج چ خ گ ش ز ف ق غ ع.
   - *Wave 4 (KG/Prep, "cousins"):* ث ح ذ ڈ ڑ ژ ص ض ط ظ ں ھ ء — introduced as **dot/shape cousins of a known sound** ("same sound as س, different dress"), which is exactly the dot-discrimination drill the Taleemabad corpus prescribes and avoids pretending these have new sounds.
2. **Teach sound, show name.** Character says the *sound* first ("bə…"), the letter name appears as a label; every screen has an initial-sound picture match (NC 2017 C6 g / NCP B3b-04). Meet ITA's critique by putting 2–3 oral-only "hear the sound" taps *before* the letter animates in.
3. **Mnemonic words:** keep the good traditional ones (khargosh, sher, seb, tota, ghubara, hathi, machhli, jahaz); replace hukka, zulm, sawab, zara, ziyafat, warzish, yaqoot/yakka with imageable child words; for ڑ ں ھ ے ء show the letter *inside* a word (گاڑی, ماں, ہاتھی's ھ) and say so — never fake an initial.
4. **Per-letter loop mirroring the Taleemabad LP spine:** 30-second retrieval of 2 previous letters → hook (character enters, no teaching) → sound → letter with its 4 positional forms as a "dress-up" beat → dot drill → trace (strokes first, then letter; NC 2017 C7 e–g) → 5-minute mixed flash for automaticity. Log letters-correct-per-minute so a Rumi-style KG letter assessment can read it.
5. **Typography/rendering:** Noto Nastaliq Urdu (bold) for the letters; positional forms via tatweel; never letter-space; `line-height 2`; Urdu numerals only; RTL layout with LTR grids as in the brand skills.
6. **Visual style:** this is an open-source personal repo, so stay **brand-neutral** (render-law 13) — do not ship Teemu, the ت-nuqta mark, or the dots-and-smile. If Kamal later wants a Taleemabad-compatible look, borrow the *system*, not the marks: Fredoka/Baloo Bhaijaan 2 + Nastaliq, blue-anchor/green-resolve/yellow-initiate colour story, soft 3D-ish rounded shapes, gold stars for reward. Rumi's navy-restraint is for teachers, not 3-year-olds.
7. **Avoid:** rote chant-throughs of all 38 letters; aeraab on isolated letters; Arabic-Indic digits; gendered teacher register; red anywhere except errors; Naskh fallback fonts; any claim that ث/س/ص "sound different".

*Open gaps:* the NCP 2022–23 grid PDFs and the SNC ECCE PDF could not be downloaded from this machine (TLS/403) — quotes for §2.3 come from indexed snippets and should be re-checked against the ncc.gov.pk file before we cite them in the README.
