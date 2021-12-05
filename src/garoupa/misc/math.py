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

"""
Pure Python linear algebra module
"""


def int2cells(num, mod):
    """
    Convert an integer to cells representing a 4x4 unitriangular matrix

    >>> e = [42821,772431,428543,443530,42121,7213]
    >>> e == int2cells(cells2int(e,4294967291), 4294967291)
    True
    >>> try:
    ...     int2cells(-1, 10)
    ... except Exception as e:
    ...     print(e)
    Number -1 too large for given mod 10

    Parameters
    ----------
    num
    mod

    Returns
    -------

    """
    m = [0, 0, 0, 0, 0, 0]
    num, m[5] = divmod(num, mod)
    num, m[4] = divmod(num, mod)
    num, m[3] = divmod(num, mod)
    num, m[2] = divmod(num, mod)
    num, m[1] = divmod(num, mod)
    rest, m[0] = divmod(num, mod)
    if rest != 0:  # pragma: no cover
        raise Exception(f"Number {num} too large for given mod {mod}")
    return m


def cells2int(m, mod):
    """
    Convert cells representing a 4x4 unitriangular matrix to an integer.

    Usage:

    >>> n = 986723489762345987253897254295863
    >>> cells2int(int2cells(n, 4294967291), 4294967291) == n
    True

    Parameters
    ----------
    m
        List with six values
    mod
        Large prime number

    Returns
    -------
        Lexicographic rank of the element (at least according to the disposition of cells adopted here)
    """
    return m[5] + m[4] * mod + m[3] * (mod ** 2) + m[2] * (mod ** 3) + m[1] * (mod ** 4) + m[0] * (mod ** 5)


def cellsmul(a, b, mod):
    """
    Multiply two unitriangular matrices 4x4 modulo 'mod'.

    'a' and 'b' given as lists in the format: [a5, a4, a3, a2, a1, a0]

    1 a4 a1 a0
    0  1 a2 a3
    0  0  1 a5
    0  0  0  1

    >>> a, b = [51,18340,56,756,456,344], [781,2340,9870,1234,9134,3134]
    >>> cellsmul(b, cellsinv(b, 4294967291), 4294967291) == [0,0,0,0,0,0]
    True
    >>> c = cellsmul(a, b, 4294967291)
    >>> cellsmul(c, cellsinv(b, 4294967291), 4294967291) == a
    True

    Parameters
    ----------
    a
        List with six values
    b
        Another (or the same) list with six values
    mod
        Large prime number

    Returns
    -------
        The list that corresponds to the resulting element from multiplication
    """
    return [
        (a[0] + b[0]) % mod,
        (a[1] + b[1]) % mod,
        (a[2] + b[2] + a[3] * b[0]) % mod,
        (a[3] + b[3]) % mod,
        (a[4] + b[4] + a[1] * b[3]) % mod,
        (a[5] + b[5] + a[1] * b[2] + a[4] * b[0]) % mod,
    ]


def cellsinv(m, mod):
    """
    Inverse of unitriangular matrix modulo 'mod'

    'm' given as a list in the format: [a5, a4, a3, a2, a1, a0]

    1 a4 a1 a0
    0  1 a2 a3
    0  0  1 a5
    0  0  0  1

    Based on https://groupprops.subwiki.org/wiki/Unitriangular_matrix_group:UT(4,p)

    >>> e = [42821,772431,428543,443530,42121,7213]
    >>> cellsinv(cellsinv(e, 4294967291), 4294967291)==e
    True

    Parameters
    ----------
    m
        List with six values
    mod
        Large prime number

    Returns
    -------
        The list that corresponds to the inverse element
    """
    return [
        -m[0] % mod,
        -m[1] % mod,
        (m[3] * m[0] - m[2]) % mod,
        -m[3] % mod,
        (m[1] * m[3] - m[4]) % mod,
        (m[1] * m[2] + m[4] * m[0] - m[1] * m[3] * m[0] - m[5]) % mod,
    ]
