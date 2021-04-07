# Detect identity after many repetitions
import operator
from datetime import datetime
from functools import reduce
from math import log
from sys import argv

from garoupa.algebra.dihedral import D

example = not True

primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
          643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
          947, 953, 967, 971, 977, 983, 991, 997, 1009]

limit, sample = 1_000_000_000, 100_000_000_000
if example:
    limit, sample = 30, 100
    G = reduce(operator.mul, [D(n) for n in primes[:5]])
elif argv[1] == "p128":
    G = reduce(operator.mul, [D(n) for n in primes[:22]])
elif argv[1] == "p256":
    G = reduce(operator.mul, [D(n) for n in primes[:38]])
elif argv[1] == "128":
    G = reduce(operator.mul, [D(n) for n in range(5, 51, 2)])
else:
    G = reduce(operator.mul, [D(n) for n in range(5, 86, 2)])

print(f"{G.bits} bits   Pc: {G.comm_degree}")
print("--------------------------------------------------------------")
for hist in G.sampled_orders(sample=sample, limit=limit):
    bad = sum(v for k, v in hist.items() if k[0] < limit)
    tot = sum(hist.values())
    print(f"\nbits: {log(G.order, 2):.2f}  Pc: {G.comm_degree or -1:.2e}   a^<{limit}=0: {bad}/{tot} = {bad / tot:.2e}",
          G, datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print(hist)
# ...
