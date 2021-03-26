import operator
from functools import reduce
from itertools import product, cycle

from hosh.algebra.product.tuple import Tuple


class Product:
    def __init__(self, *groups):
        self.order = reduce(operator.mul, [g.order for g in groups])
        self.groups = groups
        self.sorted = lambda: (Tuple(*es) for es in product(*self.groups))
        self.id = Tuple(*(g.id for g in self.groups))

    def __iter__(self):
        its = [cycle(iter(g)) for g in self.groups]
        for i in range(self.order):
            yield Tuple(*(next(it) for it in its))

    def __repr__(self):
        return "×".join([str(g) for g in self.groups])

    def __mul__(self, other):
        if isinstance(other, Product):
            return Product(*self.groups, *other.groups)
        return Product(*self.groups, other)
