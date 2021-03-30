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

import operator
from functools import reduce
from itertools import product, cycle
from math import log

from garoupa.algebra.product.tuple import Tuple


class Product:
    def __init__(self, *groups):
        self.order = reduce(operator.mul, [g.order for g in groups])
        self.groups = groups
        self.sorted = lambda: (Tuple(*es) for es in product(*(g.sorted() for g in self.groups)))
        self.identity = Tuple(*(g.identity for g in self.groups))
        self.bits = int(log(self.order, 2))

    def __iter__(self):
        its = [cycle(iter(g)) for g in self.groups]
        for i in range(self.order):
            yield Tuple(*(next(it) for it in its))

    def __repr__(self):
        return "×".join([str(g) for g in self.groups])

    def __mul__(self, other):
        if isinstance(other, Product):
            return Product(*self.groups, *other.groups)
        return Product(*self.groups, other)
