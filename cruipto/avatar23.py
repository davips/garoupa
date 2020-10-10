import math
from statistics import mean

from cruipto.uuid import UUID


def toint(l):
    n = ord(l)
    if n < 58:
        return n - 48
    elif n < 91:
        return n - 55
    else:
        return n - 61


def toints(id, limit):
    s = id + id[0]
    l = []
    i = 0
    while i < len(id):
        r = toint(s[i]) * 62 + toint(s[i + 1])
        l.append(int(round(limit * r / (62.0 * 62))))
        i += 1
    return l


def colors(id, cols=6, incr=10, threshold=127):
    # starts with darker two thirds based on bgcolor
    ns = toints(id, threshold)
    cor = ns[0:3]
    ns = ns + ns[:2]
    l = []
    i = 0
    while i < len(id):
        cor = [ini + incr if ini < fim else ini - incr for ini, fim in zip(cor, ns[i:i + 3])]

        # mirror value, if outside limits
        cor = [2 * threshold - c if c > threshold else abs(c) for c in cor]

        # new starting color for each row (5+6+6+6 = 23)
        if i % cols == cols - 1:
            cor = ns[i:i + 3]

        l.append(cor)
        i += 1
    return [[int(round((255 - threshold) * x / threshold + threshold)) for x in cor]] + l


def avatar(id, f="uuid-avatar-$id.jpg", rows=4, incr=10, threshold=166, font_filename="DejaVuSansMono-Bold.ttf",
           font_size=48,
           fontw=31,
           fonth=57, margin=3):
    """Generate a colorful image from a base62 id containing 23 chars.
    <$id> at the filename will be replaced by the provided id."""
    from PIL import Image, ImageDraw, ImageFont

    cols = math.ceil(len(id) / rows)
    width = cols * fontw + 2 * margin
    height = rows * fonth + 2 * margin

    if "$id" in f:
        f.replace("$id", id)
    text = " " + id
    cs = colors(id, cols, incr, threshold)
    im = Image.new("RGB", (width, height), tuple(cs[0]))
    draw = ImageDraw.Draw(im)
    unicode_font = ImageFont.truetype(font_filename, font_size)

    x = y = margin
    for l, c in zip(text, cs):
        draw.text((x, y), l, font=unicode_font, fill=tuple(c))
        x += fontw
        if x + fontw + margin > width:
            x = margin
            y += fonth

    im.save(f)


# u = UUID(12)
# u *= u
# print(u.id)
# avatar(u.id, incr=18, threshold=170)  # IRIS
