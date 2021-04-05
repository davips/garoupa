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

from hashlib import md5

from garoupa.colors import colorize128bit
from garoupa.core import zs_perm_id_fromblob, zs_perm_fromid, perm_id_fromzs, s_id_fromzperm
from garoupa.math import pmat_mult, pmat_inv


class Hash:
    """
    's' (< 34!) and 'z' (< 2^128 - 159) define an element of 256 bits.
    When importing 128 bits hashes like MD5, it should be split between 's' and 'z'.

    's' should be zero to create a commutative element.

    Set only 'z' for a commutative element;
    set both 'z' and 's' otherwise.
    bits = |   ~128 bits ZM127   |   ~128 bits S34   |

    Usage:
    >>> a = Hash(b"lots of data")
    >>> b = Hash(b"lots of data 2")
    >>> a.id
    'TQrQtGEcOZ666oBPwiT4G0QtAh0vW5HW4Vcw4hTD0Ls'
    >>> (a * b).id
    'Od1QpzT2bl9fHlanBznoqofqOo12PrCollgAkN1aM3W'
    >>> (b * a).id
    'Od1QpzT2bl9fHlanBznoqmMVMKt0c1hFsUBiPNJ6Pqp'
    >>> a * b * ~b == a
    True
    >>> c = Hash(b"lots of data 3")
    >>> (a * b) * c == a * (b * c)
    True
    >>> old_128bit_hash = md5(b"lots of data for a commuting element").digest()
    >>> d = Hash.from128bit(old_128bit_hash)
    >>> d.bits  # four 64-bit parts: zeros, half for 's', zeros, half for 'z'
    '0000000000000000000000000000000000000000000000000000000000000000000101011110101101011011111011101101000010100100000100110110111100000000000000000000000000000000000000000000000000000000000000001100011000100101001110110110101100101000010010110011011010100010'
    >>> e = Hash(b"lots of data", commutative=True)
    >>> f = Hash(b"lots of data 2")
    >>> e * f == f * e
    True
    >>> a * b == b * a
    False
    """
    _repr = None
    orders = 295232799039604140847618609643520000000  # 34!
    orderz = 340282366920938463463374607431768211297  # 2**128-159
    _2_128 = 2 ** 128
    _n, _id, _z, _s, _perm = None, None, None, None, None
    _bits, _zs = None, None

    def __init__(self, blob, commutative=False):
        if blob is not None:
            self._z, self._s, self._perm, self._id = zs_perm_id_fromblob(blob, commutative)

    @classmethod
    def fromperm(cls, perm, z):
        hash = Hash(None)
        hash._z, hash._perm = z, perm
        return hash

    @classmethod
    def fromzs(cls, z, s):
        hash = Hash(None)
        hash._z, hash._s = z, s
        return hash

    @classmethod
    def fromid(cls, id):
        """
        Usage:
        >>> Hash.fromid("HpHx15miyc2amaxUwSQiv0Z0XtM73NdL0paVyy1inV9").s
        99929999938476344564747343999999245678

        :param id:
        :return:
        """
        hash = Hash(None)
        hash._id = id
        return hash

    @classmethod
    def from128bit(cls, digest: bytes, commutative=False):
        """Return hash representing the given 16 bytes:
        64 most significant bits for 'z', 64 least significant bits for 's', (non-commutative); or,
        128 bits for z, none for s, if commutative flag is set (z should be less than 2^128-159).

        Usage:
        >>> bytes = md5(b"This digest represents a hash comming from some external database.").digest()
        >>> bytes
        b'G\\xa9Cm\\xd4>\\x07\\xacy\\xaf\\xc0?xI\\x01O'
        >>> h = Hash.from128bit(bytes)
        >>> h.id
        '00000000000lw1ZHv7gl7eezgThOWaUcKmljcZMPL39'
        >>> h.bits
        '0000000000000000000000000000000000000000000000000000000000000000010001111010100101000011011011011101010000111110000001111010110000000000000000000000000000000000000000000000000000000000000000000111100110101111110000000011111101111000010010010000000101001111'
        """
        hash = Hash(None)
        if commutative:
            hash._z = int.from_bytes(digest, byteorder="big")
            hash._s = 0
        else:
            hash._z = int.from_bytes(digest[:8], byteorder="big")
            hash._s = int.from_bytes(digest[8:], byteorder="big")
        return hash

    def to128bit(self, commutative=False):
        """The most significant parts of 's' and 'z' should be zero,
         because conversion will keep only: 64 bits for 's', 64 bits for 'z'.
         Unless the commutative flag is set, which results in all 128 bits from 'z'.

        Usage:
        >>> h = Hash.from128bit(b'3124123329432412')
        >>> h.to128bit()
        b'3124123329432412'
        >>> h.bits
        '0000000000000000000000000000000000000000000000000000000000000000001100110011000100110010001101000011000100110010001100110011001100000000000000000000000000000000000000000000000000000000000000000011001000111001001101000011001100110010001101000011000100110010'
        """
        if commutative:
            zbytes = self.z.to_bytes(16, byteorder="big")
            return zbytes
        zbytes = self.z.to_bytes(8, byteorder="big")
        sbytes = self.s.to_bytes(8, byteorder="big")
        return zbytes + sbytes

    @classmethod
    def fromn(cls, n: int):
        """Return hash representing the given int.
        Numbers from one of the intervals [0; 34![  or  [2^128; 2^256-159[

        Usage:
        >>> h = Hash.fromn(324134134)
        >>> h.id
        '00000000000000000000000000000000000000Lw25u'
        """
        z, s = divmod(n, cls._2_128)
        return Hash.fromzs(z, s)

    def calculate(self):
        if self._perm:
            self._s, self._id = s_id_fromzperm(self._z, self._perm)
        elif self._id:
            self._z, self._s, self._perm = zs_perm_fromid(self._id)
        elif None not in [self._z, self._s]:
            self._perm, self._id = perm_id_fromzs(self._z, self._s)
        else:
            raise Exception("Missing argument.")
        if self.s >= self.orders:
            raise Exception(f"Element 's' part outside allowed range: {self.s} >= {self.orders}")
        if self.z >= self.orderz:
            raise Exception(f"Element 'z' part outside allowed range: {self.z} >= {self.orderz}")

    @property
    def perm(self):
        if self._perm is None:
            self.calculate()
        return self._perm

    @property
    def n(self):
        if self._n is None:
            self._n = self.z * self._2_128 + self.s
        return self._n

    @property
    def zs(self):
        if self._zs is None:
            self._zs = self.z, self.s
        return self._zs

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
        return Hash.fromperm(perm=pmat_mult(self.perm, other.perm), z=(self.z + other.z) % self.orderz)

    def __invert__(self):
        return Hash.fromperm(perm=pmat_inv(self.perm), z=self.orderz - self.z)

    def __truediv__(self, other):
        return Hash.fromperm(perm=pmat_mult(self.perm, pmat_inv(other.perm)), z=(self.z - other.z) % self.orderz)

    def __add__(self, other):
        return Hash.fromzs((self.z + other.z) % self.orderz, (self.s + other.s) % self.orders)

    def __sub__(self, other):
        return Hash.fromzs((self.z - other.z) % self.orderz, (self.s - other.s) % self.orders)

    def __repr__(self):
        if self._repr is None:
            self._repr = colorize128bit(self.id)
        return self._repr

    @property
    def idc(self):
        return repr(self)

    def __str__(self):
        return self.id

    def __eq__(self, other):
        return self.z == other.z and self.s == other.s

        # @classmethod
    # def muls(cls, size, /, *perms):  # 23.6 µs
    #     return Hash(perm=reduce(pmat_mult, [p.perm for p in perms]))
    #
    # @classmethod
    # def pairmuls(cls, size, /, *pairs):  # 5.34 µs
    #     results = map(lambda a, b: pmat_mult(a.perm, b.perm), pairs[::2], pairs[1::2])
    #     return [Hash(perm=res) for res in results]


identity = Hash.fromzs(0, 0)
