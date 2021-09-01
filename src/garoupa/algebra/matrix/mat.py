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
from garoupa.algebra.npmath import int2ml, m2intl


class Mat(Element):
    def __init__(self, i, n, mod=2, _m=None):
        """nxn     modulo o
        Usage:

        >>> a = Mat(4783632, 6, 10)
        >>> a
        [[1 2 3 6 3 8]
         [0 1 7 4 0 0]
         [0 0 1 0 0 0]
         [0 0 0 1 0 0]
         [0 0 0 0 1 0]
         [0 0 0 0 0 1]]
        >>> a2 = a * a
        >>> a2
        [[1 4 0 0 6 6]
         [0 1 4 8 0 0]
         [0 0 1 0 0 0]
         [0 0 0 1 0 0]
         [0 0 0 0 1 0]
         [0 0 0 0 0 1]]
        >>> b = Mat(9947632, 6, 10)
        >>> a * b * a2  * ~a2 * ~b == a
        True
        """
        self.cells = sum(range(1, n))
        super().__init__(i, order=mod ** self.cells)
        self.n, self.mod = n, mod
        self.m = int2ml(i, mod, n) if _m is None else _m

    def __mul__(self, other):
        if self.mod != other.mod or self.n != other.n:
            raise Exception("Elements are from different groups.")
        m = (self.m @ other.m) % self.mod
        return Mat(m2intl(m, self.mod), self.n, self.mod, _m=m)

    def __repr__(self):
        return f"{self.m}"

    def __invert__(self):
        """
        >>> a = Mat(8761437689349876134, 4, 4294967291)
        >>> b = Mat(42978259879825, 4, 4294967291)
        >>> a == a * b * ~b
        True

        :return:
        """
        import numpy as np

        m = (np.linalg.inv(self.m) % self.mod).astype(np.uint64)
        return Mat(m2intl(m, self.mod), self.n, self.mod, _m=m)
