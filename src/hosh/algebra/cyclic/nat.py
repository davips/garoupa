from hosh.algebra.abs.element import Element


class Nat(Element):
    def __init__(self, i, n):
        super().__init__()
        self.i, self.n = i, n
        self.order = n

    def __mul__(self, other):
        return Nat((self.i + other.i) % self.n, self.n)

    def __repr__(self):
        return f"{self.i}"
