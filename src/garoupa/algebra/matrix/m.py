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

from garoupa.algebra.matrix.group import Group
from garoupa.algebra.matrix.mat import Mat
from garoupa.algebra.product import Product


class M(Group):
    def __init__(self, n, mod=2):
        """
        1 b b b
        0 1 b b
        0 0 1 b
        0 0 0 1
        """
        identity = Mat(0, n, mod)
        self.cells = identity.cells
        sorted = lambda: (Mat(i, self.n) for i in range(identity.order))
        super().__init__(identity, sorted)
        self.n, self.mod = n, mod

    def __iter__(self):
        while True:
            yield Mat(self.samplei(), self.n, self.mod)

    def __mul__(self, other):
        return Product(self, other)

    def __repr__(self):
        return f"M{self.n}%{self.mod}"

    def __invert__(self):
        return Mat(self.samplei(), self.n, self.mod)
