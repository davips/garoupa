#  Copyright (c) 2020. Davi Pereira dos Santos
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
#  Relevant employers or funding agencies will be notified accordingly.

from dataclasses import dataclass
from functools import lru_cache
from math import factorial

from garoupa.decorator import classproperty


def int2pmat(number, side=35):
    """Convert number into permutation matrix.

    Pads to side. If None, no padding.

    Parameters
    ----------
    number
    side

    Returns
    -------

    """
    available = list(range(side))
    mat = []
    for i in range(side, 0, -1):
        number, r = divmod(number, i)
        mat.append(available.pop(r))
    mat.extend(available)
    return mat


def pmat2int(matrix):
    """Convert permutation matrix to number.

    Parameters
    ----------
    matrix

    Returns
    -------

    """
    radix = len(matrix)
    available = list(range(radix))
    i = 1
    res = 0
    for row in matrix:
        idx = available.index(row)
        del available[idx]
        res += idx * i
        i *= radix
        radix -= 1
    return res


def pmat_mult(a, b):
    """Multiply two permutation matrices (of the same size?).

    Parameters
    ----------
    a
        list of positive integers plus zero
    b
        list of positive integers plus zero

    Returns
    -------

    """
    return [a[x] for x in b]


def pmat_transpose(m):
    """Transpose a permutation matrix (square?).

     https://codereview.stackexchange.com/questions/241511/how-to-efficiently-fast-calculate-the-transpose-of-a-permutation-matrix-in-p/241524?noredirect=1#comment473994_241524

    Parameters
    ----------
    m
        list of positive integers plus zero

    Returns
    -------
        list of positive integers plus zero
    """
    n = len(m)
    tr_ls = [0] * n

    for l in m:
        tr_ls[n - 1 - m[l]] = n - 1 - l

    return tr_ls


# Useful, but not really used functions. ====================================


@lru_cache()
def fact(n):
    """Cached factorial to speed up repetitive calls."""
    return factorial(n)


def print_binmatrix(m):
    """Print a binary matrix.

    Parameters
    ----------
    m
        list of positive integers plus zero

    Returns
    -------
        None
    """
    for row in m:
        print(" ".join(format(2 ** row, f"0{len(m)}b")), "  ", row)


def int2fac(number):
    """Convert decimal into factorial numeric system. Left-most is LSB.

    Parameters
    ----------
    number

    Returns
    -------

    """
    i = 2
    res = [0]
    while number > 0:
        number, r = divmod(number, i)
        res.append(r)
        i += 1
    return res


def fac2pmat(digits):
    """Convert factoradic number to permutation matrix.

    Parameters
    ----------
    digits

    Returns
    -------

    """
    available = list(range(len(digits)))
    mat = []
    for digit in reversed(digits):
        mat.append(available.pop(digit))
    return mat


def pmat2fac(matrix):
    """Convert permutation matrix to factoradic number.

    Parameters
    ----------
    matrix

    Returns
    -------

    """
    available = list(range(len(matrix)))
    digits = []
    for row in matrix:
        idx = available.index(row)
        del available[idx]
        digits.append(idx)
    return list(reversed(digits))


def fac2int(digits):
    """Convert factorial numeric system into decimal. Left-most is LSB.

    Parameters
    ----------
    digits

    Returns
    -------

    """
    radix = 1
    i = 1
    res = 0
    for digit in digits[1:]:
        res += digit * i
        radix += 1
        i *= radix
    return res


def lazyhash(msg: bytes, length=16):
    """Algebraic hash function: incremental/decremental, associative etc.
    Provide all non-abelian group niceties over permutation matrix multiplication."""
    side = unfac(2 ** (length * 8)) - 1
    r = int2pmat(255 - msg[0], side=side)
    for b in msg:
        r = pmat_mult(r, int2pmat(b, side=side))  # HINT: a byte is just an int for Python.
    return pmat2int(r).to_bytes(length, byteorder="little")


def bytes2int(byts):
    n = 0
    idx = 0
    while idx < len(byts):
        n += byts[idx] * pow(256, idx)
        idx += 1
    return n


def int2bytes(num):
    byts = []
    res = num
    while res > 0:
        res, rem = divmod(res, 256)
        byts.append(rem.to_bytes(1, "little")[0])
    return byts


def unfac(n):
    tofac = 1
    res, rem = n, 1
    while res > 0:
        tofac += 1
        res, rem = divmod(res, tofac)
    if tofac < 6:  # 6x6 to represent at least 1 byte as key
        tofac = 6
    return tofac


def lazyencrypt(msg, key):
    print("not finished!")
    n = bytes2int(key)
    side = unfac(n)
    keymat = int2pmat(n, side=side)
    t = []
    resbytes = [0] + list(msg[:len(key) - 1])
    for l in msg:
        resbytes = resbytes[1:] + [l]
        resmat = int2pmat(bytes2int(resbytes), side=side)
        resmat = pmat_mult(resmat, keymat)
        resbytes = int2bytes(pmat2int(resmat))
        print(l, resbytes)

        # use only first byte of resulting matrix for output, the rest becomes the next key
        t.append(resbytes[0])
    return bytes(t + resbytes[1:])


def lazydecrypt(encrypted, key):
    print("not finished!")
    n = bytes2int(key)
    side = unfac(n)
    keymat = int2pmat(n, side=side)
    t = []
    i = len(encrypted) - len(key)
    pref = list(encrypted[len(key) + 1:])
    while i >= 0:
        print(i, "pref", pref, encrypted)
        seg = [encrypted[i]] + pref
        segmat = int2pmat(bytes2int(seg), side=side)
        resmat = pmat_mult(segmat, pmat_transpose(keymat))
        resbytes = int2bytes(pmat2int(resmat))
        print('i', i, resbytes)

        # use only first byte of resulting matrix for output, the rest becomes the next key
        t.append(resbytes[-1])
        i -= 1
        pref = resbytes[:-1]
    return bytes(reversed(t + pref))


@dataclass(frozen=False)
class M:
    """A class to ease playing around with permutation matrix operations.

    'l' is the list representation of this matrix."""

    n: int = None
    m: list = None
    side: int = 35
    _t = None

    def __post_init__(self):
        if self.m is None:
            self.m = int2pmat(self.n, self.side)
        elif self.n is None:
            self.n = pmat2int(self.m)
        else:
            raise Exception(f"Cannot set both args... n:{self.n} l:{self.m}!")

    # @classmethod
    @classproperty
    @lru_cache()
    def z(cls):
        return M(n=cls.last)

    # @classmethod
    @classproperty
    @lru_cache()
    def i(cls):
        return M(0)

    @staticmethod
    @lru_cache()
    def _lazy_t(l):
        return M(m=pmat_transpose(l), side=len(l))

    @staticmethod
    @lru_cache()
    def _lazy_last(side):
        return factorial(side) - 1

    @property
    def t(self):
        if self._t is None:
            self._t = self._lazy_t(tuple(self.m))
        return self._t

    # @classmethod
    @classproperty
    @lru_cache()
    def last(cls):
        return cls._lazy_last(cls.side)

    def __mul__(self, other):
        return M(m=pmat_mult(self.m, other.m), side=self.side)

    def __truediv__(self, other):
        return M(m=pmat_mult(self.m, other.t), side=self.side)

    def __add__(self, other):
        n = pmat2int(self.m) + pmat2int(other.m)
        return M(n % (self.last + 1), side=self.side)
