from hosh.algebra.abs.element import Element
from hosh.math import int2bm8bit, bmm, bm2int8bit, bminv


class Mat8bit(Element):
    def __init__(self, i, _m=None):
        """        17x17 with 8 zeros to match 128 bits.        """
        super().__init__()
        self.i = i
        self.order = 2 ** 8
        if i == self.i and _m is not None:
            self.m = _m
        else:
            self.m = int2bm8bit(self.i)

    def __mul__(self, other):
        m = bmm(self.m, other.m)
        return Mat8bit(bm2int8bit(m), _m=m)

    def __repr__(self):
        return f"{self.m}"

    def __neg__(self):
        m = bminv(self.m)
        return Mat8bit(bm2int8bit(m), _m=m)
