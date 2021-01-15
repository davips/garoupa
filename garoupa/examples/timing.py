from timeit import timeit

from garoupa.hash import Hash

t = timeit(lambda: Hash(12431434) * Hash(895784), number=1)
print("normal warm up", round(t, 2), "s")

t = timeit(lambda: Hash(12431434) * Hash(895784), number=1000000)
print("normal", round(t, 2), "us")

print("---------------------------")
t = timeit(lambda: Hash(12431434, compiled=True) * Hash(895784, compiled=True), number=1)
print("compiled warm up", round(t, 2), "s")

t = timeit(lambda: Hash(12431434, compiled=True) * Hash(895784, compiled=True), number=1000000)
print("compiled", round(t, 2), "us")
