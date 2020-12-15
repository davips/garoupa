#  Copyright (c) 2020. Davi Pereira dos Santos
#  This file is part of the garoupa project.
#  Please respect the license - more about this in the section (*) below.
#
#  garoupa is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  garoupa is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with garoupa.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.

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


def colors(id, cols=6, incr=10, fgthreshold=127, bgthreshold=127, renew_at=1):
    # starts with darker two thirds based on bgcolor
    ns = toints(id, fgthreshold)
    cor = ns[0:3]
    ns = ns + ns[:2]
    l = []
    i = 0
    while i < len(id):
        cor = [ini + incr if ini < fim else ini - incr for ini, fim in zip(cor, ns[i:i + 3])]

        # mirror value, if outside limits
        cor = [2 * fgthreshold - c if c > fgthreshold else abs(c) for c in cor]

        l.append(cor)

        # new starting color for each row (5+6+6+6 = 23)
        if i % cols == renew_at:
            cor = ns[i + 1:i + 4]

        i += 1
    return [[int(round((255 - bgthreshold) * x / fgthreshold + bgthreshold)) for x in l[-1]]] + l


def avatar(id, f="avatar-id-$id.jpg", rows=4, incr=15, fgthreshold=230, bgthreshold=160, renew_at=4,
           font_filename="DejaVuSansMono-Bold.ttf",
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
        f = f.replace("$id", id)

    text = " " + id
    cs = colors(id, cols, incr, fgthreshold, bgthreshold, renew_at)
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

# u = UUID()
# u = u * u * u
# avatar(u.id, f="/tmp/a.jpg")
# # avatar("1PB2C52SP0Ccsqxc8SkrGyF", fgthreshold=200, bgthreshold=160)  # IRIS 1PB2C52SP0Ccsqxc8SkrGyF
# 1PB2C52SPOCSkrGyF
#
# # s = UUID.load_avatar("avatar-id-00000000000000000000001.jpg")
# s = UUID.load_avatar("/tmp/a.jpg")
#
# print(u.id, s[:-1])
# print(u.id == s[:-1])
