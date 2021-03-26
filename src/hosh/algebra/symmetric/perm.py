from math import factorial

from hosh.algebra.abs.element import Element


class Perm(Element):
    def __init__(self, i, n):
        super().__init__()
        self.i, self.n = i, n
        self.order = factorial(n)
        available = list(range(n))
        mat = []
        for div in range(n, 0, -1):
            i, r = divmod(i, div)
            mat.append(available.pop(r))
        mat.extend(available)
        self.perm = mat

    def __mul__(self, other):
        perm = [self.perm[x] for x in other.perm]
        radix = self.n
        available = list(range(self.n))
        i = 1
        res = 0
        for row in perm:
            idx = available.index(row)
            del available[idx]
            res += idx * i
            i *= radix
            radix -= 1
        return Perm(res, self.n)

    def __repr__(self):
        return f"{self.perm}"
