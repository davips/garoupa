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

from math import factorial

from garoupa.algebra.abs.element import Element
from garoupa.algebra.math import pmat_inv, pmat_mult, pmat2int, int2pmat


class Perm(Element):
    def __init__(self, i, n, _perm=None):
        super().__init__(i, factorial(n))
        self.n = n
        self.perm = _perm if _perm else int2pmat(self.i, self.n)

    def __mul__(self, other):
        perm = pmat_mult(self.perm, other.perm)
        return Perm(pmat2int(perm), self.n, _perm=perm)

    def __repr__(self):
        return f"{self.perm}"

    def __invert__(self):
        perm = pmat_inv(self.perm)
        return Perm(pmat2int(perm), self.n, _perm=perm)
