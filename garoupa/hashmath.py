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
#
from math import factorial

import numpy as np


def numba():
    try:
        from numba import njit
    except ModuleNotFoundError as e:
        print("Install numba to use compiled version of Hash:\npip install numba")

    @njit
    def bytes2bm_compiled(bs):
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

    @njit
    def bmm_compiled(a, b):
        """unitriangular bmatrix multiplication"""
        return (a @ b) % 2

    @njit
    def bm2int_compiled(m):
        return bm2int(m)

    @njit
    def bminv_compiled(m):
        return np.linalg.inv(m) % 2

    def int2bm_compiled(n):
        return bytes2bm_compiled(n.to_bytes(16, byteorder='big'))

    return bytes2bm_compiled, bmm_compiled, bm2int_compiled, bminv_compiled, int2bm_compiled


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
    return bytes2bm(n.to_bytes(16, byteorder='big'))


def bmm(a, b):
    """unitriangular bmatrix multiplication"""
    return (a @ b) % 2


# @njit
# def bytes2cycledbm_compiled(bs):
#     return bytes2cycledbm(bs)
#
#
def bytes2cycledbm(bs):
    """Create a unitriangular matrix multiplying the matrix representations of all 127 bit left-rotations of the given bytes."""
    b15 = int(bs[15])
    b14 = int(bs[14])
    b13 = int(bs[13])
    b12 = int(bs[12])
    b11 = int(bs[11])
    b10 = int(bs[10])
    b9 = int(bs[9])
    b8 = int(bs[8])
    b7 = int(bs[7])
    b6 = int(bs[6])
    b5 = int(bs[5])
    b4 = int(bs[4])
    b3 = int(bs[3])
    b2 = int(bs[2])
    b1 = int(bs[1])
    b0 = int(bs[0])
    m = np.eye(17)
    r = np.eye(17)
    for run in range(128):
        # print(run, nb.typeof(b15))
        # # Code generator:
        # b, B = 0, 15
        #
        #
        # def code(i, j):
        #     global b, B
        #     print(f"\t\tm[{i}, {j}] = float(b{B} >> {b} & 1)")
        #     b += 1
        #     if b == 8:
        #         b = 0
        #         B -= 1
        #
        #
        # for i in range(12):
        #     if i < 3:
        #         for j in range(i + 1, 4):
        #             code(i, j)
        #     for j in range(max(5, i + 1), 17):
        #         code(i, j)
        #
        # for i in range(13, 17):
        #     for j in range(max(12, i + 1), 17):
        #         code(i, j)
        m[0, 1] = float((b15 >> 0) + 1)
        m[0, 2] = float((b15 >> 1) + 1)
        m[0, 3] = float((b15 >> 2) + 1)
        m[0, 5] = float((b15 >> 3) + 1)
        m[0, 6] = float((b15 >> 4) + 1)
        m[0, 7] = float((b15 >> 5) + 1)
        m[0, 8] = float((b15 >> 6) + 1)
        m[0, 9] = float((b15 >> 7) + 1)
        m[0, 10] = float((b14 >> 0) + 1)
        m[0, 11] = float((b14 >> 1) + 1)
        m[0, 12] = float((b14 >> 2) + 1)
        m[0, 13] = float((b14 >> 3) + 1)
        m[0, 14] = float((b14 >> 4) + 1)
        m[0, 15] = float((b14 >> 5) + 1)
        m[0, 16] = float((b14 >> 6) + 1)
        m[1, 2] = float((b14 >> 7) + 1)
        m[1, 3] = float((b13 >> 0) + 1)
        m[1, 5] = float((b13 >> 1) + 1)
        m[1, 6] = float((b13 >> 2) + 1)
        m[1, 7] = float((b13 >> 3) + 1)
        m[1, 8] = float((b13 >> 4) + 1)
        m[1, 9] = float((b13 >> 5) + 1)
        m[1, 10] = float((b13 >> 6) + 1)
        m[1, 11] = float((b13 >> 7) + 1)
        m[1, 12] = float((b12 >> 0) + 1)
        m[1, 13] = float((b12 >> 1) + 1)
        m[1, 14] = float((b12 >> 2) + 1)
        m[1, 15] = float((b12 >> 3) + 1)
        m[1, 16] = float((b12 >> 4) + 1)
        m[2, 3] = float((b12 >> 5) + 1)
        m[2, 5] = float((b12 >> 6) + 1)
        m[2, 6] = float((b12 >> 7) + 1)
        m[2, 7] = float((b11 >> 0) + 1)
        m[2, 8] = float((b11 >> 1) + 1)
        m[2, 9] = float((b11 >> 2) + 1)
        m[2, 10] = float((b11 >> 3) + 1)
        m[2, 11] = float((b11 >> 4) + 1)
        m[2, 12] = float((b11 >> 5) + 1)
        m[2, 13] = float((b11 >> 6) + 1)
        m[2, 14] = float((b11 >> 7) + 1)
        m[2, 15] = float((b10 >> 0) + 1)
        m[2, 16] = float((b10 >> 1) + 1)
        m[3, 5] = float((b10 >> 2) + 1)
        m[3, 6] = float((b10 >> 3) + 1)
        m[3, 7] = float((b10 >> 4) + 1)
        m[3, 8] = float((b10 >> 5) + 1)
        m[3, 9] = float((b10 >> 6) + 1)
        m[3, 10] = float((b10 >> 7) + 1)
        m[3, 11] = float((b9 >> 0) + 1)
        m[3, 12] = float((b9 >> 1) + 1)
        m[3, 13] = float((b9 >> 2) + 1)
        m[3, 14] = float((b9 >> 3) + 1)
        m[3, 15] = float((b9 >> 4) + 1)
        m[3, 16] = float((b9 >> 5) + 1)
        m[4, 5] = float((b9 >> 6) + 1)
        m[4, 6] = float((b9 >> 7) + 1)
        m[4, 7] = float((b8 >> 0) + 1)
        m[4, 8] = float((b8 >> 1) + 1)
        m[4, 9] = float((b8 >> 2) + 1)
        m[4, 10] = float((b8 >> 3) + 1)
        m[4, 11] = float((b8 >> 4) + 1)
        m[4, 12] = float((b8 >> 5) + 1)
        m[4, 13] = float((b8 >> 6) + 1)
        m[4, 14] = float((b8 >> 7) + 1)
        m[4, 15] = float((b7 >> 0) + 1)
        m[4, 16] = float((b7 >> 1) + 1)
        m[5, 6] = float((b7 >> 2) + 1)
        m[5, 7] = float((b7 >> 3) + 1)
        m[5, 8] = float((b7 >> 4) + 1)
        m[5, 9] = float((b7 >> 5) + 1)
        m[5, 10] = float((b7 >> 6) + 1)
        m[5, 11] = float((b7 >> 7) + 1)
        m[5, 12] = float((b6 >> 0) + 1)
        m[5, 13] = float((b6 >> 1) + 1)
        m[5, 14] = float((b6 >> 2) + 1)
        m[5, 15] = float((b6 >> 3) + 1)
        m[5, 16] = float((b6 >> 4) + 1)
        m[6, 7] = float((b6 >> 5) + 1)
        m[6, 8] = float((b6 >> 6) + 1)
        m[6, 9] = float((b6 >> 7) + 1)
        m[6, 10] = float((b5 >> 0) + 1)
        m[6, 11] = float((b5 >> 1) + 1)
        m[6, 12] = float((b5 >> 2) + 1)
        m[6, 13] = float((b5 >> 3) + 1)
        m[6, 14] = float((b5 >> 4) + 1)
        m[6, 15] = float((b5 >> 5) + 1)
        m[6, 16] = float((b5 >> 6) + 1)
        m[7, 8] = float((b5 >> 7) + 1)
        m[7, 9] = float((b4 >> 0) + 1)
        m[7, 10] = float((b4 >> 1) + 1)
        m[7, 11] = float((b4 >> 2) + 1)
        m[7, 12] = float((b4 >> 3) + 1)
        m[7, 13] = float((b4 >> 4) + 1)
        m[7, 14] = float((b4 >> 5) + 1)
        m[7, 15] = float((b4 >> 6) + 1)
        m[7, 16] = float((b4 >> 7) + 1)
        m[8, 9] = float((b3 >> 0) + 1)
        m[8, 10] = float((b3 >> 1) + 1)
        m[8, 11] = float((b3 >> 2) + 1)
        m[8, 12] = float((b3 >> 3) + 1)
        m[8, 13] = float((b3 >> 4) + 1)
        m[8, 14] = float((b3 >> 5) + 1)
        m[8, 15] = float((b3 >> 6) + 1)
        m[8, 16] = float((b3 >> 7) + 1)
        m[9, 10] = float((b2 >> 0) + 1)
        m[9, 11] = float((b2 >> 1) + 1)
        m[9, 12] = float((b2 >> 2) + 1)
        m[9, 13] = float((b2 >> 3) + 1)
        m[9, 14] = float((b2 >> 4) + 1)
        m[9, 15] = float((b2 >> 5) + 1)
        m[9, 16] = float((b2 >> 6) + 1)
        m[10, 11] = float((b2 >> 7) + 1)
        m[10, 12] = float((b1 >> 0) + 1)
        m[10, 13] = float((b1 >> 1) + 1)
        m[10, 14] = float((b1 >> 2) + 1)
        m[10, 15] = float((b1 >> 3) + 1)
        m[10, 16] = float((b1 >> 4) + 1)
        m[11, 12] = float((b1 >> 5) + 1)
        m[11, 13] = float((b1 >> 6) + 1)
        m[11, 14] = float((b1 >> 7) + 1)
        m[11, 15] = float((b0 >> 0) + 1)
        m[11, 16] = float((b0 >> 1) + 1)
        m[13, 14] = float((b0 >> 2) + 1)
        m[13, 15] = float((b0 >> 3) + 1)
        m[13, 16] = float((b0 >> 4) + 1)
        m[14, 15] = float((b0 >> 5) + 1)
        m[14, 16] = float((b0 >> 6) + 1)
        m[15, 16] = float((b0 >> 7) + 1)

        lead = b0 >> 7
        b0 = int(((b0 << 1) % 256) + (b1 >> 7))
        b1 = int(((b1 << 1) % 256) + (b2 >> 7))
        b2 = int(((b2 << 1) % 256) + (b3 >> 7))
        b3 = int(((b3 << 1) % 256) + (b4 >> 7))
        b4 = int(((b4 << 1) % 256) + (b5 >> 7))
        b5 = int(((b5 << 1) % 256) + (b6 >> 7))
        b6 = int(((b6 << 1) % 256) + (b7 >> 7))
        b7 = int(((b7 << 1) % 256) + (b8 >> 7))
        b8 = int(((b8 << 1) % 256) + (b9 >> 7))
        b9 = int(((b9 << 1) % 256) + (b10 >> 7))
        b10 = int(((b10 << 1) % 256) + (b11 >> 7))
        b11 = int(((b11 << 1) % 256) + (b12 >> 7))
        b12 = int(((b12 << 1) % 256) + (b13 >> 7))
        b13 = int(((b13 << 1) % 256) + (b14 >> 7))
        b14 = int(((b14 << 1) % 256) + (b15 >> 7))
        b15 = int(((b15 << 1) % 256) + lead)

        r = (r @ m) % 2
    return r


#
#
# def bytes2cycledbm(bs):
#     return bytes2cycledbm_nub(np.frombuffer(bs, dtype=np.dtype(np.uint8)))
#
#
# def int2cycledbm(n):
#     return bytes2cycledbm(n.to_bytes(16, byteorder='big'))


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
    return np.linalg.inv(m) % 2


def bitpos(i, j):
    """Return bit position corresponding to the given cell location in the matrix."""
    b = i * 17 + j
    if i == 0:
        b -= 1
    else:
        b -= factorial(i + 2) / (2 * factorial(i))
    if i < 4:
        b -= i
        if j > 3:
            b -= 1
    else:
        b -= 4
    if i > 11:
        b -= 4
    return int(b)


def bmmap():
    """Print unitriangular matrix showing bit positions."""
    for i in range(17):
        print(i, end=":\t")
        for j in range(17):
            if j == i:
                print(1, end="\t")
            elif j == 4:
                print(0, end="\t")
            elif i > j:
                print(0, end="\t")
            elif i == 12:
                print(0, end="\t")
            else:
                print(bitpos(i, j), end="\t")
        print()

# def int2bm(n):
#     m = np.eye(17)
#     b = 127
#     for i in range(12):
#         if i < 3:
#             for j in range(i + 1, 4):
#                 m[i, j] = n >> b & 1
#                 b -= 1
#         for j in range(max(5, i + 1), 17):
#             m[i, j] = n >> b & 1
#             b -= 1
#     for i in range(13, 17):
#         for j in range(max(12, i + 1), 17):
#             m[i, j] = n >> b & 1
#             b -= 1
#     return m


# def bm2int(m):
#     n = 0
#     b = 127
#     for i in range(12):
#         if i < 3:
#             for j in range(i + 1, 4):
#                 n += int(m[i, j]) << b
#                 b -= 1
#         for j in range(max(5, i + 1), 17):
#             n += int(m[i, j]) << b
#             b -= 1
#     for i in range(13, 17):
#         for j in range(max(12, i + 1), 17):
#             n += int(m[i, j]) << b
#             b -= 1
#     return n
