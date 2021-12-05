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
"""Operations with permutations"""


def int2pmat(number, side):
    """Convert number into permutation.

    Pads to side.

    Usage:

    >>> int2pmat(4, 4)
    [0, 2, 1, 3]

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

    Usage:

    >>> pmat2int([0, 2, 1, 3])
    4

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
    if len(a) != len(b):  # pragma: no cover
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
# Hosh class helper functions
##############################################################################
