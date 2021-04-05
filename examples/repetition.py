# Detect identity after many repetitions

from pprint import pprint
from timeit import timeit

import pathos.multiprocessing as mp
from lange import gp

from garoupa.algebra.matrix import M
from garoupa.algebra.matrix.m128bit import M128bit


def g(le):
    print("fork")
    # for le in gp[1000, 1500, ...]:
    s = {}

    def f():
        for l in range(11, 19):
            G = M(l) if l < 18 else M128bit()
            z = G.identity
            print(G, G.cells, sep="\t", end="\t")
            for j in range(3):
                t = 1
                a = ~G
                r = a
                for i in range(int(le)):
                    r *= a
                    t += 1
                    if r == z:
                        s[str(G)] = t, a.i
                        break
            print(t)
        pprint(s)

    print()
    print(timeit(f, number=1))


mp.ProcessingPool().map(g, gp[1000, 1500, ..., 999_999_999_999])
