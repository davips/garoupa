import operator
import random as rnd
from dataclasses import dataclass
from functools import reduce
from math import log

from hosh.algebra.product.product import Product
from hosh.algebra.symmetric.perm import Perm


@dataclass
class S:
    n: int

    def __post_init__(self):
        self.order = reduce(operator.mul, range(1, self.n + 1))
        self.sorted = lambda: (Perm(i, self.n) for i in range(self.order))
        self.id = Perm(0, self.n)
        self.bits = int(log(self.order, 2))

    def __iter__(self):
        for i in range(self.order):
            yield Perm(rnd.getrandbits(self.bits), self.n)

    def __mul__(self, other):
        return Product(self, other)

    def __repr__(self):
        return f"S{self.n}"
