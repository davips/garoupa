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
primes = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101
]


def prime_zeta(N: int, s: int) -> float:
    S = 0
    for i in range(N):
        S += 1 / (primes[i] ** s)
    return S


def prob_fail(prime_subset: list) -> float:
    P = 0
    for p in prime_subset:
        P += 1 / (p ** (p + 1))
    return P


# Assume we chose prime_subset = [2, 3, 5, 7]
prime_subset = [2, 3, 5, 7]

# Let's calculate the probability of failure
pf = prob_fail(prime_subset)

# Let's calculate now the prime zeta function for s = 2+1
pzf = prime_zeta(len(primes), min(prime_subset) + 1)

# Note that the prob_fail < prime_zeta
print(f"pf = {pf} < {pzf} = pzf")

# Now let's change the prime_subset to [3, 5, 7], then repeating the process
prime_subset = [3, 5, 7]
pf = prob_fail(prime_subset)
pzf = prime_zeta(len(primes), min(prime_subset) + 1)

# It stills true
print(f"pf = {pf} < {pzf} = pzf")

# Let's change the prime_subset to [5, 7, 11, 13] now
prime_subset = [5, 7, 11, 13]
pf = prob_fail(prime_subset)
pzf = prime_zeta(len(primes), min(prime_subset) + 1)

# The probability of failure is getting smaller but the upper-bound given
# by the zeta function is not good enough anymore, so we need to re-estimate it
print(f"pf = {pf} < {pzf} = pzf")


def prime_zeta_partial(N: int, s: int, upper: int) -> float:
    zeta = prime_zeta(N, s)
    partial = 0
    for i in range(upper):
        partial += 1 / (primes[i] ** s)
    return zeta - partial


# Going back to the last prime_subset we have
pzpf = prime_zeta_partial(len(primes), min(prime_subset) + 1, upper=2)

# We got a better approximation by setting the upper-bound of the partial sum
# to 2 (i such that primes[i]=5)
print(f"pf = {pf} < {pzpf} = pzpf")

# One more time, we can change the prime_subset
prime_subset = [7, 11, 13, 17, 23]
pf = prob_fail(prime_subset)
pzpf = prime_zeta_partial(len(primes), min(prime_subset) + 1, upper=3)

# It is very close now as we want
print(f"pf = {pf} < {pzpf} = pzpf")

# What if min prime_set -> "inf"??
prime_subset = [83, 89, 97, 101]
pf = prob_fail(prime_subset)
pzpf = prime_zeta_partial(len(primes), min(prime_subset) + 1, upper=22)

# Both go to zero!
print(f"pf = {pf} < {pzpf} = pzpf")
