"""ت Tay = titli (butterfly). The bowl is a smiling leaf; the two dots are two butterflies.
idle 0-90: leaf sways, butterflies bob + slow flap, blink at 40.
tap 90-180: butterflies dip (anticipation), loop up, return with overshoot + settle; pupil follows; sparkle burst."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from harf_rig import *

GREEN = (94, 190, 110); DGREEN = (50, 140, 80); LGREEN = (180, 235, 170)
W1, W2, W3, W4 = (255, 138, 80), (255, 196, 60), (150, 120, 230), (120, 190, 255)

anim, layer = animation("Tay titli", WIDE)

leaf = group("leaf", path([((120, 200), (0, 0), (10, 60)), ((300, 330), (-90, 0), (90, 0)), ((470, 235), (-20, 60), (10, -30)), ((505, 180), (-10, 15), (0, 0))]), stroke(GREEN, 46))
vein = group("vein", path([((150, 215), (0, 0), (10, 40)), ((300, 300), (-70, 0), (70, 0)), ((450, 235), (-20, 40), (0, 0))]), stroke(LGREEN, 7))
stem = group("stem", path([((505, 180), (0, 0), (10, -20)), ((530, 150), (-10, 5), (0, 0))]), stroke(DGREEN, 14))
face_g, eye_w, pupils = face(128, 190, smile=[((138, 224), (0, 0), (6, 10)), ((170, 226), (-8, 4), (0, 0))])
leafAll = group("leafAll", face_g, stem, vein, leaf, anchor=(300, 300))

def butterfly(name, x, y, c1, c2, phase):
    wl = group("wingL", ellipse(-16, -6, 17, 12), ellipse(-12, 10, 12, 8), fill(c1))
    wr = group("wingR", ellipse(16, -6, 17, 12), ellipse(12, 10, 12, 8), fill(c2))
    spots = group("spots", ellipse(-16, -6, 5, 4), ellipse(16, -6, 5, 4), fill(WHITE))
    body = group("body", path([((0, -14), (0, 0), (0, 8)), ((0, 14), (0, -8), (0, 0))]), stroke(INK, 4))
    ant = group("antennae", path([((0, -14), (0, 0), (-4, -8)), ((-9, -26), (2, 4), (0, 0))]), path([((0, -14), (0, 0), (4, -8)), ((9, -26), (-2, 4), (0, 0))]), stroke(INK, 2))
    for w in (wl, wr):               # flap = scale X; slow at rest, fast in flight
        pairs, f = [], phase
        while f < TAP[1]:
            resting = f < TAP[0] or f >= 165
            period = 14 if resting else 6
            pairs += [(f, (100, 100)), (f + period // 2, (70 if resting else 30, 100))]
            f += period
        pairs.append((TAP[1], (100, 100)))
        keys(w.transform.scale, pairs)
    b = group(name, ant, body, spots, wr, wl); b.transform.scale.value = V(135, 135)
    p = b.transform.position
    bob(p, x, y, amp=4, phase=phase)
    lead = phase * 2
    keys(p, [(90 + lead, (x, y + 10)), (102 + lead, (x - 40, y - 55)), (118 + lead, (x + 55, y - 80)), (134 + lead, (x - 20, y - 40)),
             (150 + lead, (x, y - 8)), (158 + lead, (x, y + 3)), (165 + lead, (x, y)), (180, (x, y))])
    return b

bf1 = butterfly("butterfly1", 255, 150, W1, W2, 0)
bf2 = butterfly("butterfly2", 345, 150, W3, W4, 3)

sway(leafAll.transform.rotation, ((0, 0), (45, 2.2), (90, 0), (96, -3), (120, 3), (150, -1), (165, 0.6), (180, 0)))
look(pupils, ((0, (0, 0)), (90, (0, 0)), (100, (1, -5)), (118, (3, -6)), (140, (0, -3)), (160, (0, 0)), (180, (0, 0))))
blink(eye_w, pupils)

for g in (sparkle_burst(300, 150, W2), bf1, bf2, leafAll): layer.add_shape(g)   # first = on top
out = os.path.join(os.path.dirname(__file__), "..", "lotties", "tay-titli.json")
print("tay-titli.json", export(anim, out), "bytes")
