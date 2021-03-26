from hosh.algebra.abs.element import Element


class R(Element):
    def __init__(self, i, n):
        super().__init__()
        self.i, self.n = i, n
        self.order = 2 * n

    def __mul__(self, other):
        i = (self.i + other.i) % self.n
        if isinstance(other, R):
            return R(i, self.n)
        else:
            from hosh.algebra.dihedral.s import S
            return S(i, self.n)
