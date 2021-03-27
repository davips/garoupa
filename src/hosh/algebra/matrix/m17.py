#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the hoshy project.
#  Please respect the license - more about this in the section (*) below.
#
#  hoshy is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  hoshy is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with hoshy.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.
import random as rnd
from dataclasses import dataclass

from hosh.algebra.matrix.mat17 import Mat17
from hosh.algebra.product.product import Product


@dataclass
class M17:
    def __post_init__(self):
        self.order = 2 ** 128
        self.sorted = lambda: (Mat17(i) for i in range(self.order))
        self.id = Mat17(0)
        self.bits = 128

    def __iter__(self):
        for i in range(self.order):
            yield Mat17(rnd.getrandbits(self.bits))

    def __mul__(self, other):
        return Product(self, other)

    def __repr__(self):
        return f"M17"

    def __invert__(self):
        return Mat17(rnd.getrandbits(self.bits))
