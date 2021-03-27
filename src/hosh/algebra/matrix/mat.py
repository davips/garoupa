from hosh.algebra.abs.element import Element
from hosh.math import int2bml, bmm, bm2intl, bminv


class Mat(Element):
    def __init__(self, i, n, _m=None):
        """        nxn        """
        super().__init__()
        self.i, self.n = i, n
        self.bits = sum(range(1, n))
        self.order = 2 ** self.bits
        if i == self.i and _m is not None:
            self.m = _m
        else:
            self.m = int2bml(self.i, self.n, self.bits)

    def __mul__(self, other):
        m = bmm(self.m, other.m)
        return Mat(bm2intl(m, self.bits), self.n, _m=m)

    def __repr__(self):
        return f"{self.m}"

    def __neg__(self):
        m = bminv(self.m)
        return Mat(bm2intl(m, self.bits), self.n, _m=m)
