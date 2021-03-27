from hosh.algebra.abs.element import Element


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
        self.order = self.bits ** 2
        raise Exception("Not implemented. Use M17")

    def __mul__(self, other):
        raise Exception("Not implemented. Use M17")

    def __repr__(self):
        return f"M{self.n}"

    def __neg__(self):
        raise Exception("Not implemented. Use M17")
