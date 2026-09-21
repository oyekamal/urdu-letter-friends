"""ن Noon = narangi (نارنگی, orange). The deep bowl of Noon is an orange-peel bowl; the single dot above
is a small whole orange, and the ORANGE is the character (the word must start with the letter sound).
The bowl has no face: a round eye on the bowl would read as a second dot (research 01 §5).
idle 0-90: orange bobs, bowl rocks gently, orange blinks at 40.
tap 90-180: orange squashes (anticipation), hops high, two bounces on landing, settles at the dot spot; bowl wobbles."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from harf_rig import *

PEEL = (255, 150, 60); PEEL_D = (225, 110, 40); FLESH = (255, 210, 150); LEAF = (90, 180, 100)
anim, layer = animation("Noon narangi", WIDE)
CX, CY = 300, 300                  # bowl centre; noon's bowl is deeper and rounder than ba's

bowl = group("bowl", path([((110, 190), (0, 0), (0, 90)), ((CX, 350), (-110, 0), (110, 0)), ((490, 190), (0, 90), (0, 0))]), stroke(PEEL, 44))
inner = group("inner", path([((150, 215), (0, 0), (0, 60)), ((CX, 316), (-80, 0), (80, 0)), ((450, 215), (0, 60), (0, 0))]), stroke(FLESH, 10))
segs = group("segments", *[path([((CX, 316), (0, 0), (0, 0)), ((CX + dx, 232), (0, 0), (0, 0))]) for dx in (-70, 0, 70)], stroke(PEEL_D, 3))
bowlAll = group("bowlAll", segs, inner, bowl, anchor=(CX, 350))

OX, OY, OR = CX, 120, 42           # the dot: a small orange
peel = group("peel", ellipse(0, 0, OR, OR), fill(PEEL))
navel = group("navel", ellipse(0, 6, 4, 3), fill(PEEL_D))
leaf = group("leaf", path([((4, -OR + 2), (0, 0), (6, -14)), ((22, -OR - 16), (-2, 8), (0, 0)), ((6, -OR - 2), (0, 0), (0, 0))], closed=True), fill(LEAF))
face_g, eye_w, pupils = face(-7, -9, r=10, blush_dx=10, blush_dy=18, smile=[((-12, 14), (0, 0), (5, 7)), ((12, 14), (-5, 7), (0, 0))])
orange = group("orange", face_g, leaf, navel, peel, anchor=(0, 0))
orange.transform.position.value = V(OX, OY)

bob(orange.transform.position, OX, OY, amp=4)
keys(orange.transform.position, [(94, (OX, OY + 10)), (110, (OX, OY - 95)), (126, (OX, OY + 4)), (134, (OX, OY - 30)), (144, (OX, OY + 2)), (150, (OX, OY - 10)), (156, (OX, OY)), (180, (OX, OY))])
keys(orange.transform.scale, [(0, (100, 100)), (90, (100, 100)), (94, (112, 86)), (100, (92, 110)), (126, (110, 90)), (132, (100, 100)), (144, (106, 94)), (150, (100, 100)), (180, (100, 100))])
keys(orange.transform.rotation, [(0, 0), (90, 0), (110, 180), (126, 360), (180, 360)])
keys(bowlAll.transform.rotation, [(0, 0), (45, 1.5), (90, 0), (124, 0), (128, -3), (136, 3), (144, -1.5), (152, 0.6), (160, 0), (180, 0)])
keys(bowlAll.transform.scale, [(0, (100, 100)), (124, (100, 100)), (128, (104, 96)), (136, (98, 102)), (144, (100, 100)), (180, (100, 100))])
blink(eye_w, pupils)

for g in (sparkle_burst(OX, OY - 60, (255, 220, 90), at=108, rx=50, ry=35), orange, bowlAll): layer.add_shape(g)
out = os.path.join(os.path.dirname(__file__), "..", "lotties", "noon-narangi.json")
print("noon-narangi.json", export(anim, out), "bytes")
