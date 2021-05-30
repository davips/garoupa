#  Copyright (c) 2021. Gabriel Dalforno
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
from collections import OrderedDict
from math import gcd

import matplotlib.pyplot as plt


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
    return int((a * b) / gcd(a, b))


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
    return p ** ((p ** n - 1) / (p - 1))


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
#######  Full characterization of G = W2 x W3 x W5 x W7 x W11 x W13  ######
###########################################################################
N = 2 ** 3 * 3 ** 4 * 5 ** 6 * 7 ** 8 * 11 ** 12 * 13 ** 14
print("Full characterization of G = W2 x W3 x W5 x W7 x W11 x W13")
print("----------------------------------------------------------")
print(f"Number of elements: 2^3 x 3^4 x 5^6 x 7^8 x 11^12 x 13^14")
print(f"Number of bits: {math.log(N, 2)}")
del N
print(f"Minimum order for a never-trivial element: {2 * 3 * 5 * 7 * 11 * 13}")

P = 1
for p in (2, 3, 5, 7, 11, 13):
    P *= Pc(2, p)
print(f"Probability of commutation: {P}")
del P

W2xW3 = direct_product_order_hist(order_hist(2), order_hist(3))
W2xW3xW5 = direct_product_order_hist(W2xW3, order_hist(5))
del W2xW3
W2xW3xW5xW7 = direct_product_order_hist(W2xW3xW5, order_hist(7))
del W2xW3xW5
W2xW3xW5xW7xW11 = direct_product_order_hist(W2xW3xW5xW7, order_hist(11))
del W2xW3xW5xW7
G = direct_product_order_hist(W2xW3xW5xW7xW11, order_hist(13))
del W2xW3xW5xW7xW11

sorted_keys = sorted(G.keys())
G = OrderedDict({str(key): G[key] for key in sorted_keys})

plt.style.use("dark_background")
plt.title("G = W2 x W3 x W5 x W7 x W11 x W13")
plt.bar(G.keys(), G.values(), color="blue")
plt.xticks(
    [
        0,
        int(0.5 * len(sorted_keys)),
        int(0.65 * len(sorted_keys)),
        int(0.75 * len(sorted_keys)),
        int(0.85 * len(sorted_keys)),
        int(0.95 * len(sorted_keys))
    ]
)
plt.xlabel("Order")
plt.ylabel("#Elements")
plt.show()
