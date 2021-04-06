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

from garoupa.algebra.abs.element import Element
from garoupa.math import int2bm8bit, bmm, bm2int8bit, bminv


class Mat8bit(Element):
    def __init__(self, i, _m=None):
        """        17x17 with 8 zeros to match 128 bits.        """
        super().__init__(i, 2 ** 8)
        if i == self.i and _m is not None:
            self.m = _m
        else:
            self.m = int2bm8bit(self.i)

    def __mul__(self, other):
        m = bmm(self.m, other.m, 2)
        return Mat8bit(bm2int8bit(m), _m=m)

    def __repr__(self):
        return f"{self.m}"

    def __invert__(self):
        m = bminv(self.m)
        return Mat8bit(bm2int8bit(m), _m=m)
