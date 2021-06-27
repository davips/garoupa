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
from decimal import Decimal, getcontext
from functools import reduce
import matplotlib.pyplot as plt
import numpy

from experiments.symmetricdescr import order_histS
from garoupa.algebra.symmetric import S

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
    return (p ** 2 + p ** (p - 1) - 1) / orderW2(p)


# Order histogram of W2,p
def order_histW2(p: int) -> dict:
    return {
        1: 1,
        p: (2 * p - 1) * (p ** (p - 1)) - 1,
        p ** 2: ((p - 1) ** 2) * (p ** (p - 1))
    }


# Least Common Multiple
def lcm(a: int, b: int) -> int:
    return (a * b) // math.gcd(a, b)


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


def median(values, weights):
    acc = 0
    s = sum(weights)
    for w, v in zip(weights, values):
        acc += w
        if acc >= s // 2:
            break
    return v


def wmean0(values, weights):
    u = sum(w * v for w, v in zip(weights, values)) // sum(weights)
    weights = [w for w, v in zip(weights, values) if v < u]
    s = int(Decimal(sum(w * ((v - u) ** 2) for w, v in zip(weights, values)) // sum(weights)).sqrt())
    return u, s


###########################################################################
#######  Full characterization of G = W2 x W3 x W5 x W7 x W11 x W13 x ...
###########################################################################
for take in range(1, 13):  # "128"-bit: 6; "256"-bit: 8
    ws = primes[:take]
    dup = None
    sn = 0 #S(15)
    print()
    print("----------------------------------------------------------")
    print(f"G = W2 x W... x W{ws[-1]} x W{dup} x {sn}")
    print(f"Minimum order for a never-trivial element: {reduce(operator.mul, ws)}")

    # Add a duplicate wreath to make |G| near 2^384 (and also Pc as a side effect).
    if dup:
        ws = ws + [dup]

    N = reduce(operator.mul, (order(2, a) for a in ws))
    G = reduce(direct_product_order_hist, map(order_hist, ws))
    P = 1
    if sn:
        N *= sn.order
        P *= sn.comm_degree
        G = direct_product_order_hist(G, order_histS(sn.n))
    bits = math.log(N, 2)
    base = 64
    bitsbase = int(math.log(base, 2))
    mmcbits = lcm(8, bitsbase)
    bitslimit = (math.ceil(bits) // mmcbits + 1) * mmcbits
    print(f"bits: {bits}.  Nearest: {bitslimit} bits     {bitslimit / bitsbase} digits    {bitslimit / 8} bytes")

    for prime in ws:
        P *= Pc(2, prime)
    print(f"Probability of commutation: {P}")

    sorted_keys = sorted(G.keys())
    G = dict({str(key): G[key] for key in sorted_keys})

    # plt.style.use("dark_background")
    # plt.title(f"G = W2 x W... x W{ws[-1]}")
    # plt.bar(G.keys(), G.values(), color="blue")
    # plt.yscale("log")
    # plt.xticks([
    #     0,
    #     int(0.5 * len(sorted_keys)),
    #     int(0.65 * len(sorted_keys)),
    #     int(0.75 * len(sorted_keys)),
    #     int(0.85 * len(sorted_keys)),
    #     int(0.95 * len(sorted_keys))
    # ])
    # plt.xlabel("Order")
    # plt.ylabel("#Elements")
    # plt.show()

    t = sum(G.values())
    acc = 0
    foi = False
    vals = []
    weights = []
    for key, v in G.items():
        acc += v
        p = (t - acc) / t
        # if int(key) > 10000000:
        if t // acc < 10 ** 2:
            if not foi:
                print(f"{p:.58e}    1/{t // acc:.1e}   reps allowed < {int(key):_}", flush=True)
            foi = True
            if foi:
                vals.append(int(key))
                weights.append(v)
    if foi:
        print(median(vals, weights), flush=True)

    # Results for W2 ... W29 !!!
    # 99.99999999999998%    154_040_315    garante ordem acima de 154M (1 em 10^18)
    # For comparison, it is the same probability of MD5 resulting in a collision after 2.6 × 10^10 hashes.

    # 99.9999999731%      2_155_487_205
    # 99.997%         1_000_571_521_950
    # 98.32%      1_002_681_290_940_420    repetição sem limites para 98% dos elementos (10^15 repetições)

# for pi in primes[:10]:
#     o = order(2, pi)
#     print(f"|W2,{pi:<2}|: {o:<60_}    {math.log(o, 2):<28} bits")
#     if pi == primes[4]:
#         print('-----------')

"""
base-64
64 digits

----------------------------------------------------------
G = W2 x W... x W19 x WNone
Minimum order for a never-trivial element: 9699690
Number of bits: 297.5824748376703.  Compatible with: 384 bits
Probability of commutation: 1.3674814255755696e-103
9.999999996048327677300e-01 1_000_692 150671822625249681076853911937223128978523303906569452603253481697914844967919624

----------------------------------------------------------
G = W2 x W... x W19 x W19
Minimum order for a never-trivial element: 9699690
Number of bits: 382.541025106542.  Compatible with: 384 bits
Probability of commutation: 1.0077254229078475e-131
9.999999999594980648610e-01 1_000_692 580495779297195110573587781192980641999361007778557671425361505690796073985707529525485581793053974240520

----------------------------------------------------------
G = W2 x W... x W19 x WNone x S25
Minimum order for a never-trivial element: 9699690
Number of bits: 381.2639884465455.  Compatible with: 384 bits
Probability of commutation: 1.891290625481518e-125
9.999999999800267547201e-01 1_000_692 118125654385623329379021240469595465429499359410849169418929426942183875146215174300147519604239488439424

"""

"""
base-128

G = W2 x W... x W23 x W0 x 0
Minimum order for a never-trivial element: 223092870
bits: 406.1479617830386.  Nearest: 448 bits     64.0 digits    56.0 bytes
Probability of commutation: 5.382669313684215e-139
9.9999999999932764893628700519911944866180419921875000000000e-01    1/1.5e+12   reps allowed < 10_013_850
1185010205829450

G = W2 x W... x W23 x W0 x S15
Minimum order for a never-trivial element: 223092870
bits: 446.3981022529212.  Nearest: 448 bits     64.0 digits    56.0 bytes
Probability of commutation: 8.171900583922535e-149
9.9999999999996469490781692002201452851295471191406250000000e-01    1/2.8e+13   reps allowed < 10_006_920
1659014288161230

G = W2 x W... x W23 x W10 x 0
Minimum order for a never-trivial element: 223092870
bits: 442.6891708267996.  Nearest: 448 bits     64.0 digits    56.0 bytes
Probability of commutation: 5.382669846568477e-152
1.0000000000000000000000000000000000000000000000000000000000e+00    1/1.3e+20   reps allowed < 10_013_850
2619496244465100
"""
