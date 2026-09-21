"""harf_rig — shared python-lottie helpers for Urdu letter characters (harf = letter).

Every character is ONE shape layer, flat vector, white ground, no images, no masks, no expressions.
Every character has two Lottie markers: `idle` (a 3 s loop) and `tap` (a 3 s reaction that returns to the
idle pose), so the app drives it with lottie-web `playSegments` by marker name. See README and
.claude/skills/letter-character/SKILL.md for the contract and the pedagogy rules behind it.
"""
import io, json, math, os
from lottie import objects
from lottie.objects import easing
from lottie.nvector import NVector as V
from lottie.exporters.core import export_lottie

FPS = 30
IDLE = (0, 90)      # 3 s loop
TAP = (90, 180)     # 3 s reaction
WIDE = (600, 420)   # horizontal letters (ب ت پ ...)
TALL = (420, 680)   # tall letters (ا ل ک ...)

STD = easing.Bezier(V(0.4, 0), V(0.2, 1))   # Material standard
DEC = easing.Bezier(V(0, 0), V(0.2, 1))     # decelerate (entering)
ACC = easing.Bezier(V(0.4, 0), V(1, 1))     # accelerate (exiting)
HOLD = easing.Hold()

INK = (41, 26, 36); WHITE = (255, 255, 255); BLUSH = (255, 120, 140)

def col(rgb):
    r, g, b = rgb
    return objects.Color(r / 255, g / 255, b / 255)

def animation(name, size, frames=TAP[1]):
    a = objects.Animation(frames, FPS); a.width, a.height = size; a.name = name
    layer = objects.ShapeLayer(); layer.name = name; layer.in_point = 0; layer.out_point = frames
    a.add_layer(layer)
    return a, layer

def fill(rgb): return objects.Fill(col(rgb))

def stroke(rgb, w):
    s = objects.Stroke(col(rgb), w); s.line_cap = objects.LineCap.Round; s.line_join = objects.LineJoin.Round
    return s

def ellipse(cx, cy, rx, ry):
    e = objects.Ellipse(); e.position.value = V(cx, cy); e.size.value = V(rx * 2, ry * 2); return e

def path(points, closed=False):
    """points: [(pos, in_tangent, out_tangent)], tangents relative to pos."""
    b = objects.Bezier(); b.closed = closed
    for p, i, o in points: b.add_point(V(*p), V(*i), V(*o))
    sh = objects.Path(); sh.shape.value = b; return sh

def group(name, *shapes, anchor=None):
    """Shapes render FIRST-ON-TOP inside a group; pass them top -> bottom.
    A Fill/Stroke styles every shape above it: keep one style per group."""
    g = objects.Group(); g.name = name
    for s in shapes: g.add_shape(s)
    if anchor: g.transform.anchor_point.value = V(*anchor); g.transform.position.value = V(*anchor)
    return g

def keys(prop, pairs, ease=STD):
    """pairs: [(frame, value)] with strictly increasing frames (python-lottie REPLACES same-frame keys)."""
    last = -1
    for f, v in pairs:
        assert f > last, f"non-increasing keyframe {f}"
        last = f
        prop.add_keyframe(f, V(*v) if isinstance(v, (tuple, list)) else v, ease)

# ---------- reusable behaviours ----------
def bob(prop, x, y, amp=4, start=IDLE[0], end=IDLE[1], phase=0.0, step=15):
    """Sinusoidal idle bob, one cycle per loop, ends where it started."""
    keys(prop, [(f, (x, y + amp * math.sin(2 * math.pi * (f - start) / (end - start) + phase))) for f in range(start, end + 1, step)])

def sway(rot_prop, pairs=((0, 0), (45, 2.2), (90, 0))):
    keys(rot_prop, list(pairs))

def blink(eye_white_group, pupil_groups, at=(40, 170)):
    """100 ms close / 50 hold / 100 open. Eye white squashes to a dash; pupils hide via opacity holds."""
    pairs = [(0, (100, 100))]
    for f0 in at: pairs += [(f0, (100, 100)), (f0 + 3, (100, 8)), (f0 + 4, (100, 8)), (f0 + 7, (100, 100))]
    keys(eye_white_group.transform.scale, pairs)
    for g in pupil_groups:
        o = g.transform.opacity; o.add_keyframe(0, 100, HOLD)
        for f0 in at: o.add_keyframe(f0 + 2, 0, HOLD); o.add_keyframe(f0 + 6, 100, HOLD)

def look(pupil_groups, pairs):
    """Pupil offset keyframes: [(frame,(dx,dy))]."""
    for g in pupil_groups: keys(g.transform.position, list(pairs))

def face(cx, cy, r=16, blush_dx=22, blush_dy=34, smile=None, ink=INK):
    """Googly eye + blush + smile, matching alif-worm / ba-duck. Returns (face_group, eye_white, [pupil, glint])."""
    eye_w = group("eyeWhite", ellipse(cx, cy, r, r), fill(WHITE), anchor=(cx, cy))
    pupil = group("pupil", ellipse(cx + 3, cy + 2, r * 0.44, r * 0.44), fill(ink))
    glint = group("glint", ellipse(cx + 6, cy - 2, r * 0.16, r * 0.16), fill(WHITE))
    bl = group("blush", ellipse(cx + blush_dx, cy + blush_dy, 9, 5.5), fill(BLUSH))
    parts = [glint, pupil, eye_w, bl]
    if smile: parts.append(group("smile", path(smile), stroke(ink, 5)))
    return group("face", *parts), eye_w, [pupil, glint]

def sparkle_burst(cx, cy, rgb, at=TAP[0] + 3, n=6, rx=70, ry=55):
    """Secondary action: n dots fly out and fade. Hidden (opacity 0, HOLD) outside the burst."""
    g = objects.Group(); g.name = "sparkles"
    for i in range(n):
        a = i * 2 * math.pi / n
        sp = group(f"spark{i}", ellipse(0, 0, 5, 5), fill(rgb))
        p, o = sp.transform.position, sp.transform.opacity
        p.add_keyframe(0, V(cx, cy), HOLD); p.add_keyframe(at, V(cx, cy), STD); p.add_keyframe(at + 17, V(cx + rx * math.cos(a), cy + ry * math.sin(a)), STD)
        o.add_keyframe(0, 0, HOLD); o.add_keyframe(at, 100, STD); o.add_keyframe(at + 17, 0, HOLD)
        g.add_shape(sp)
    return g

def export(anim, out_path, markers=({"cm": "idle", "tm": IDLE[0], "dr": IDLE[1] - IDLE[0]}, {"cm": "tap", "tm": TAP[0], "dr": TAP[1] - TAP[0]})):
    buf = io.StringIO(); export_lottie(anim, buf); d = json.loads(buf.getvalue())
    d["markers"] = list(markers)
    with open(out_path, "w") as fh: json.dump(d, fh, separators=(",", ":"))
    return os.path.getsize(out_path)

if __name__ == "__main__":
    a, layer = animation("check", WIDE)
    f, ew, pups = face(100, 100); blink(ew, pups); layer.add_shape(f)
    p = "/tmp/harf_rig_check.json"; export(a, p); d = json.load(open(p))
    assert [m["cm"] for m in d["markers"]] == ["idle", "tap"] and d["layers"][0]["shapes"], "rig broken"
    print("harf_rig ok")
