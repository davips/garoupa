# Abstract algebra module
from itertools import islice
from hosh.algebra.cyclic import Z
from hosh.algebra.dihedral import D
from hosh.algebra.symmetric import S

# Direct product between:
#   symmetric group S4;
#   cyclic group Z5; and,
#   dihedral group D4.
G = S(4) * Z(5) * D(4)
print(G)
# ...

# Sampling and operating over some pairs.
fetch5 = islice(G, 0, 5)
for a, b in zip(fetch5, G):
    print(a, "*", b, "=", a * b, sep="\t")
# ...
