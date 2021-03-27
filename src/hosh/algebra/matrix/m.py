import random as rnd
from hosh.algebra.abs.element import Element
from hosh.algebra.matrix.mat import Mat
from hosh.algebra.product import Product


class M(Element):
    def __init__(self, n):
        """
        1 b b b
        0 1 b b
        0 0 1 b
        0 0 0 1
        """
        super().__init__()
        self.n = n
        self.bits = sum(range(1, n))
        self.order = 2 ** self.bits
        self.sorted = lambda: (Mat(i, self.n) for i in range(self.order))

    def __iter__(self):
        for i in range(self.order):
            yield Mat(rnd.getrandbits(self.bits), self.n)

    def __mul__(self, other):
        return Product(self, other)

    def __repr__(self):
        return f"M{self.n}"

    def __invert__(self):
        return Mat(rnd.getrandbits(self.bits), self.n)
