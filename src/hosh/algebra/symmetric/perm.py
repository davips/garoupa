import sys
from math import factorial

from hosh.algebra.abs.element import Element
from hosh.math import pmat_inv, pmat_mult, pmat2int, int2pmat


class Perm(Element):
    def __init__(self, i, n, _perm=None):
        super().__init__()
        self.i, self.n = i, n
        self.order = factorial(n)
        if i == self.i and _perm:
            self.perm = _perm
        else:
            self.perm = int2pmat(self.i, self.n)

    def __mul__(self, other):
        perm = pmat_mult(self.perm, other.perm)
        return Perm(pmat2int(perm), self.n, _perm=perm)

    def __repr__(self):
        return f"{self.perm}"

    def __neg__(self):
        perm = pmat_inv(self.perm)
        return Perm(pmat2int(perm), self.n, _perm=perm)
