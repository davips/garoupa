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

from garoupa.algebra.matrix.group import Group
from garoupa.algebra.matrix.mat8bit import Mat8bit
from garoupa.algebra.product.product import Product


class M8bit(Group):
    def __init__(self):
        super().__init__(Mat8bit(0), lambda: (Mat8bit(i) for i in range(self.order)))

    def __iter__(self):
        for i in range(self.order):
            yield Mat8bit(rnd.getrandbits(int(self.bits)))

    def __mul__(self, other):
        return Product(self, other)

    def __repr__(self):
        return self.__class__.__name__

    def __invert__(self):
        return Mat8bit(rnd.getrandbits(int(self.bits)))
