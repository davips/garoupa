from hosh.algebra.abs.element import Element


class Mat(Element):
    def __init__(self, i, n, _m=None):
        """
        1 b b b
        0 1 b b
        0 0 1 b
        0 0 0 1
        """
        super().__init__()
        self.i, self.n = i, n
        self.nbits = sum(range(1, n))
        self.order = self.nbits ** 2
        if i == self.i and _m:
            self.m = _m
        else:
            # self.m =
            raise Exception("Not implemented. Use Mat17 or Mat6 or ...?")

    def __mul__(self, other):
        raise Exception("Not implemented. Use Mat17 or Mat6 or ...?")

    def __repr__(self):
        return f"{self.m}"

    def __neg__(self):
        raise Exception("Not implemented. Use Mat17 or Mat6 or ...?")
