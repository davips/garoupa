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
from colored import stylize


def paint(txt, fgr, fgg, fgb):
    fgcolor = f"#{hex(fgr)[2:].rjust(2, '0')}{hex(fgg)[2:].rjust(2, '0')}{hex(fgb)[2:].rjust(2, '0')}"
    return stylize(txt, colored.fg(fgcolor) + colored.attr("bold") + colored.bg("#000000"))


def lim(x):
    return min(255, max(0, x))


def colorize128bit(id, digits, ampl=0.8, change=0.44):
    """
    Usage:

    >>> c = colorize128bit("Iaz3L67a2BQv0GifoWOjWale6LYFTGmJJ1ZPfdoPJNO", 32)
    >>> c == '\x1b[38;5;96m\x1b[1m\x1b[48;5;0mI\x1b[0m\x1b[38;5;133m\x1b[1m\x1b[48;5;0ma\x1b[0m\x1b[38;5;98m\x1b[1m\x1b[48;5;0mz\x1b[0m\x1b[38;5;138m\x1b[1m\x1b[48;5;0m3\x1b[0m\x1b[38;5;168m\x1b[1m\x1b[48;5;0mL\x1b[0m\x1b[38;5;97m\x1b[1m\x1b[48;5;0m6\x1b[0m\x1b[38;5;96m\x1b[1m\x1b[48;5;0m7\x1b[0m\x1b[38;5;133m\x1b[1m\x1b[48;5;0ma\x1b[0m\x1b[38;5;134m\x1b[1m\x1b[48;5;0m2\x1b[0m\x1b[38;5;140m\x1b[1m\x1b[48;5;0mB\x1b[0m\x1b[38;5;176m\x1b[1m\x1b[48;5;0mQ\x1b[0m\x1b[38;5;175m\x1b[1m\x1b[48;5;0mv\x1b[0m\x1b[38;5;170m\x1b[1m\x1b[48;5;0m0\x1b[0m\x1b[38;5;248m\x1b[1m\x1b[48;5;0mG\x1b[0m\x1b[38;5;168m\x1b[1m\x1b[48;5;0mi\x1b[0m\x1b[38;5;133m\x1b[1m\x1b[48;5;0mf\x1b[0m\x1b[38;5;96m\x1b[1m\x1b[48;5;0mo\x1b[0m\x1b[38;5;133m\x1b[1m\x1b[48;5;0mW\x1b[0m\x1b[38;5;98m\x1b[1m\x1b[48;5;0mO\x1b[0m\x1b[38;5;138m\x1b[1m\x1b[48;5;0mj\x1b[0m\x1b[38;5;168m\x1b[1m\x1b[48;5;0mW\x1b[0m\x1b[38;5;97m\x1b[1m\x1b[48;5;0ma\x1b[0m\x1b[38;5;96m\x1b[1m\x1b[48;5;0ml\x1b[0m\x1b[38;5;133m\x1b[1m\x1b[48;5;0me\x1b[0m\x1b[38;5;134m\x1b[1m\x1b[48;5;0m6\x1b[0m\x1b[38;5;140m\x1b[1m\x1b[48;5;0mL\x1b[0m\x1b[38;5;176m\x1b[1m\x1b[48;5;0mY\x1b[0m\x1b[38;5;175m\x1b[1m\x1b[48;5;0mF\x1b[0m\x1b[38;5;170m\x1b[1m\x1b[48;5;0mT\x1b[0m\x1b[38;5;248m\x1b[1m\x1b[48;5;0mG\x1b[0m\x1b[38;5;168m\x1b[1m\x1b[48;5;0mm\x1b[0m\x1b[38;5;133m\x1b[1m\x1b[48;5;0mJ\x1b[0m\x1b[38;5;96m\x1b[1m\x1b[48;5;0mJ\x1b[0m\x1b[38;5;133m\x1b[1m\x1b[48;5;0m1\x1b[0m\x1b[38;5;98m\x1b[1m\x1b[48;5;0mZ\x1b[0m\x1b[38;5;138m\x1b[1m\x1b[48;5;0mP\x1b[0m\x1b[38;5;168m\x1b[1m\x1b[48;5;0mf\x1b[0m\x1b[38;5;97m\x1b[1m\x1b[48;5;0md\x1b[0m\x1b[38;5;96m\x1b[1m\x1b[48;5;0mo\x1b[0m\x1b[38;5;133m\x1b[1m\x1b[48;5;0mP\x1b[0m\x1b[38;5;134m\x1b[1m\x1b[48;5;0mJ\x1b[0m\x1b[38;5;140m\x1b[1m\x1b[48;5;0mN\x1b[0m\x1b[38;5;176m\x1b[1m\x1b[48;5;0mO\x1b[0m'
    True
    """
    numbers = md5(id.encode()).digest()
    margin = 64
    fgr = margin + numbers[1] * ampl
    fgg = margin + numbers[2] * ampl
    fgb = margin + numbers[3] * ampl
    out = ""
    nnn = numbers * (digits * 3 // 2)
    for dr, dg, db, c in zip(nnn, nnn[1:], nnn[2:], id):
        r = max(margin, lim(fgr + change * (dr - 128)))
        g = max(margin, lim(fgg + change * (dg - 128)))
        b = max(margin, lim(fgb + change * (db - 128)))
        out += f"{paint(c, int(r), int(g), int(b))}"
    return out
