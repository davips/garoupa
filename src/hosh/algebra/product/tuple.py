from hosh.algebra.abs.element import Element


class Tuple(Element):
    def __init__(self, *items):
        super().__init__()
        self.items = items
        itemsrv = list(reversed(items))
        lst = zip([1] + [(elema.order) for elema in itemsrv[:-1]], [elemb.i for elemb in itemsrv])
        self.i = sum(x * y for x, y in lst)

    def __mul__(self, other):
        return Tuple(*(a * b for a, b in zip(self.items, other.items)))

    def __repr__(self):
        return f"«{', '.join([str(a) for a in self.items])}»"
