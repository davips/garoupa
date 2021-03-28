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
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.

from hashlib import md5

import colored
from colored import stylize

from garoupa.base62 import b62dec


def paint(txt, fgr, fgg, fgb):
    fgcolor = f"#{hex(fgr)[2:].rjust(2, '0')}{hex(fgg)[2:].rjust(2, '0')}{hex(fgb)[2:].rjust(2, '0')}"
    return stylize(txt, colored.fg(fgcolor) + colored.attr("bold"))


def lim(x):
    return min(255, max(0, x))


def colorize128bit(id, ampl=0.8, change=0.1):
    numbers = md5(id.encode()).digest()
    margin = 60
    base = numbers[0]
    ch = 255 * change
    fgr = margin + (base ^ numbers[1]) * ampl
    fgg = margin + (base ^ numbers[2]) * ampl
    fgb = margin + (base ^ numbers[3]) * ampl
    out = ""
    for i, c in enumerate(id):
        quot, dr = divmod(b62dec(c)[1], 4)
        quot, dg = divmod(quot, 4)
        db = quot % 4
        r = max(margin, lim(fgr + ch * (dr - 2)))
        g = max(margin, lim(fgg + ch * (dg - 2)))
        b = max(margin, lim(fgb + ch * (db - 2)))
        out += f"{paint(c, int(r), int(g), int(b))}"
    return out
