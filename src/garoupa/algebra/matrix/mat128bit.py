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
from garoupa.algebra.abs.element import Element
from garoupa.algebra.matrix.mat import Mat
from garoupa.algebra.npmath import int2bm, bm2int, bminv, bmm


class Mat128bit(Element):
    def __init__(self, i, _m=None):
        """nxn     modulo o
        Usage:

        >>> a = Mat(4783632, 6, 5)
        >>> a
        [[1 2 1 0 4 3]
         [0 1 0 1 1 2]
         [0 0 1 2 0 0]
         [0 0 0 1 0 0]
         [0 0 0 0 1 0]
         [0 0 0 0 0 1]]
        """
        super().__init__(i, 2 ** 128)
        self.m = int2bm(i) if _m is None else _m

    def __mul__(self, other):
        m = bmm(self.m, other.m, 2)
        return Mat128bit(bm2int(m), _m=m)

    def __repr__(self):
        return f"{self.m}"

    def __invert__(self):
        m = bminv(self.m)
        return Mat128bit(bm2int(m), _m=m)
