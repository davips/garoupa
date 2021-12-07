#  Copyright (c) 2021. Davi Pereira dos Santos
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
#  part of this work is illegal and is unethical regarding the effort and
#  time spent here.
"""Functions to colorize representation of Hosh objects, e.g. on ipython"""
from hashlib import md5

import colored
from ansi2html import Ansi2HTMLConverter
from colored import stylize

from garoupa.config import GLOBAL


def paint(txt, fgr, fgg, fgb):
    """
    >>> from garoupa import setup, ø
    >>> ø * b"asd"
    \x1b[38;5;71m\x1b[1m\x1b[48;5;0mL\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0ms\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mx\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mC\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0ma\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mj\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0ml\x1b[0m\x1b[38;5;78m\x1b[1m\x1b[48;5;0mK\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0m8\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0m3\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0m0\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mA\x1b[0m\x1b[38;5;72m\x1b[1m\x1b[48;5;0mK\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mq\x1b[0m\x1b[38;5;149m\x1b[1m\x1b[48;5;0mt\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mU\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0m5\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mv\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0m0\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mC\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0m9\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mY\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mV\x1b[0m\x1b[38;5;78m\x1b[1m\x1b[48;5;0m9\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0mb\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0mQ\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0mn\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mZ\x1b[0m\x1b[38;5;72m\x1b[1m\x1b[48;5;0mJ\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0m1\x1b[0m\x1b[38;5;149m\x1b[1m\x1b[48;5;0mw\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mG\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0m3\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mq\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0ms\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0ml\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mW\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0m9\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mZ\x1b[0m\x1b[38;5;78m\x1b[1m\x1b[48;5;0m6\x1b[0m
    >>> setup(dark_theme=False)
    >>> ø * b"asd"
    \x1b[38;5;2m\x1b[1m\x1b[48;5;15mL\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15ms\x1b[0m\x1b[38;5;22m\x1b[1m\x1b[48;5;15mx\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15mC\x1b[0m\x1b[38;5;22m\x1b[1m\x1b[48;5;15ma\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15mj\x1b[0m\x1b[38;5;22m\x1b[1m\x1b[48;5;15ml\x1b[0m\x1b[38;5;28m\x1b[1m\x1b[48;5;15mK\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15m8\x1b[0m\x1b[38;5;64m\x1b[1m\x1b[48;5;15m3\x1b[0m\x1b[38;5;70m\x1b[1m\x1b[48;5;15m0\x1b[0m\x1b[38;5;64m\x1b[1m\x1b[48;5;15mA\x1b[0m\x1b[38;5;23m\x1b[1m\x1b[48;5;15mK\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15mq\x1b[0m\x1b[38;5;70m\x1b[1m\x1b[48;5;15mt\x1b[0m\x1b[38;5;58m\x1b[1m\x1b[48;5;15mU\x1b[0m\x1b[38;5;2m\x1b[1m\x1b[48;5;15m5\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15mv\x1b[0m\x1b[38;5;22m\x1b[1m\x1b[48;5;15m0\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15mC\x1b[0m\x1b[38;5;22m\x1b[1m\x1b[48;5;15m9\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15mY\x1b[0m\x1b[38;5;22m\x1b[1m\x1b[48;5;15mV\x1b[0m\x1b[38;5;28m\x1b[1m\x1b[48;5;15m9\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15mb\x1b[0m\x1b[38;5;64m\x1b[1m\x1b[48;5;15mQ\x1b[0m\x1b[38;5;70m\x1b[1m\x1b[48;5;15mn\x1b[0m\x1b[38;5;64m\x1b[1m\x1b[48;5;15mZ\x1b[0m\x1b[38;5;23m\x1b[1m\x1b[48;5;15mJ\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15m1\x1b[0m\x1b[38;5;70m\x1b[1m\x1b[48;5;15mw\x1b[0m\x1b[38;5;58m\x1b[1m\x1b[48;5;15mG\x1b[0m\x1b[38;5;2m\x1b[1m\x1b[48;5;15m3\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15mq\x1b[0m\x1b[38;5;22m\x1b[1m\x1b[48;5;15ms\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15ml\x1b[0m\x1b[38;5;22m\x1b[1m\x1b[48;5;15mW\x1b[0m\x1b[38;5;34m\x1b[1m\x1b[48;5;15m9\x1b[0m\x1b[38;5;22m\x1b[1m\x1b[48;5;15mZ\x1b[0m\x1b[38;5;28m\x1b[1m\x1b[48;5;15m6\x1b[0m
    """
    if GLOBAL["dark_theme"]:
        bgcolor = colored.bg("#000000")
    else:
        bgcolor = colored.bg("#FFFFFF")
    fgcolor = f"#{hex(fgr)[2:].rjust(2, '0')}{hex(fgg)[2:].rjust(2, '0')}{hex(fgb)[2:].rjust(2, '0')}"
    return stylize(txt, colored.fg(fgcolor) + colored.attr("bold") + bgcolor)


def lim(x):
    return min(255, max(0, x))


def id2ansi(id, ampl=0.8, change=0.44):
    rgbs = id2rgb(id, ampl, change)[1:]
    strs = [paint(l, *rgb) for l, rgb in zip(id, rgbs)]
    return "".join(strs)


def id2rgb(id, ampl=0.8, change=0.44, dark=None):
    if dark is None:
        dark = GLOBAL["dark_theme"]
    digits = len(id)
    numbers = md5(id.encode()).digest()
    margin = 64
    fgr = margin + numbers[1] * ampl
    fgg = margin + numbers[2] * ampl
    fgb = margin + numbers[3] * ampl
    out = []
    nnn = numbers * (digits * 3 // 2)
    bgr, bgg, bgb = 0, 0, 0
    for dr, dg, db, _ in zip(nnn, nnn[1:], nnn[2:], id):
        r = max(margin, lim(fgr + change * (dr - 128)))
        g = max(margin, lim(fgg + change * (dg - 128)))
        b = max(margin, lim(fgb + change * (db - 128)))
        if not dark:
            r = r - 130
            g = g - 130
            b = b - 130
            if r < 0 or g < 0 or b < 0:
                worst = min([r, g, b])
                r -= worst
                g -= worst
                b -= worst
        out.append([int(r), int(g), int(b)])
        bgr += r
        bgg += g
        bgb += b
    bgr = int(255 - bgr / digits)
    bgg = int(255 - bgg / digits)
    bgb = int(255 - bgb / digits)
    return [[bgr, bgg, bgb]] + out


def ansi2html(ansi, **kwargs):
    r"""
    >>> from garoupa import Hosh
    >>> Hosh(b"asd").idc
    '\x1b[38;5;71m\x1b[1m\x1b[48;5;0mL\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0ms\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mx\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mC\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0ma\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mj\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0ml\x1b[0m\x1b[38;5;78m\x1b[1m\x1b[48;5;0mK\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0m8\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0m3\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0m0\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mA\x1b[0m\x1b[38;5;72m\x1b[1m\x1b[48;5;0mK\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mq\x1b[0m\x1b[38;5;149m\x1b[1m\x1b[48;5;0mt\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mU\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0m5\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mv\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0m0\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mC\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0m9\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mY\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mV\x1b[0m\x1b[38;5;78m\x1b[1m\x1b[48;5;0m9\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0mb\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0mQ\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0mn\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mZ\x1b[0m\x1b[38;5;72m\x1b[1m\x1b[48;5;0mJ\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0m1\x1b[0m\x1b[38;5;149m\x1b[1m\x1b[48;5;0mw\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mG\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0m3\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mq\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0ms\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0ml\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mW\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0m9\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mZ\x1b[0m\x1b[38;5;78m\x1b[1m\x1b[48;5;0m6\x1b[0m'
    >>> Hosh(b"asd").html
    '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n<title></title>\n<style type="text/css">\n.ansi2html-content { display: inline; white-space: pre-wrap; word-wrap: break-word; }\n.body_foreground { color: #AAAAAA; }\n.body_background { background-color: #000000; }\n.body_foreground > .bold,.bold > .body_foreground, body.body_foreground > pre > .bold { color: #FFFFFF; font-weight: normal; }\n.inv_foreground { color: #000000; }\n.inv_background { background-color: #AAAAAA; }\n.ansi1 { font-weight: bold; }\n.ansi48-0 { background-color: #000316; }\n.ansi38-71 { color: #5faf5f; }\n.ansi38-72 { color: #5faf87; }\n.ansi38-107 { color: #87af5f; }\n.ansi38-78 { color: #5fd787; }\n.ansi38-113 { color: #87d75f; }\n.ansi38-149 { color: #afd75f; }\n.ansi38-83 { color: #5fff5f; }\n.ansi38-119 { color: #87ff5f; }\n</style>\n</head>\n<body class="body_foreground body_background" style="font-size: normal;" >\n<pre class="ansi2html-content">\n<span class="ansi38-71"></span><span class="ansi1 ansi38-71"></span><span class="ansi1 ansi38-71 ansi48-0">L</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">s</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">x</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">C</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">a</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">j</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">l</span><span class="ansi38-78"></span><span class="ansi1 ansi38-78"></span><span class="ansi1 ansi38-78 ansi48-0">K</span><span class="ansi38-119"></span><span class="ansi1 ansi38-119"></span><span class="ansi1 ansi38-119 ansi48-0">8</span><span class="ansi38-113"></span><span class="ansi1 ansi38-113"></span><span class="ansi1 ansi38-113 ansi48-0">3</span><span class="ansi38-113"></span><span class="ansi1 ansi38-113"></span><span class="ansi1 ansi38-113 ansi48-0">0</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">A</span><span class="ansi38-72"></span><span class="ansi1 ansi38-72"></span><span class="ansi1 ansi38-72 ansi48-0">K</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">q</span><span class="ansi38-149"></span><span class="ansi1 ansi38-149"></span><span class="ansi1 ansi38-149 ansi48-0">t</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">U</span><span class="ansi38-71"></span><span class="ansi1 ansi38-71"></span><span class="ansi1 ansi38-71 ansi48-0">5</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">v</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">0</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">C</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">9</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">Y</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">V</span><span class="ansi38-78"></span><span class="ansi1 ansi38-78"></span><span class="ansi1 ansi38-78 ansi48-0">9</span><span class="ansi38-119"></span><span class="ansi1 ansi38-119"></span><span class="ansi1 ansi38-119 ansi48-0">b</span><span class="ansi38-113"></span><span class="ansi1 ansi38-113"></span><span class="ansi1 ansi38-113 ansi48-0">Q</span><span class="ansi38-113"></span><span class="ansi1 ansi38-113"></span><span class="ansi1 ansi38-113 ansi48-0">n</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">Z</span><span class="ansi38-72"></span><span class="ansi1 ansi38-72"></span><span class="ansi1 ansi38-72 ansi48-0">J</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">1</span><span class="ansi38-149"></span><span class="ansi1 ansi38-149"></span><span class="ansi1 ansi38-149 ansi48-0">w</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">G</span><span class="ansi38-71"></span><span class="ansi1 ansi38-71"></span><span class="ansi1 ansi38-71 ansi48-0">3</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">q</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">s</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">l</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">W</span><span class="ansi38-83"></span><span class="ansi1 ansi38-83"></span><span class="ansi1 ansi38-83 ansi48-0">9</span><span class="ansi38-107"></span><span class="ansi1 ansi38-107"></span><span class="ansi1 ansi38-107 ansi48-0">Z</span><span class="ansi38-78"></span><span class="ansi1 ansi38-78"></span><span class="ansi1 ansi38-78 ansi48-0">6</span>\n</pre>\n</body>\n\n</html>\n'
    """
    conv = Ansi2HTMLConverter(dark_bg=GLOBAL["dark_theme"], **kwargs)
    return conv.convert(ansi)
