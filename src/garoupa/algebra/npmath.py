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
#  part of this work is illegal and is unethical regarding the effort and
#  time spent here.
"""Operations using numpy"""
import numpy as np


def bytes2bm(bs):
    m = np.eye(17)
    m[0, 1] = float(bs[15] & 1)
    m[0, 2] = float(bs[15] >> 1 & 1)
    m[0, 3] = float(bs[15] >> 2 & 1)
    m[0, 5] = float(bs[15] >> 3 & 1)
    m[0, 6] = float(bs[15] >> 4 & 1)
    m[0, 7] = float(bs[15] >> 5 & 1)
    m[0, 8] = float(bs[15] >> 6 & 1)
    m[0, 9] = float(bs[15] >> 7 & 1)
    m[0, 10] = float(bs[14] & 1)
    m[0, 11] = float(bs[14] >> 1 & 1)
    m[0, 12] = float(bs[14] >> 2 & 1)
    m[0, 13] = float(bs[14] >> 3 & 1)
    m[0, 14] = float(bs[14] >> 4 & 1)
    m[0, 15] = float(bs[14] >> 5 & 1)
    m[0, 16] = float(bs[14] >> 6 & 1)
    m[1, 2] = float(bs[14] >> 7 & 1)
    m[1, 3] = float(bs[13] & 1)
    m[1, 5] = float(bs[13] >> 1 & 1)
    m[1, 6] = float(bs[13] >> 2 & 1)
    m[1, 7] = float(bs[13] >> 3 & 1)
    m[1, 8] = float(bs[13] >> 4 & 1)
    m[1, 9] = float(bs[13] >> 5 & 1)
    m[1, 10] = float(bs[13] >> 6 & 1)
    m[1, 11] = float(bs[13] >> 7 & 1)
    m[1, 12] = float(bs[12] & 1)
    m[1, 13] = float(bs[12] >> 1 & 1)
    m[1, 14] = float(bs[12] >> 2 & 1)
    m[1, 15] = float(bs[12] >> 3 & 1)
    m[1, 16] = float(bs[12] >> 4 & 1)
    m[2, 3] = float(bs[12] >> 5 & 1)
    m[2, 5] = float(bs[12] >> 6 & 1)
    m[2, 6] = float(bs[12] >> 7 & 1)
    m[2, 7] = float(bs[11] & 1)
    m[2, 8] = float(bs[11] >> 1 & 1)
    m[2, 9] = float(bs[11] >> 2 & 1)
    m[2, 10] = float(bs[11] >> 3 & 1)
    m[2, 11] = float(bs[11] >> 4 & 1)
    m[2, 12] = float(bs[11] >> 5 & 1)
    m[2, 13] = float(bs[11] >> 6 & 1)
    m[2, 14] = float(bs[11] >> 7 & 1)
    m[2, 15] = float(bs[10] & 1)
    m[2, 16] = float(bs[10] >> 1 & 1)
    m[3, 5] = float(bs[10] >> 2 & 1)
    m[3, 6] = float(bs[10] >> 3 & 1)
    m[3, 7] = float(bs[10] >> 4 & 1)
    m[3, 8] = float(bs[10] >> 5 & 1)
    m[3, 9] = float(bs[10] >> 6 & 1)
    m[3, 10] = float(bs[10] >> 7 & 1)
    m[3, 11] = float(bs[9] & 1)
    m[3, 12] = float(bs[9] >> 1 & 1)
    m[3, 13] = float(bs[9] >> 2 & 1)
    m[3, 14] = float(bs[9] >> 3 & 1)
    m[3, 15] = float(bs[9] >> 4 & 1)
    m[3, 16] = float(bs[9] >> 5 & 1)
    m[4, 5] = float(bs[9] >> 6 & 1)
    m[4, 6] = float(bs[9] >> 7 & 1)
    m[4, 7] = float(bs[8] & 1)
    m[4, 8] = float(bs[8] >> 1 & 1)
    m[4, 9] = float(bs[8] >> 2 & 1)
    m[4, 10] = float(bs[8] >> 3 & 1)
    m[4, 11] = float(bs[8] >> 4 & 1)
    m[4, 12] = float(bs[8] >> 5 & 1)
    m[4, 13] = float(bs[8] >> 6 & 1)
    m[4, 14] = float(bs[8] >> 7 & 1)
    m[4, 15] = float(bs[7] & 1)
    m[4, 16] = float(bs[7] >> 1 & 1)
    m[5, 6] = float(bs[7] >> 2 & 1)
    m[5, 7] = float(bs[7] >> 3 & 1)
    m[5, 8] = float(bs[7] >> 4 & 1)
    m[5, 9] = float(bs[7] >> 5 & 1)
    m[5, 10] = float(bs[7] >> 6 & 1)
    m[5, 11] = float(bs[7] >> 7 & 1)
    m[5, 12] = float(bs[6] & 1)
    m[5, 13] = float(bs[6] >> 1 & 1)
    m[5, 14] = float(bs[6] >> 2 & 1)
    m[5, 15] = float(bs[6] >> 3 & 1)
    m[5, 16] = float(bs[6] >> 4 & 1)
    m[6, 7] = float(bs[6] >> 5 & 1)
    m[6, 8] = float(bs[6] >> 6 & 1)
    m[6, 9] = float(bs[6] >> 7 & 1)
    m[6, 10] = float(bs[5] & 1)
    m[6, 11] = float(bs[5] >> 1 & 1)
    m[6, 12] = float(bs[5] >> 2 & 1)
    m[6, 13] = float(bs[5] >> 3 & 1)
    m[6, 14] = float(bs[5] >> 4 & 1)
    m[6, 15] = float(bs[5] >> 5 & 1)
    m[6, 16] = float(bs[5] >> 6 & 1)
    m[7, 8] = float(bs[5] >> 7 & 1)
    m[7, 9] = float(bs[4] & 1)
    m[7, 10] = float(bs[4] >> 1 & 1)
    m[7, 11] = float(bs[4] >> 2 & 1)
    m[7, 12] = float(bs[4] >> 3 & 1)
    m[7, 13] = float(bs[4] >> 4 & 1)
    m[7, 14] = float(bs[4] >> 5 & 1)
    m[7, 15] = float(bs[4] >> 6 & 1)
    m[7, 16] = float(bs[4] >> 7 & 1)
    m[8, 9] = float(bs[3] & 1)
    m[8, 10] = float(bs[3] >> 1 & 1)
    m[8, 11] = float(bs[3] >> 2 & 1)
    m[8, 12] = float(bs[3] >> 3 & 1)
    m[8, 13] = float(bs[3] >> 4 & 1)
    m[8, 14] = float(bs[3] >> 5 & 1)
    m[8, 15] = float(bs[3] >> 6 & 1)
    m[8, 16] = float(bs[3] >> 7 & 1)
    m[9, 10] = float(bs[2] & 1)
    m[9, 11] = float(bs[2] >> 1 & 1)
    m[9, 12] = float(bs[2] >> 2 & 1)
    m[9, 13] = float(bs[2] >> 3 & 1)
    m[9, 14] = float(bs[2] >> 4 & 1)
    m[9, 15] = float(bs[2] >> 5 & 1)
    m[9, 16] = float(bs[2] >> 6 & 1)
    m[10, 11] = float(bs[2] >> 7 & 1)
    m[10, 12] = float(bs[1] & 1)
    m[10, 13] = float(bs[1] >> 1 & 1)
    m[10, 14] = float(bs[1] >> 2 & 1)
    m[10, 15] = float(bs[1] >> 3 & 1)
    m[10, 16] = float(bs[1] >> 4 & 1)
    m[11, 12] = float(bs[1] >> 5 & 1)
    m[11, 13] = float(bs[1] >> 6 & 1)
    m[11, 14] = float(bs[1] >> 7 & 1)
    m[11, 15] = float(bs[0] & 1)
    m[11, 16] = float(bs[0] >> 1 & 1)
    m[13, 14] = float(bs[0] >> 2 & 1)
    m[13, 15] = float(bs[0] >> 3 & 1)
    m[13, 16] = float(bs[0] >> 4 & 1)
    m[14, 15] = float(bs[0] >> 5 & 1)
    m[14, 16] = float(bs[0] >> 6 & 1)
    m[15, 16] = float(bs[0] >> 7 & 1)
    return m


def int2bm(n):
    return bytes2bm(n.to_bytes(16, byteorder="big"))


def bmm(a, b, mod):
    """unitriangular matrix (modulo) multiplication"""
    return (a @ b) % mod


def bm2int(m):
    n = 0
    b = 0
    for i in range(12):
        if i < 3:
            for j in range(i + 1, 4):
                n += int(m[i, j]) << b
                b += 1
        for j in range(max(5, i + 1), 17):
            n += int(m[i, j]) << b
            b += 1
    for i in range(13, 17):
        for j in range(max(12, i + 1), 17):
            n += int(m[i, j]) << b
            b += 1
    return n


def bminv(m):
    return np.uint8(np.linalg.inv(m) % 2)


def int2bm6(n):
    m = np.eye(6)
    m[0, 1] = float(n >> 14 & 1)
    m[0, 2] = float(n >> 13 & 1)
    m[0, 3] = float(n >> 12 & 1)
    m[0, 4] = float(n >> 11 & 1)
    m[0, 5] = float(n >> 10 & 1)

    m[1, 2] = float(n >> 9 & 1)
    m[1, 3] = float(n >> 8 & 1)
    m[1, 4] = float(n >> 7 & 1)
    m[1, 5] = float(n >> 6 & 1)

    m[2, 3] = float(n >> 5 & 1)
    m[2, 4] = float(n >> 4 & 1)
    m[2, 5] = float(n >> 3 & 1)

    m[3, 4] = float(n >> 2 & 1)
    m[3, 5] = float(n >> 1 & 1)

    m[4, 5] = float(n & 1)
    return m


def bm2int6(m):
    n = (int(m[0, 1]) << 14) + (int(m[0, 2]) << 13) + (int(m[0, 3]) << 12) + (int(m[0, 4]) << 11) + (int(m[0, 5]) << 10)
    n += (int(m[1, 2]) << 9) + (int(m[1, 3]) << 8) + (int(m[1, 4]) << 7) + (int(m[1, 5]) << 6)
    n += (int(m[2, 3]) << 5) + (int(m[2, 4]) << 4) + (int(m[2, 5]) << 3)
    n += (int(m[3, 4]) << 2) + (int(m[3, 5]) << 1)
    n += int(m[4, 5])
    return n


def int2bm8bit(n):
    m = np.eye(5)
    m[0, 2] = float(n >> 7 & 1)
    m[0, 3] = float(n >> 6 & 1)
    m[0, 4] = float(n >> 5 & 1)

    m[1, 2] = float(n >> 4 & 1)
    m[1, 3] = float(n >> 3 & 1)
    m[1, 4] = float(n >> 2 & 1)

    m[2, 3] = float(n >> 1 & 1)
    m[2, 4] = float(n & 1)
    return m


def bm2int8bit(m):
    n = (int(m[0, 2]) << 7) + (int(m[0, 3]) << 6) + (int(m[0, 4]) << 5)
    n += (int(m[1, 2]) << 4) + (int(m[1, 3]) << 3) + (int(m[1, 4]) << 2)
    n += (int(m[2, 3]) << 1) + int(m[2, 4])
    return n


def int2bml(n, l, bits):
    m = np.eye(l)
    b = bits - 1
    for i in range(l - 1):
        for j in range(i + 1, l):
            m[i, j] = float(n >> b & 1)
            b -= 1
    return m


def bm2intl(m, bits):
    n = 0
    l = len(m)
    b = bits - 1
    for i in range(l - 1):
        for j in range(i + 1, l):
            n += int(m[i, j]) << b
            b -= 1
    return n


def int2ml(n, o, l):
    """
    Usage:

    >>> from numpy import uint64
    >>> int2ml(4095, 4, 5)
    array([[1, 3, 3, 3, 3],
           [0, 1, 3, 3, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]], dtype=uint64)
    """
    m = np.eye(l, dtype=np.uint64)
    for i in range(l - 1):
        for j in range(i + 1, l):
            n, rem = divmod(n, o)
            m[i, j] = rem
    return m


def m2intl(m, o):
    """
    Usage:

    >>> from numpy import array, uint8
    >>> m = array([[1, 3, 3, 3, 3],
    ...            [0, 1, 3, 3, 0],
    ...            [0, 0, 1, 0, 0],
    ...            [0, 0, 0, 1, 0],
    ...            [0, 0, 0, 0, 1]], dtype=np.uint64)
    >>> m2intl(m, 4)
    4095
    """
    n = 0
    l = len(m)
    exp = 1
    for i in range(l - 1):
        for j in range(i + 1, l):
            n += int(m[i, j]) * exp
            exp *= o
    return n


#########################################
#########################################
#########################################


def m4m(a, b, mod):
    """unitriangular matrix (modulo) multiplication"""
    return (a @ b) % mod


def m42int(m, o):
    """
    Usage:

    >>> from numpy import array, uint8
    >>> m = array([[1, 3, 3, 3, 3],
    ...            [0, 1, 3, 3, 0],
    ...            [0, 0, 1, 0, 0],
    ...            [0, 0, 0, 1, 0],
    ...            [0, 0, 0, 0, 1]], dtype=np.uint64)
    >>> m42int(m, 4)
    4095
    """
    n = 0
    l = len(m)
    exp = 1
    for i in range(l - 1):
        for j in range(i + 1, l):
            n += int(m[i, j]) * exp
            exp *= o
    return n


def int2m4(n, o, l=4):
    """
    Usage:

    >>> int2m4(4095, 4, 5)
    array([[1, 3, 3, 3, 3],
           [0, 1, 3, 3, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]], dtype=uint64)
    """
    m = np.eye(l, dtype=np.uint64)
    for i in range(l - 1):
        for j in range(i + 1, l):
            n, rem = divmod(n, o)
            m[i, j] = rem
    return m


def m4inv(m, o):
    # if o < 257:
    #     return np.uint8(np.linalg.inv(m) % o)
    return np.linalg.inv(m) % o
