# Draws the app icons: a white question mark on green, in the same flat style as the checklist app's icon.
from PIL import Image, ImageDraw
import math, os
here = os.path.dirname(os.path.abspath(__file__))
S = 2048
img = Image.new('RGB', (S, S), '#138a4a')
d = ImageDraw.Draw(img)
w = S * 0.11                                  # stroke width
cx, cy, r = S * 0.5, S * 0.36, S * 0.155       # hook of the question mark
pts = []
for i in range(0, 221):                       # arc from the left (180°) over the top to lower right (400°)
    t = math.radians(180 + i)
    pts.append((cx + r * math.cos(t), cy + r * math.sin(t)))
p0 = pts[-1]
c = (cx, cy + r * 1.05)                       # curve from the arc's end into the stem
p2 = (cx, cy + r * 1.55)
for i in range(1, 101):
    u = i / 100
    pts.append(((1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * c[0] + u * u * p2[0],
                (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * c[1] + u * u * p2[1]))
for i in range(1, 41):                        # short straight stem
    pts.append((cx, p2[1] + (S * 0.06) * i / 40))
for x, y in pts:                              # stamp round brushes along the path: round caps and joins
    d.ellipse([x - w / 2, y - w / 2, x + w / 2, y + w / 2], fill='white')
dr = w * 0.6
dy = pts[-1][1] + S * 0.155
d.ellipse([cx - dr, dy - dr, cx + dr, dy + dr], fill='white')
for n in (512, 180):
    img.resize((n, n), Image.LANCZOS).save(os.path.join(here, '..', f'icon-{n}.png'), optimize=True)
print('ok')
