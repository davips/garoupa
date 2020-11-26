from random import random
from timeit import timeit

from cruipto.linalg import int2pmat, print_binmatrix, pmat2int, \
    int2fac, pmat_mult
from cruipto.uuid import UUID

# Show output of operations.
a = UUID(int2pmat(2 ** 128 - 1))
b = UUID('12345678901234')
c = UUID(1)
print(a, b, c)
print()
print((a * b))
print((a * b) * b)
print((a * b) * b.t)
print((a * b) * c)

# Check for collisions.
s = set()
r = set()
aa = bb = 0
for i in range(100000):
    while aa in r:
        aa = round(random() * 2 ** 128)
    while bb in r:
        bb = round(random() * 2 ** 128)
    r.add(aa)
    r.add(bb)
    a = int2pmat(aa)
    b = int2pmat(bb)
    n = pmat2int(pmat_mult(a, b))
    s.add(a)
    s.add(b)
    s.add(n)
    if i > len(s) - 1:
        print(i, a, b, n)
        print('Colision detected!!!!!!!!!!!!!!')
        break
if i == 100000-1:
    print('No collisions!')


# Check general overhead of all uuid ops.
def f():
    a = UUID(int2pmat(2 ** 128 - 1))
    b = UUID('12345678901234')
    (a * b) * b.t


print(timeit(f, number=10000) * 100, 'us')
