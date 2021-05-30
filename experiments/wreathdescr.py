#  Copyright (c) 2021. Gabriel Dalforno and Davi Pereira-Santos
#  This file is part of the garoupa project.
#  Please respect the license - more about this in the section (*) below.
#
#  garoupa is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  garoupa is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with garoupa.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.

import math
import operator
from functools import reduce
import matplotlib.pyplot as plt

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
          643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
          947, 953, 967, 971, 977, 983, 991, 997, 1009]


# Order of the group W2,p
def orderW2(p: int) -> int:
    return p ** (p + 1)


# Probability of commutation of W2,p
def PW2(p: int) -> float:
    return (p ** 2 + p ** (p - 1) - 1) / (p ** (2 * (p + 1)))


# Order histogram of W2,p
def order_histW2(p: int) -> dict:
    return {
        1: 1,
        p: (2 * p - 1) * (p ** (p - 1)) - 1,
        p ** 2: ((p - 1) ** 2) * (p ** (p - 1))
    }


# Least Common Multiple
def lcm(a: int, b: int) -> int:
    return int((a * b) / math.gcd(a, b))


# Order histogram of G1xG2
def direct_product_order_hist(G1: dict, G2: dict) -> dict:
    hist = {}
    for k1 in G1.keys():
        for k2 in G2.keys():
            key = lcm(k1, k2)
            hist[key] = hist.get(key, 0) + G1[k1] * G2[k2]
    return hist


# Order of the group G
def orderG(primes: list) -> int:
    order = 1
    for p in primes:
        order *= orderW2(p)
    return order


# Probability of commutation of G
def PG(primes: list) -> float:
    prob = 1
    for p in primes:
        prob *= PW2(p)
    return prob


# Order histogram of G
def order_histG(primes: list) -> dict:
    initial = direct_product_order_hist(
        order_histW2(primes[0]), order_histW2(primes[1])
    )
    if len(primes) > 2:
        for p in primes[2:]:
            initial = direct_product_order_hist(initial, order_histW2(p))
    return initial


# Number of irreducible representations of W2,p
def k(n: int, p: int) -> int:
    if n == 1:
        return p
    return (1 / p) * (k(n - 1, p) * p ** 2 + k(n - 1, p) ** p - k(n - 1, p))


# Order of the group W2,p
def order(n: int, p: int) -> int:
    return p ** ((p ** n - 1) // (p - 1))


# Probability of commutation of W2,p
def Pc(n: int, p: int) -> float:
    return k(n, p) / order(n, p) ** 2


# Order histogram of W2,p
def order_hist(p: int) -> dict:
    return {
        1: 1,
        p: (2 * p - 1) * (p ** (p - 1)) - 1,
        p ** 2: ((p - 1) ** 2) * (p ** (p - 1))
    }


###########################################################################
#######  Full characterization of G = W2 x W3 x W5 x W7 x W11 x W13 x ...
###########################################################################
bitslimits = iter(192 * i for i in range(1, 5))
bitslimit = next(bitslimits)
for take in range(6, 9):  # "128"-bit: 6; "256"-bit: 8
    ws = primes[:take]
    N = reduce(operator.mul, (a ** (a + 1) for a in ws))
    bits = math.log(N, 2)
    if bits > bitslimit:
        bitslimit = next(bitslimits)
        continue
    print()
    print("----------------------------------------------------------")
    print(f"G = W2 x W... x W{ws[-1]}", N)
    print(f"Number of bits: {bits}.  Compatible with: {bitslimit} bits")
    print(f"Minimum order for a never-trivial element: {reduce(operator.mul, ws)}")
    P = 1
    for prime in ws:
        P *= Pc(2, prime)
    print(f"Probability of commutation: {P}")

    G = reduce(direct_product_order_hist, map(order_hist, ws))
    sorted_keys = sorted(G.keys())
    G = dict({str(key): G[key] for key in sorted_keys})

    plt.style.use("dark_background")
    plt.title(f"G = W2 x W... x W{ws[-1]}")
    plt.bar(G.keys(), G.values(), color="blue")
    plt.yscale("log")
    plt.xticks([
        0,
        int(0.5 * len(sorted_keys)),
        int(0.65 * len(sorted_keys)),
        int(0.75 * len(sorted_keys)),
        int(0.85 * len(sorted_keys)),
        int(0.95 * len(sorted_keys))
    ])
    plt.xlabel("Order")
    plt.ylabel("#Elements")
    plt.show()

    t = sum(G.values())
    acc = 0
    for key, v in G.items():
        acc += v
        p = (t - acc) / t
        # if p < 0.999_999_999_999_999_999:
        # if key > 1_000_000_000_000:
        # if key > 100_000_000:
        if int(key) > 1_000_000:
            print(f"{p:.21e} {int(key):_}", acc, flush=True)
            break

    # 99.99999999999998%    154_040_315    garante ordem acima de 154M (1 em 10^18)
    # 99.9999999731%      2_155_487_205
    # 99.997%         1_000_571_521_950
    # 98.32%      1_002_681_290_940_420    repetição sem limites para 98% dos elementos (10^15 repetições)

print()
for pi in primes[:10]:
    o = order(2, pi)
    print(f"|W2,{pi:<2}|: {o:<60_}    {math.log(o, 2):<28} bits")
    if pi == primes[4]:
        print('-----------')
