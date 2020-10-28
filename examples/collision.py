# Check distribution of collisions after multiplication.
import json
from math import factorial
import random

import fastrand
import psutil as psutil

from cruipto.linalg import pmat_mult, pmat2int, int2pmat

# To check collisions. (seems unnecessary, due to the nature of the mult op.
s = {}
t = {}
lim = factorial(35) - 1
m = lim  # factorial(35) - 5000000
n = lim - 10_000_000  # factorial(35) - 2
c = 0
for i in range(lim, lim - 10, -1):
    ii = random.randrange(lim)
    mi = int2pmat(ii)
    for j in range(m, n, -1):
        jj = random.randrange(lim)
        c += 1
        mj = int2pmat(jj)
        r = pmat2int(pmat_mult(mi, mj))
        s[r] = s.get(r, 0) + 1

        if (j - n) % round((m - n) * 0.005) == 0:
            mem = psutil.virtual_memory()[2]
            print(100 * (j - n) / (m - n), '%   memory used:', mem, '%')
            print('unicos:', len(s), 'max/min:', max(s.values()),
                  min(s.values()),
                  'tests:', c, 'collision rate:', 100 * (c - len(s)) / c, '%')
            print()
            if mem > 96:
                print('out of memory')
                break

# print(json.dumps(s, indent=4))
