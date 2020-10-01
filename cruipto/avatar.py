from PIL import Image, ImageDraw, ImageFont, ImageFilter

# configuration
width = 158
height = 176
font_size = 48
start_limit = 150
limit = 200
inc = 15
offset = 200


def move(fc, aft):
    r, g, b = fc
    dr = (r + inc) % limit if r < round((limit * ord(aft[0]) / 800)) else (r + limit - inc) % limit
    dg = (g + inc) % limit if g < round((limit * ord(aft[1]) / 800)) else (r + limit - inc) % limit
    db = (b + inc) % limit if b < round((limit * ord(aft[2]) / 800)) else (r + limit - inc) % limit
    return dr, dg, db


def avatar(uuid, f="uuid-avatar-$id.jpg"):
    """Generate a colorful image.

    <$id> at the filename will be replaced by the provided uuid."""
    if "$id" in f:
        f.replace("$id", uuid)
    n = uuid.n
    tt = " " + uuid.id

    res, c1 = divmod(n, 21780986680939)
    res, c2 = divmod(res, 21780986680939)
    _, c3 = divmod(res, 21780986680939)
    b1, b2, b3 = (
        offset + round((255 - offset) * c1 / 21780986680939),
        offset + round((255 - offset) * c2 / 21780986680939),
        offset + round((255 - offset) * c3 / 21780986680939),
    )
    back_ground_color = b1, b2, b3

    im = Image.new("RGB", (width, height), back_ground_color)
    draw = ImageDraw.Draw(im)
    unicode_font = ImageFont.truetype("DejaVuSansMono-Bold.ttf", font_size)

    res, rem = divmod(c1, 27928)
    r = round(start_limit * rem / 27928)
    res, rem = divmod(res, 27928)
    g = round(start_limit * rem / 27928)
    res, rem = divmod(res, 27928)
    b = round(start_limit * rem / 27928)
    font_color = r, g, b
    c = 0
    i = 0
    for l in tt[0:5]:
        draw.text((3 + i, 3), l, font=unicode_font, fill=font_color)
        i += 31
        c += 1
        font_color = move(font_color, tt[c:c + 3])

    res, rem = divmod(c2, 27928)
    r = round(start_limit * rem / 27928)
    res, rem = divmod(res, 27928)
    g = round(start_limit * rem / 27928)
    res, rem = divmod(res, 27928)
    b = round(start_limit * rem / 27928)
    font_color = r, g, b
    c = 0
    i = 0
    for l in tt[5:10]:
        draw.text((3 + i, 61), l, font=unicode_font, fill=font_color)
        i += 31
        c += 1
        font_color = move(font_color, tt[c:c + 3])

    res, rem = divmod(c3, 27928)
    r = round(start_limit * rem / 27928)
    res, rem = divmod(res, 27928)
    g = round(start_limit * rem / 27928)
    res, rem = divmod(res, 27928)
    b = round(start_limit * rem / 27928)
    font_color = r, g, b
    c = 0
    i = 0
    for l in tt[10:15]:
        draw.text((3 + i, 117), l, font=unicode_font, fill=font_color)
        i += 31
        c += 1
        font_color = move(font_color, tt[c:c + 3])
        # if c == 13:
        #     font_color = move(font_color, tt[13:15] + tt[1])
        # else:
        #     font_color = move(font_color, tt[14] + tt[1:3])

    im.save(f)
