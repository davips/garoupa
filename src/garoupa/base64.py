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


alphabet = tuple("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-.")
rev_alphabet = dict((c, v) for v, c in enumerate(alphabet))


def b64dec(string):
    """
    Usage:

    >>> b64dec("aa") == 10*64 + 10
    True

    Parameters
    ----------
    string

    Returns
    -------

    """
    num = 0
    for char in string:
        num = num * 64 + rev_alphabet[char]
    return num


def b64enc(num, digits):
    """
    Usage:

    >>> b64enc(123456, 10)
    '0000000u90'
    >>> n = b64dec(b64enc(123456, 10))
    >>> n == 123456
    True
    """
    encoded = ""
    while num:
        num, rem = divmod(num, 64)
        encoded = alphabet[rem] + encoded
    return encoded.rjust(digits, "0")
