# Timing tradeoff startup/repetition
from timeit import timeit

from garoupa import Hash

t = timeit(lambda: Hash(12431434) * Hash(895784), number=1)
print("Normal warm up time:", round(t, 2), "s")
# ...

t = timeit(lambda: Hash(12431434) * Hash(895784), number=100000)
print("Normal time:", round(t * 10, 2), "us")
# ...

t = timeit(lambda: Hash(12431434, compiled=True) * Hash(895784, compiled=True), number=1)
print("Compiled warm up time:", round(t, 2), "s")
# ...

t = timeit(lambda: Hash(12431434, compiled=True) * Hash(895784, compiled=True), number=100000)
print("Compiled time:", round(t * 10, 2), "us")
# ...
