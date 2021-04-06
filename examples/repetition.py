# Detect identity after many repetitions

from pprint import pprint
from timeit import timeit

import pathos.multiprocessing as mp
from lange import gp

from garoupa.algebra.cyclic import Z
from garoupa.algebra.matrix import M
from garoupa.algebra.matrix.m128bit import M128bit
from garoupa.algebra.symmetric import S

for hist in S(34).sampled_orders():
    print(hist)
