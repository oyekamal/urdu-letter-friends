"""م Meem = machhli (مچھلی, fish). The round head-loop of Meem is the fish's body, the long descending
stroke is its tail. No dots, so the eye sits inside the body with no fake-dot risk.
idle 0-90: fish bobs, tail sways, fin flaps, blink at 40.
tap 90-180: anticipation squash, three quick tail flicks, body wiggle, bubbles rise and pop."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from harf_rig import *

ORANGE = (255, 140, 66); DORANGE = (220, 100, 40); CREAM = (255, 224, 190); BLUE = (120, 190, 255)
anim, layer = animation("Meem machhli", WIDE)
HX, HY, R = 400, 140, 70           # head loop centre + radius (the meem's loop)

# tail = the descending stroke of meem: from the loop's bottom-left down to the far left, round caps
tail = group("tail", path([((HX - 30, HY + 62), (0, 0), (-60, 70)), ((150, 358), (60, -40), (0, 0))]), stroke(ORANGE, 44),
             anchor=(HX - 30, HY + 62))
tailfin = group("tailfin", path([((155, 360), (0, 0), (0, 0)), ((95, 328), (0, 0), (0, 0)), ((112, 368), (0, 0), (0, 0)), ((85, 403), (0, 0), (0, 0))], closed=True), fill(DORANGE),
                anchor=(155, 360))
body = group("body", ellipse(HX, HY, R, R * 0.92), fill(ORANGE))
belly = group("belly", ellipse(HX + 8, HY + 22, R * 0.6, R * 0.35), fill(CREAM))
fin = group("fin", path([((HX + 20, HY + 40), (0, 0), (10, 25)), ((HX + 30, HY + 95), (-5, -8), (0, 0)), ((HX - 5, HY + 58), (0, 0), (0, 0))], closed=True), fill(DORANGE),
            anchor=(HX + 20, HY + 40))
mouth = group("mouth", path([((HX + 62, HY + 8), (0, 0), (6, 6)), ((HX + 72, HY + 2), (0, 0), (0, 0))]), stroke(INK, 4))
face_g, eye_w, pupils = face(HX + 28, HY - 14, r=14, blush_dx=14, blush_dy=30)
fish = group("fish", face_g, mouth, fin, belly, body, tailfin, tail, anchor=(HX, HY))

bob(fish.transform.position, HX, HY, amp=5)
keys(fish.transform.rotation, [(0, 0), (45, -2), (90, 0), (94, 3), (100, -6), (108, 6), (116, -5), (124, 4), (134, -2), (146, 1), (160, 0), (180, 0)])
keys(fish.transform.scale, [(0, (100, 100)), (90, (100, 100)), (95, (92, 108)), (104, (106, 96)), (114, (100, 100)), (180, (100, 100))])
# tail sway: slow at rest, quick flicks on tap
tp = [(0, 0), (22, 6), (45, 0), (68, -6), (90, 0)]
tp += [(96, 14), (102, -14), (108, 14), (114, -12), (120, 8), (128, -4), (138, 2), (150, 0), (180, 0)]
keys(tail.transform.rotation, tp); keys(tailfin.transform.rotation, [(f, v * 1.4) for f, v in tp])
keys(fin.transform.rotation, [(0, 0), (15, 12), (30, 0), (45, 12), (60, 0), (75, 12), (90, 0), (96, 20), (102, 0), (108, 20), (114, 0), (180, 0)])
look(pupils, ((0, (0, 0)), (90, (0, 0)), (100, (3, -3)), (120, (-2, -3)), (140, (0, 0)), (180, (0, 0))))
blink(eye_w, pupils)

# bubbles: three rise from the mouth after the tap and pop (scale to 0), hidden otherwise
bubbles = objects.Group(); bubbles.name = "bubbles"
for i, (dx, delay, size) in enumerate(((0, 0, 9), (14, 6, 6), (-6, 12, 7))):
    b = group(f"bubble{i}", ellipse(0, 0, size, size), stroke(BLUE, 3)); s = TAP[0] + 4 + delay
    keys(b.transform.position, [(0, (HX + 80 + dx, HY)), (s, (HX + 80 + dx, HY)), (s + 24, (HX + 90 + dx * 2, HY - 110))], ease=DEC)
    o = b.transform.opacity; o.add_keyframe(0, 0, HOLD); o.add_keyframe(s, 100, HOLD); o.add_keyframe(s + 24, 0, HOLD)
    keys(b.transform.scale, [(0, (60, 60)), (s, (60, 60)), (s + 24, (110, 110))])
    bubbles.add_shape(b)

for g in (bubbles, fish): layer.add_shape(g)
out = os.path.join(os.path.dirname(__file__), "..", "lotties", "meem-machhli.json")
print("meem-machhli.json", export(anim, out), "bytes")
