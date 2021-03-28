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

import random as rnd
from dataclasses import dataclass
from itertools import chain, repeat
from math import log

from garoupa.algebra.dihedral.r import R
from garoupa.algebra.dihedral.s import S
from garoupa.algebra.product.product import Product


@dataclass
class D:
    n: int

    def __post_init__(self):
        self.order = self.n * 2
        self.r = lambda: (R(r, self.n) for r in range(self.n))
        self.s = lambda: (S(s, self.n) for s in range(self.n))
        self.sorted = lambda: chain(self.r(), self.s())
        self.id = R(0, self.n)
        self.bits = int(log(self.order, 2))

    @property
    def comm_degree(self):
        """Exact commutativity degree"""
        num = (self.n + 3) if self.n % 2 == 0 else (self.n + 6)
        den = 4 * self.n
        return num / den

    def __iter__(self):
        for i in range(self.order):
            yield rnd.choice([R, S])(rnd.getrandbits(self.bits), self.n)

    def __mul__(self, other):
        return Product(self, other)

    def __repr__(self):
        return f"D{self.n}"

    def __xor__(self, other):
        return Product(*repeat(self, other))

    __pow__ = __xor__
