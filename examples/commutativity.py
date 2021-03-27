# Commutativity degree of groups
from itertools import product

from hosh.algebra.dihedral import D
from hosh.algebra.matrix.m17 import M17
from hosh.algebra.matrix.m6 import M6
from hosh.algebra.matrix.m8bit import M8bit


def traverse(G):
    i, count = G.order, G.order
    for idx, a in enumerate(G.sorted()):
        for b in list(G.sorted())[idx + 1:]:
            if a * b == b * a:
                count += 2
            i += 2
    print(f"|{G}| = ".rjust(20, ' '),
          f"{G.order}:".ljust(10, ' '),
          f"{count}/{i}:".rjust(10, ' '),
          f"\t{100 * count / i} %", sep="")


traverse(D(8))
# ...

traverse(D(8) ^ 2)
# ...

traverse(M8bit())
# ...

# Large groups (sampling is needed).
Gs = [M6(), D(8) ** 3]
for G in Gs:
    i, count = 0, 0
    for a, b in product(G, G):
        if a * b == b * a:
            count += 1
        i += 1
        if i > 20000:
            break
    print(f"|{G}| = ".rjust(20, ' '),
          f"{G.order}:".ljust(10, ' '),
          f"{count}/{i}:".rjust(10, ' '),
          f"\t{100 * count / i} %", sep="")
# ...
