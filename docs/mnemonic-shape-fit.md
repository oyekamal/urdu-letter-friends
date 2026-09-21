# Which word to teach with each letter: sound + shape fit

Kamal's rule after seeing Meem/Noon v1 (2026-09-21): the word must pass two tests, not one.

1. **Sound test** (research 01 §5): the word starts with the letter's sound. Non-negotiable.
2. **Shape test** (Kamal's duck): the object's *natural* silhouette already looks like the letter. If the animator has to bend the object to fit, the child sees a bent object, not a letter. The duck passes because a floating duck is a bowl with a head; nothing was forced.

Score = shape fit (★ weak … ★★★ the object simply is the letter). Kid-familiarity noted where it matters (Pakistani 3-year-old).

## Wave 1

| Letter | Shape to match | Candidates (sound ✓) | Shape fit | Recommend |
|---|---|---|---|---|
| ا alif | one tall straight stroke | انگلی ungli finger · انار anaar pomegranate · اونٹ oont camel | finger ★★★ · pomegranate ★ · camel ★ | **انگلی finger pointing up** (shipped) |
| ب be | shallow bowl, one dot below | بطخ batakh duck · بلی billi cat · بکری bakri goat | duck ★★★ (Kamal) · cat ★ · goat ★ | **بطخ duck** (shipped, Kamal's) |
| ت te | shallow bowl, two dots above | تتلی titli butterfly · تربوز tarbooz watermelon · تالا tala lock | two butterflies over a slice of watermelon? watermelon slice = bowl ★★★, butterflies = dots ★★★ | **تربوز slice as the bowl + two تتلی as dots** — replaces the leaf (پتّا fails sound test anyway). Spoken word: titli; the slice is scenery. Or watermelon alone with two seeds as dots (تربوز, ★★★, one word). |
| م meem | round loop top-right, long tail slanting down-left | مور mor peacock · مچھلی fish · مرغی murghi hen · مکڑی makri spider | peacock ★★★ (round body, long trailing tail) · fish ★ (v1, rejected) · hen ★★ · spider ★ | **مور peacock**: body = loop, hanging tail = the stroke, head tuft at top |
| ن noon | deep bowl, one dot above | ناؤ nao boat · نان naan · نارنگی orange · نل nal tap | boat ★★★ (a boat IS a bowl) · naan ★ · orange ★ (v1, rejected) · tap ★ | **ناؤ boat**, dot = the sun above it or a bird. Spoken: nao |
| ک kaaf | long slanted stroke, bowl at bottom, short bar on top | کیلا kela banana · کنگھی kanghi comb · کچھوا kachhua turtle · کبوتر kabootar pigeon | banana ★★ (the curve) · comb ★ · turtle ★ · pigeon ★ | **کیلا banana** lying in the bowl, its stem as the top bar. Needs a sketch before committing |
| ل laam | tall stroke hooking into a bowl, like a J | لاٹھی laathi cane · لومڑی lomri fox · لالٹین lantern · لڈو laddu | cane ★★★ (a J) · fox ★★ (tail curl as the hook) · lantern ★ · laddu ★ | **لاٹھی cane** (dada's stick, with a face), or **لومڑی fox** if a cane feels dull to kids. Kamal picks |
| د daal | small rounded bracket opening left | دیا diya lamp · دم dum tail · دانت daant tooth · دروازہ door | diya ★★ (bowl on its side with a flame) · tail ★★ · tooth ★ · door ★ | **دیا diya**: the clay bowl is the curve, the flame sits at the top tip |

## What this changes

- Retire `meem-machhli.json` and `noon-narangi.json` to `lotties/legacy/` once Kamal confirms the replacements (peacock, boat).
- Tay: decide between watermelon slice + butterflies (two ideas in one frame) and watermelon with seeds (one idea). Research 01 says one idea per screen for 3-year-olds, so the single-word version is the safer bet.
- Add a `shape_fit` field to `lotties/manifest.json` (1–3) so a weak fit is visible before anyone animates it.
- Update the letter-character skill gate: no drawing until both tests are recorded.

## Still to score (waves 2–4)

پ patang kite (★★★, a kite is a bowl with a tail, three dots = three bows on the string) · ٹ tamatar/ٹوپی topi cap (a cap is a bowl!) · س سانپ snake (★★★, the teeth of س) · ر رسی rope · و وہیل whale? · ہ ہاتھی elephant · ی یاک? … to be done with Kamal in the same table before any generator is written.
