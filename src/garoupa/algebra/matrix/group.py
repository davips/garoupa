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
from dataclasses import dataclass
from itertools import repeat
from random import Random

from garoupa.algebra.abs.element import Element


@dataclass
class Group:
    identity: Element
    sorted: callable
    seed: int = 0

    def __post_init__(self):
        self.bits = self.identity.bits
        self.order = self.identity.order
        self.name = self.__class__.__name__
        self.rnd = Random(self.seed)

    @property
    def comm_degree(self):
        raise Exception("Not implemented for groups of the class", self.name)

    def __iter__(self):
        raise Exception("Not implemented for groups of the class", self.name)

    def __invert__(self) -> Element:
        return next(iter(self))

    def samplei(self):
        return self.rnd.getrandbits(int(self.bits))

    def __mul__(self, other):
        from garoupa.algebra.product import Product
        return Product(self, other)

    def __xor__(self, other):
        from garoupa.algebra.product import Product
        return Product(*repeat(self, other))

    __pow__ = __xor__
