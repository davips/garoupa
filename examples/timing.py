# Timing tradeoff startup/repetition
from timeit import timeit

from garoupa import Hash


def f():
    return Hash(12431434) * Hash(895784)


def f_compiled():
    return Hash(12431434, compiled=True) * Hash(895784, compiled=True)


t = timeit(f, number=1)
print("Normal warm up time:", round(t, 2), "s")
"""
Normal warm up time: 0.0 s
"""

t = timeit(f, number=100000)
print("Normal time:", round(t * 10, 2), "us")
"""
Normal time: 52.25 us
"""

t = timeit(f_compiled, number=1)
print("Compiled warm up time:", round(t, 2), "s")
"""
Compiled warm up time: 2.28 s
"""

t = timeit(f_compiled, number=100000)
print("Compiled time:", round(t * 10, 2), "us")
"""
Compiled time: 7.59 us
"""
