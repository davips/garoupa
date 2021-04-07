# Detect identity after many repetitions
import operator
from datetime import datetime
from functools import reduce
from math import log

from garoupa.algebra.dihedral import D
from garoupa.algebra.symmetric import S

limit = 100_000_000
step = 1
sample = 100_000_000_000
Ds = reduce(operator.mul, [D(n) for n in range(5, 49, 2)])
Ss = reduce(operator.mul, [S(n) for n in range(3, 5, 1)])
# G = Ds * Ss
G = reduce(operator.mul, [D(2**i) for i in range(6, 28)])
print(f"bits: {log(G.order, 2):.2f}\tPc: {G.comm_degree or -1:.2e}", G)
print("--------------------------------------------------------------")
for hist in G.sampled_orders(sample=sample, limit=limit):
    bad = sum(v for k, v in hist.items() if k[0] < limit)
    tot = sum(hist.values())
    print(f"\nbits: {log(G.order, 2):.2f}  Pc: {G.comm_degree or -1:.2e}   a^<{limit}=0: {bad}/{tot} = {bad / tot:.2e}",
          G, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print(hist)
