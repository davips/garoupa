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
from collections import Counter
from math import factorial, gcd, exp, pi, sqrt

# Calculates all the partitions of Sn
from garoupa.algebra.dihedral import D
from garoupa.algebra.symmetric import S


def accel_asc(n: int) -> list:
    # https://arxiv.org/pdf/0909.2331.pdf
    return list(accel_asc_yield(n))


def accel_asc_yield(n: int) -> list:
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2 * x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[: k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[: k + 1]


# Calculates the lcm of a list
def LCMofArray(a: list) -> int:
    # https://www.codegrepper.com/code-examples/python/least+common+multiple+of+list+in+python
    lcm = a[0]
    for i in range(1, len(a)):
        lcm = lcm * a[i] // gcd(lcm, a[i])
    return lcm


# Calculates the number of conjugated classes for each partition
def conj_class_size(p: list, n: int) -> int:
    counter = Counter(p)
    total = 1
    for key, val in counter.items():
        total *= (key ** val) * factorial(val)
    return factorial(n) // total


# Order of the group Sn
def orderS(n: int) -> int:
    return factorial(n)


# Probability of commutation of Sn
def PS(n: int) -> int:
    return exp((2 * pi * sqrt(n)) / sqrt(3)) / (4 * n * sqrt(3) * factorial(n))


# Sn order histogram
def order_histS(n: int) -> dict:
    ## for n=0 it took 138 seconds to run
    hist = {}
    partitions = accel_asc(n)
    for p in partitions:
        lcm = LCMofArray(p)
        hist[lcm] = hist.get(lcm, 0) + conj_class_size(p, n)
    return hist


# Least Common Multiple
def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


# Order histogram of G1xG2
def direct_product_order_hist(G1: dict, G2: dict) -> dict:
    hist = {}
    for k1 in G1.keys():
        for k2 in G2.keys():
            key = lcm(k1, k2)
            hist[key] = hist.get(key, 0) + G1[k1] * G2[k2]
    return hist


# Order of the group SD
def orderSD(integers: list) -> int:
    order = 1
    for n in integers:
        order *= orderS(n)
    return order


# Probability of commutation of SD
def PSD(integers: list) -> float:
    prob = 1
    for n in integers:
        prob *= PS(n)
    return prob


# Order histogram of SD
def order_histSD(integers: list) -> dict:
    initial = direct_product_order_hist(
        order_histS(integers[0]), order_histS(integers[1])
    )
    if len(integers) > 2:
        for n in integers[2:]:
            initial = direct_product_order_hist(initial, order_histS(n))
    return initial


# G = {k: v for k, v in sorted(list((order_histS(78).items())))}
# # G = {k: v for k, v in sorted(list((D(8)^32).order_hist.items()))}
# t = sum(G.values())
# acc = 0
# print(max(G.keys()))
# print(G)
# for key, v in G.items():
#     acc += v
#     p = (t - acc) / t
#     print(p, f"{acc / t:e}", f"1:{t // acc:e}   reps allowed={int(key-1):_}", flush=True)
#     if p < 0.99:
#         break
# print((D(8)^64).comm_degree, S(78).comm_degree)
