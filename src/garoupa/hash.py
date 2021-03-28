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

from functools import reduce, lru_cache
from math import factorial

from garoupa.colors import colorize128bit
from garoupa.core import s_z_perm_id_fromblob, s_z_perm_fromid, perm_id_fromsz, s_id_fromzperm
from garoupa.math import pmat_mult, pmat_inv


class Hash:
    """
    's' (< 34!) and 'z' (< 2^128 - 159) define an element of 256 bits.
    When importing 128 bits hashes like MD5, it should be split between 's' and 'z'.

    's' should be zero to create a commutative element.

    Set 'z' for a commutative element;
    set both '
    bits = |   ~64 bits ZM127   |   ~64 bits S34   |   64 bits S34   |   64 bits ZM127   |

    Usage:
    >>> a = Hash(2345, 234)
    >>> b = Hash(3210, 789)
    >>> str(a)
    '00000000000000000004kgldjfdRDKqooNfP6fKwdCM'
    >>> str(a * b)
    '000000000000000001k7sBgku1gWz02CQZ7ryQ5T6cB'
    >>> a * b * ~b == a
    True
    >>> c = Hash(457, 45674)
    >>> (a * b) * c == a * (b * c)
    True

    """
    _repr = None
    orders = 295232799039604140847618609643520000000  # 34!
    orderz = 340282366920938463463374607431768211297  # 2**128-159
    _2_128 = 2 ** 128
    _n = None
    _bits = None

    def __init__(self, s=None, z=None, blob=None, id=None, perm=None):
        if blob:
            self._s, self._z, self._id, self._perm = s_z_perm_id_fromblob(blob)
        else:
            self._s, self._z, self._id, self._perm = s, z, id, perm

    def calculate(self):
        if self._perm:
            self._s, self._id = s_id_fromzperm(self._z, self._perm)
        elif self._id:
            self._s, self._z, self._perm = s_z_perm_fromid(self._id)
        elif None not in [self._s, self._z]:
            self._perm, self._id = perm_id_fromsz(self._s, self._z)
        else:
            raise Exception("Missing argument.")

    @property
    def perm(self):
        if self._perm is None:
            self.calculate()
        return self._perm

    @property
    def n(self):
        if self._n is None:
            self._n = self.s * self._2_128 + self.z
        return self._n

    @property
    def id(self):
        if self._id is None:
            self.calculate()
        return self._id

    @property
    def s(self):
        if self._s is None:
            self.calculate()
        return self._s

    @property
    def bits(self):
        if self._bits is None:
            self._bits = bin(self.n)[2:].rjust(256, "0")
        return self._bits

    @property
    def z(self):
        if self._z is None:
            self.calculate()
        return self._z

    def __mul__(self, other):
        return Hash(z=(self.z + other.z) % self.orderz, perm=pmat_mult(self.perm, other.perm))

    def __invert__(self):
        return Hash(z=self.orderz - self.z, perm=pmat_inv(self.perm))

    def __truediv__(self, other):
        return Hash(z=(self.z - other.z) % self.orderz, perm=pmat_mult(self.perm, pmat_inv(other.perm)))

    def __add__(self, other):
        return Hash((self.s + other.s) % self.orders, (self.z + other.z) % self.orderz)

    def __sub__(self, other):
        return Hash((self.s - other.s) % self.orders, (self.z - other.z) % self.orderz)

    def __repr__(self):
        if self._repr is None:
            self._repr = colorize128bit(self.id)
        return self._repr

    def __str__(self):
        return self.id

    def __eq__(self, other):
        return self.s == other.s and self.z == other.z
        # @classmethod
    # def muls(cls, size, /, *perms):  # 23.6 µs
    #     return Hash(perm=reduce(pmat_mult, [p.perm for p in perms]))
    #
    # @classmethod
    # def pairmuls(cls, size, /, *pairs):  # 5.34 µs
    #     results = map(lambda a, b: pmat_mult(a.perm, b.perm), pairs[::2], pairs[1::2])
    #     return [Hash(perm=res) for res in results]
