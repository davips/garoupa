# Abstract algebra module
from itertools import islice
from math import factorial

from hosh.algebra.cyclic import Z
from hosh.algebra.dihedral import D

# Direct product between:
#   symmetric group S4;
#   cyclic group Z5; and,
#   dihedral group D4.
from hosh.algebra.symmetric import S
from hosh.algebra.symmetric.perm import Perm

G = S(4) * Z(5) * D(4)
print(G)
# ...

# Sampling and operating over some pairs.
fetch5 = islice(G, 0, 5)
for a, b in zip(fetch5, G):
    print(a, "*", b, "=", a * b, sep="\t")
# ...

# Operator ~ is another way of sampling. Group S35 modulo 2^128.
G = S(35, 2 ** 128)
print(~G)
# ...

# Manual element creation. Group S35 modulo 2^128.
last_perm_i = factorial(35) - 1
last_128bit = 2 ** 128 - 1
a = Perm(i=last_perm_i, n=35, m=last_128bit)
print(a.i, "=", last_perm_i % last_128bit, sep="\t")
# ...

# Inverse element. Group S4 modulo 20.
a = Perm(i=21, n=4, m=20)
b = Perm(i=17, n=4, m=20)
print(a, "*", -a, "=", (a * -a).i, "=", a * -a)
# ...

print(a, "*", b, "=", a * b)
# ...

print(a, "*", b, "*", -b, "=", a * b * -b)
# ...
