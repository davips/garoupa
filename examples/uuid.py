#  Copyright (c) 2020. Davi Pereira dos Santos
#      This file is part of the cruipto project.
#      Please respect the license. Removing authorship by any means
#      (by code make up or closing the sources) or ignoring property rights
#      is a crime and is unethical regarding the effort and time spent here.
#      Relevant employers or funding agencies will be notified accordingly.
#
#      cruipto is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      cruipto is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with cruipto.  If not, see <http://www.gnu.org/licenses/>.
#

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

fac = int2fac(2 ** 128 + 3214134)

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
