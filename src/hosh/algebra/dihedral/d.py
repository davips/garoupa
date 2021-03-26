import random as rnd
from dataclasses import dataclass
from itertools import chain
from math import log

from hosh.algebra.dihedral.r import R
from hosh.algebra.dihedral.s import S
from hosh.algebra.product.product import Product


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

    def __iter__(self):
        for i in range(self.order):
            yield rnd.choice([R, S])(rnd.getrandbits(self.bits), self.n)

    def __mul__(self, other):
        return Product(self, other)

    def __repr__(self):
        return f"D{self.n}"
