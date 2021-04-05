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

from garoupa.algebra.cyclic.nat import Nat
from garoupa.algebra.matrix.group import Group
from garoupa.algebra.product.product import Product


class Z(Group):
    def __init__(self, n, seed=0):
        sorted = lambda: (Nat(i, n) for i in range(n))
        super().__init__(Nat(0, n), sorted, seed)
        self.n = n

    @property
    def comm_degree(self):
        """Exact commutativity degree"""
        return 1

    def __iter__(self):
        while True:
            yield Nat(self.samplei(), self.n)

    def __repr__(self):
        return f"Z{self.n}"
