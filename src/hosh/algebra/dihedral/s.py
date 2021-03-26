from hosh.algebra.abs.element import Element


class S(Element):
    def __init__(self, i, n):
        super().__init__()
        self.i, self.n = i, n
        self.order = n

    def __mul__(self, other):
        i = (self.i - other.i) % self.n
        if isinstance(other, S):
            from hosh.algebra.dihedral.r import R
            return R(i, self.n)
        else:
            return S(i, self.n)
