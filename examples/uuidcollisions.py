from random import random
from timeit import timeit

from garoupa.hash import Hash
from garoupa.linalg import int2pmat, pmat2int, \
    pmat_mult
from garoupa.uuid import UUID

# Show output of operations.
a = UUID(int2pmat(2 ** 128 - 1))
b = UUID('12345678901234123456789')
c = UUID(1)
print(a, b, c)
print()
print((a * b))
print((a * b) * b)
print((a * b) * b.t)
print((a * b) * c)

# Check for collisions.
s = {0}
aa = bb = 0
for i in range(100000):
    while aa in s:
        aa = round(random() * 2 ** 128)
    while bb in s:
        bb = round(random() * 2 ** 128)
    a = int2pmat(aa)
    b = int2pmat(bb)
    n = pmat2int(pmat_mult(a, b))
    s.add(aa)
    s.add(bb)
    s.add(n)
    if i > len(s) - 1:
        print(i, a, b, n)
        print('Colision detected!!!!!!!!!!!!!!')
        break
if i == 100000 - 1:
    print('No collisions!', len(s))


# Check general overhead of all uuid ops.
def f():
    a = UUID(int2pmat(2 ** 128 - 1))
    b = UUID('12345678901234123456789')
    (a * b) * b.t


print(timeit(f, number=10000) * 100, 'us')


# Check general overhead of all hash ops.
def f():
    a = Hash(2 ** 128 - 1)
    b = Hash('1234567890123412345678')
    (a * b) / b

f()
print(timeit(f, number=10000) * 100, 'us')
