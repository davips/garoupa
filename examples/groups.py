# Abstract algebra module
from itertools import islice
from math import factorial

from garoupa.algebra.cyclic import Z
from garoupa.algebra.dihedral import D

# Direct product between:
#   symmetric group S4;
#   cyclic group Z5; and,
#   dihedral group D4.
from garoupa.algebra.symmetric import S
from garoupa.algebra.symmetric.perm import Perm

G = S(4) * Z(5) * D(4)
print(G)
# ...

# Operating over 5 sampled pairs.
for a, b in islice(zip(G, G), 0, 5):
    print(a, "*", b, "=", a * b, sep="\t")
# ...

# Operator ~ is another way of sampling.
G = S(12)
print(~G)
# ...

# Manual element creation.
last_perm_i = factorial(12) - 1
a = Perm(i=last_perm_i, n=12)
print("Last element of S35:", a)
# ...

# Inverse element. Group S4.
a = Perm(i=21, n=4)
b = Perm(i=17, n=4)
print(a, "*", ~a, "=", (a * ~a).i, "=", a * ~a, "= identity")
# ...

print(a, "*", b, "=", a * b)
# ...

print(a, "*", b, "*", ~b, "=", a * b * ~b, "= a")
# ...

