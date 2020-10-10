import math


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


def fgcolors(id, cols=6):
    # starts with darker two thirds based on bgcolor
    cor = map(lambda x: (x - 166) * 2, bgcolor(id))

    ns = toints(id, 166)
    ns = ns + ns[:2]
    l = []
    i = 0
    while i < len(id):
        cor = [ini + 10 if ini < fim else ini - 10 for ini, fim in zip(cor, ns[i:i + 3])]

        # mirror value, if outside limits
        cor = [2 * 166 - c if c > 166 else abs(c) for c in cor]

        l.append(cor)
        i += 1

        # new starting color for each row (5+6+6+6 = 23)
        if i % cols > 0:
            cor = ns[i:i + 3]

    return l


def bgcolor(id):
    return [int(round(x + 166)) for x in toints(id[-3:], 83)]


def avatar(id, f="uuid-avatar-$id.jpg", rows=4, font_filename="DejaVuSansMono-Bold.ttf", font_size=48, fontw=31,
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

    back_ground_color = bgcolor(text)

    im = Image.new("RGB", (width, height), tuple(back_ground_color))
    draw = ImageDraw.Draw(im)
    unicode_font = ImageFont.truetype(font_filename, font_size)

    colors = [back_ground_color] + fgcolors(id, cols)

    x = y = margin
    for l, c in zip(text, colors):
        draw.text((x, y), l, font=unicode_font, fill=tuple(c))
        x += fontw
        if x + fontw + margin > width:
            x = margin
            y += fonth

    im.save(f)

# avatar("1PB2C52SP0Ccsqxc8SkrGyF")  # IRIS
