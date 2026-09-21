"""ا Alif = ungli (انگلی, finger). A finger pointing up IS the tall stroke of Alif.
idle 0-90: gentle sway from the base + tiny bob; blink at 40.
tap 90-180: anticipation lean, three "ek! ek!" wags, overshoot, settle; sparkle at the fingertip."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from harf_rig import *

SKIN = (242, 181, 138); SKIN_D = (214, 140, 100); NAIL = (255, 214, 200); GOLD = (255, 196, 60)
anim, layer = animation("Alif ungli", TALL)
CX, TOP, BOT, HW = 210, 110, 610, 48          # centre x, top y, base y, half width

body = group("finger", path([((CX, TOP + HW), (0, 0), (0, -HW * 0.55)), ((CX, TOP + HW), (0, 0), (0, 0)), ((CX, BOT), (0, 0), (0, 0))]), stroke(SKIN, HW * 2))
nail = group("nail", ellipse(CX, TOP + HW * 0.95, HW * 0.62, HW * 0.78), fill(NAIL))
knuckles = group("knuckles", path([((CX - 22, 330), (0, 0), (8, 6)), ((CX + 22, 330), (-8, 6), (0, 0))]),
                 path([((CX - 22, 470), (0, 0), (8, 6)), ((CX + 22, 470), (-8, 6), (0, 0))]), stroke(SKIN_D, 5))
face_g, eye_w, pupils = face(CX - 12, 250, r=13, blush_dx=26, blush_dy=22,
                              smile=[((CX - 16, 292), (0, 0), (8, 10)), ((CX + 18, 290), (-8, 10), (0, 0))])
eye2 = group("eye2", ellipse(CX + 20, 250, 8, 8), fill(WHITE), anchor=(CX + 20, 250)); pup2 = group("pupil2", ellipse(CX + 22, 252, 3.5, 3.5), fill(INK))
whole = group("alif", face_g, pup2, eye2, nail, knuckles, body, anchor=(CX, BOT))

sway(whole.transform.rotation, ((0, 0), (45, 1.8), (90, 0),
                                (94, 4), (102, -12), (112, 12), (122, -10), (132, 8), (142, -4), (152, 2), (162, -0.6), (170, 0), (180, 0)))
bob(whole.transform.position, CX, BOT, amp=3)
look(pupils + [pup2], ((0, (0, 0)), (90, (0, 0)), (102, (-4, -3)), (112, (4, -3)), (122, (-3, -2)), (140, (0, 0)), (180, (0, 0))))
blink(eye_w, pupils); blink(eye2, [pup2])

for g in (sparkle_burst(CX, TOP + 10, GOLD, at=TAP[0] + 6, rx=60, ry=45), whole): layer.add_shape(g)
out = os.path.join(os.path.dirname(__file__), "..", "lotties", "alif-ungli.json")
print("alif-ungli.json", export(anim, out), "bytes")
