# Check distribution of collisions after multiplication.
from timeit import timeit

import fastrand
import psutil as psutil

# Check collisions. (seems unnecessary, due to the nature of the mult op.
from garoupa.hash import Hash
from garoupa.hashmath import int2bm, bmm, bm2int

s, re = {}, {}
lim = 2 ** 128 - 1
m = lim  # factorial(35) - 5000000
n = lim - 10_000_000  # factorial(35) - 2
c, t = 0, 0
for i in range(lim, lim - 10, -1):
    while True:
        ii = ((fastrand.xorshift128plus() + 2 ** 63) << 64) + (fastrand.xorshift128plus() + 2 ** 63)
        if ii not in s:
            break
        print("another ii", ii)
    mi = int2bm(ii)
    s[ii] = s.get(ii, 0) + 1
    c += 1
    for j in range(m, n, -1):
        while True:
            jj = ((fastrand.xorshift128plus() + 2 ** 63) << 64) + (fastrand.xorshift128plus() + 2 ** 63)
            if jj not in s:
                break
            print("another jj", jj)
        c += 1
        mj = int2bm(jj)
        r = bm2int(bmm(mi, mj))
        re[r] = re.get(r, 0) + 1
        s[jj] = s.get(jj, 0) + 1
        t += 1

        if (j - n) % round((m - n) * 0.005) == 0:
            mem = psutil.virtual_memory()[2]
            print(100 * (j - n) / (m - n), '%   memory used:', mem, '%')
            print('unicos:', len(s), 'max/min:', max(s.values()), min(s.values()),
                  'tests:', t, 'collision rate:', 100 * (t - len(re)) / t, '%')
            print()
            if mem > 96:
                print('out of memory')
                break


# print(json.dumps(s, indent=4))

