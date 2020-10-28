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
