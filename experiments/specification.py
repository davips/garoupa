#  Copyright (c) 2021. Davi Pereira dos Santos
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
#  part of this work is illegal and unethical regarding the effort and
#  time spent here.

from bigfloat import *
from sympy import isprime

from garoupa.misc.encoding.base import n2id

a16 = tuple("0123456789abcdef")
a16up = tuple("ghijklmnopqrstuv")
a63 = tuple("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_")
a64 = tuple("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-.")
a65 = tuple("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-._")


def dec(string, alphabet):
    rev_alphabet = dict((c, v) for v, c in enumerate(alphabet))
    num = 0
    for char in reversed(string):
        num = num * len(alphabet) + rev_alphabet[char]
    return num


def enc(num, alphabet):
    encoded = ""
    while num:
        num, rem = divmod(num, len(alphabet))
        encoded += alphabet[rem]
    return encoded


# # 5x5 is not a good choice due to:
# p = (16 ** 40) ** (1 / 10)
# print(log(p ** 6) / log(2), p)  # |H1|=2^96 for 5x5 40-digit (bad) p=65536
# p = (16 ** 64) ** (1 / 10)
# print(log(p ** 4) / log(2), p)  # |H|=2^102 for 5x5 64-digit (not good) p=50859008
# p = (16 ** 80) ** (1 / 10)
# print(log(p ** 4) / log(2), p)  # |H|=2^128 for 5x5 80-digit (almost good) p=4294967296

# 4x4 is the choice
for digits in [16, 32, 40, 64]:
    with precision(60):
        n = pow(64 ** digits, 1 / 6)  # |H| is defined by max possible G
        p = None
        for i in range(int(n - 10000), 2 ** 333):
            # Get the largest possible G.
            if isprime(i):
                i4 = i ** 4
                i6 = i4 * i ** 2
                # print((i6 - i4 - i) / 64 ** digits)
                if (i6 - i4 - i) > 64 ** digits:
                    break
                p = i
        if p is None:
            exit()
        # p = 4294967291
        gbits = log(p ** 6) / log(2)
        # print(f"p={p}\t\t|G|={gbits}")
        # print(pow(p ** 6 - p ** 4, 1 / digits), f": min. alphabet to fit G\\H into {digits} digits")
        # print(64 ** 2 * pow(16, digits - 3) / (p ** 4 - p), "<- representable / |H\\Z|")
        # print(pow(64, digits) / (p ** 6 - p ** 4), "<- representable / |G\\H|")

        # relevant digests
        digits_b16a = digits // 4 - 1
        digits_b16 = digits - 3
        res, rem = divmod(p ** 4 - p, 16 ** digits_b16)
        print(f"{digits}: Group({p}, "
              f"{p ** 4}, "
              f"{p ** 6}, "
              f"{digits}, "
              f"{3 * digits // 4}, "
              f"\n\"{n2id(1, digits, p)}\", \"{n2id(p - 1, digits, p)}\","
              f"\n\"{n2id(p, digits, p)}\", \"{n2id(p ** 4 - 1, digits, p)}\","
              f"\n\"{n2id(p ** 4, digits, p)}\", \"{n2id(p ** 6 - 1, digits, p)}\")"
              )
        print()
