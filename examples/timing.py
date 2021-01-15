# Timing tradeoff startup/repetition
from timeit import timeit

from garoupa import Hash


def f():
    return Hash(12431434) * Hash(895784)


def f_compiled():
    return Hash(12431434) * Hash(895784)


t = timeit(f, number=1)
print("Normal warm up time:", round(t, 2), "s")
# ...

t = timeit(lambda: f, number=100000)
print("Normal time:", round(t * 10, 2), "us")
# ...

t = timeit(f_compiled, number=1)
print("Compiled warm up time:", round(t, 2), "s")
# ...

t = timeit(f_compiled, number=100000)
print("Compiled time:", round(t * 10, 2), "us")
# ...
