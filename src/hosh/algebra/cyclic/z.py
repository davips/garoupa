import random as rnd
from dataclasses import dataclass
from math import log

from hosh.algebra.cyclic.nat import Nat
from hosh.algebra.product.product import Product


@dataclass
class Z:
    n: int

    def __post_init__(self):
        self.order = self.n
        self.sorted = lambda: (Nat(i, self.n) for i in range(self.order))
        self.id = Nat(0, self.n)
        self.bits = int(log(self.order, 2))

    def __iter__(self):
        for i in range(self.order):
            yield Nat(rnd.getrandbits(self.bits), self.n)

    def __mul__(self, other):
        return Product(self, other)

    def __repr__(self):
        return f"Z{self.n}"
