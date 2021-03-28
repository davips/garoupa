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


alphabet = tuple("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
rev_alphabet = dict((c, v) for v, c in enumerate(alphabet))


def b62dec(string):
    """
    Usage:
    >>> b62dec("AA") == (0, 10*62 + 10)
    True

    Parameters
    ----------
    string

    Returns
    -------

    """
    num = 0
    for char in string:
        num = num * 62 + rev_alphabet[char]
    s, z = divmod(num, 2 ** 128)
    return s, z


def b62enc(s, z):
    """
    Usage:
    >>> b62enc(123, 456)
    '00000000000000000000FSL0OJRorrriZQUQzLO9WlE'
    >>> n = b62dec(b62enc(123, 456))
    >>> n == (123, 456)
    True

    :param s:
    :param z:
    :return:
    """
    encoded = ""
    num = s * 2 ** 128 + z
    while num:
        num, rem = divmod(num, 62)
        encoded = alphabet[rem] + encoded
    return encoded.rjust(43, "0")
