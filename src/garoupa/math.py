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
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.

##############################################################################
# Abstract Algebra helper functions
##############################################################################

def int2pmat(number, side):
    """Convert number into permutation.

    Pads to side.

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
    """Convert permutation to number.

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
    """Multiply two permutations.

    Parameters
    ----------
    a
        list of positive integers plus zero
    b
        list of positive integers plus zero

    Returns
    -------

    """
    if len(a) != len(b):
        raise Exception("a and b should have same length.")
    return [a[x] for x in b]


def pmat_transpose(m):
    """Transpose a permutation.

    Original author (CC BY-SA 4.0 LICENSE):
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


def pmat_inv(m):
    size = len(m)
    r = list(range(size))
    for i in range(size):
        r[m[i]] = i
    return r


##############################################################################
# Hash class helper functions
##############################################################################

def m4m(a, b, mod):
    """Multiply two unitriangular matrices 4x4 modulo 'mod'.

    'a' and 'b' given as lists in the format: [a1,4 a1,3 a2,4 a2,3 a3,4 a1,2]

    1 a0 a4 a5
    0  1 a2 a3
    0  0  1 a1
    0  0  0  1

    >>> a, b = [51,18340,56,756,456,344], [781,2340,9870,1234,9134,3134]
    >>> m4m(b, m4inv(b, 4294967291), 4294967291) == [0,0,0,0,0,0]
    True
    >>> c = m4m(a, b, 4294967291)
    >>> m4m(c, m4inv(b, 4294967291), 4294967291) == a
    True
    """
    return [
        (a[0] + b[0] + a[5] * b[2] + a[1] * b[4]) % mod,
        (a[1] + b[1] + a[5] * b[3]) % mod,
        (a[2] + b[2] + a[3] * b[4]) % mod,
        (a[3] + b[3]) % mod,
        (a[4] + b[4]) % mod,
        (a[5] + b[5]) % mod
    ]


def m4inv(m, mod):
    """Inverse of unitriangular matrix modulo 'mod'

    'm' given as a list in the format: [a1,4 a1,3 a2,4 a2,3 a3,4 a1,2]

    1 a0 a4 a5
    0  1 a2 a3
    0  0  1 a1
    0  0  0  1

    Based on https://groupprops.subwiki.org/wiki/Unitriangular_matrix_group:UT(4,p)

    >>> e = [42821,772431,428543,443530,42121,7213]
    >>> m4inv(m4inv(e, 4294967291), 4294967291)==e
    True
    """
    return [
        (m[5] * m[2] + m[1] * m[4] - m[5] * m[3] * m[4] - m[0]) % mod,
        (m[5] * m[3] - m[1]) % mod,
        (m[3] * m[4] - m[2]) % mod,
        -m[3] % mod,
        -m[4] % mod,
        -m[5] % mod,
    ]


def int2m4(num, mod):
    """
    >>> e = [42821,772431,428543,443530,42121,7213]
    >>> e == int2m4(m42int(e,4294967291), 4294967291)
    True
    """
    m = [0, 0, 0, 0, 0, 0]
    num, m[5] = divmod(num, mod)
    num, m[4] = divmod(num, mod)
    num, m[3] = divmod(num, mod)
    num, m[2] = divmod(num, mod)
    num, m[1] = divmod(num, mod)
    num, m[0] = divmod(num, mod)
    return m


def m42int(m, mod):
    """
    >>> n = 986723489762345987253897254295863
    >>> m42int(int2m4(n, 4294967291), 4294967291) == n
    True
    """
    return m[5] + m[4] * mod + m[3] * (mod ** 2) + m[2] * (mod ** 3) + m[1] * (mod ** 4) + m[0] * (mod ** 5)
