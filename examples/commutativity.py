# Commutativity degree of groups

from garoupa.algebra.cyclic import Z
from garoupa.algebra.dihedral import D
from garoupa.algebra.matrix.m import M


def traverse(G):
    i, count = G.order, G.order
    for idx, a in enumerate(G.sorted()):
        for b in list(G.sorted())[idx + 1 :]:
            if a * b == b * a:
                count += 2
            i += 2
    print(
        f"|{G}| = ".rjust(20, " "),
        f"{G.order}:".ljust(10, " "),
        f"{count}/{i}:".rjust(15, " "),
        f"  {G.bits} bits",
        f"\t{100 * count / i} %",
        sep="",
    )


# Dihedral
traverse(D(8))
# ...
traverse(D(8) ^ 2)
# ...

# Z4!
traverse(Z(4) * Z(3) * Z(2))
# ...

# M 3x3 %4
traverse(M(3, 4))

# Large groups (sampling is needed).
Gs = [D(8) ^ 3, D(8) ^ 4, D(8) ^ 5]
for G in Gs:
    i, count = 0, 0
    for a, b in zip(G, G):
        if a * b == b * a:
            count += 1
        if i >= 10_000:
            break
        i += 1
    print(
        f"|{G}| = ".rjust(20, " "),
        f"{G.order}:".ljust(10, " "),
        f"{count}/{i}:".rjust(15, " "),
        f"  {G.bits} bits",
        f"\t~{100 * count / i} %",
        sep="",
    )
# ...
