# Tendence of commutativity on Mn
from itertools import chain

from garoupa.algebra.matrix.m import M
from garoupa.algebra.matrix.m8bit import M8bit


def traverse(G):
    i, count = G.order, G.order
    for idx, a in enumerate(G.sorted()):
        for b in list(G.sorted())[idx + 1:]:
            if a * b == b * a:
                count += 2
            i += 2
    print(f"|{G}| = ".rjust(20, ' '),
          f"{G.order}:".ljust(10, ' '),
          f"{count}/{i}:".rjust(15, ' '), f"  {G.bits} bits",
          f"\t{100 * count / i} %", sep="")


M1_4 = map(M, range(1, 5))
for G in chain(M1_4):
    traverse(G)
"""
   |M1%2| = 1:                   1/1:  0.0 bits	    100.0 %
   |M2%2| = 2:                   4/4:  1.0 bits	    100.0 %
   |M3%2| = 8:                 40/64:  3.0 bits	    62.5 %
   |M4%2| = 64:            1024/4096:  6.0 bits	    25.0 %
  |M8bit| = 256:         14848/65536:  8.0 bits	    22.65625 %
   |M5%2| = 1024:      62464/1048576:  10.0 bits	5.95703125 %
"""

for G in map(M, range(5, 9)):
    G.sampled_comm_degree(chunksize=10000, nchunks=2)
"""
    1202/19771:	~6.079611552273532 %
    1214/20000:	~6.07 %
M5%2    1214/20000:	~6.07 %
     168/19913:	~0.8436699643449003 %
     169/20000:	~0.845 %
M6%2     169/20000:	~0.845 %
      11/19943:	~0.05515719801434087 %
      11/20000:	~0.055 %
M7%2      11/20000:	~0.055 %
       1/19972:	~0.005007009813739235 %
       1/20000:	~0.005 %
M8%2       1/20000:	~0.005 %
"""

# Other, longer, results.
"""
All Mi here are Mi%2:
     |M1| = 1:                        1/1:  0 bits	100.0 %
     |M2| = 2:                        4/4:  1 bits	100.0 %
     |M3| = 8:                      40/64:  3 bits	62.5 %
     |M4| = 64:                 1024/4096:  6 bits	25.0 %
  |M8bit| = 256:              14848/65536:  8 bits	22.65625 %
     |M5| = 1024:           62464/1048576:  10 bits	5.95703125 %
     |M6| = 32768:       839693/100000000:  15.0 bits ~0.839693 %
     |M7| = 2097152:          683/1000000:  21 bits	~0.0683 %
     |M8| = 268435456:         30/1000000:  28 bits	~0.003 %
     |M9| = 68719476736:        1/1000000:  36 bits	~0.0001 %
    |M10| = 35184372088832:     0/1000000:  45 bits	~0.0 %

...
Approximated worst case (worst in 10 long runs, so it is unfavorably biased):
     |M9| = 68719476736:      44/48420000:  36 bits ~9.087154068566707e-05 %
    |M10| = 35184372088832:    2/38310000:  45 bits ~5.220569042025581e-06 %
"""
