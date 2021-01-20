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

import hashlib

import numpy as np
from garoupa.encoders import dec, enc
from garoupa.hashmath import bmm, bm2int, int2bm, bytes2bm, bminv, numba
from numpy.core.multiarray import ndarray


class Hash:
    last_n = 2 ** 128 - 1
    base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    base62rev = {char: idx for idx, char in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")}
    _m, _hex, _n, _id, _inv = None, None, None, None, None
    _bitindexes = None

    def __init__(self, identifier, compiled=False):
        if compiled:
            Hash.bytes2bm, Hash.bmm, Hash.bm2int, Hash.bminv, Hash.int2bm = numba()
        else:
            Hash.bytes2bm, Hash.bmm, Hash.bm2int, Hash.bminv, Hash.int2bm = bytes2bm, bmm, bm2int, bminv, int2bm
        self.compiled = compiled

        if isinstance(identifier, int):
            if identifier > self.last_n or identifier < 0:
                raise Exception(f"Number should be in the interval [0," f"{self.last_n}]!")
            self._n = identifier
        elif isinstance(identifier, ndarray):
            if identifier.shape != (17, 17):
                raise Exception(f"Invalid numpy array identifier:", identifier)
            self._m = identifier
        elif isinstance(identifier, str):
            size = len(identifier)
            if size == 22:
                if any([c not in self.base62 for c in identifier]):
                    raise Exception(f"Invalid base62 identifier:", identifier)
                self._id = identifier
            elif size == 32:
                if any([c not in "0123456789abcdef" for c in identifier]):
                    raise Exception(f"Invalid MD5 hex digest:", identifier)
                self._hex = identifier
            else:
                raise Exception(f"String identifier should have 22 or 32 chars! Not {size}!")
        elif isinstance(identifier, bytes) and len(identifier) == 16:
            self._bytes = identifier
        elif isinstance(identifier, bytes):
            self._hex = hashlib.md5(identifier).hexdigest()
        else:
            raise Exception("Wrong argument type for UUID:", type(identifier))

    @property
    def bitindexes(self):
        if self._bitindexes is None:
            self._bitindexes = [i for i, b in enumerate(np.concatenate(self.m)) if b == 1]
        return self._bitindexes

    @property
    def last(self):
        return Hash(self.last_n)

    @property
    def n(self):
        if self._n is None:
            if self._hex is not None:
                self._n = int(self._hex, 16)
            elif self._m is not None:
                self._n = self.bm2int(self._m)
            elif self._id is not None:
                self._n = dec(self._id, lookup=self.base62rev)
                if self._n > self.last_n:
                    raise Exception(f"Id {self._id} converted to number is higher than {self.last_n}.")
            elif self._bytes is not None:
                self._n = int.from_bytes(self._bytes, byteorder="big")
            else:
                raise Exception("Missing hash starting point!")
        return self._n

    @property
    def m(self):
        if self._m is None:
            if self._n is not None or self._hex is not None or self._id is not None:
                self._m = Hash.int2bm(self.n)
            elif self._bytes is not None:
                self._m = Hash.bytes2bm(self._bytes)
            else:
                raise Exception("Missing hash starting point!")
        return self._m

    @property
    def bytes(self):
        if self._bytes is None:
            if self._m is not None or self._id is not None or self._n is not None:
                self._bytes = self.n.to_bytes(16, byteorder="big")
            elif self._hex is not None:
                self._bytes = bytes.fromhex(self._hex)
            else:
                raise Exception("Missing hash starting point!")
        return self._bytes

    @property
    def hex(self):
        if self._hex is None:
            if self._m is not None or self._id is not None or self._n is not None:
                self._hex = hex(self.n)[2:].rjust(32, "0")
            elif self._bytes is not None:
                self._hex = self._bytes.hex()
            else:
                raise Exception("Missing hash starting point!")
        return self._hex

    @property
    def id(self):
        if self._id is None:
            if self._m is not None or self._hex is not None or self._n is not None or self._bytes is not None:
                self._id = enc(self.n, alphabet=self.base62)
            else:
                raise Exception("Missing hash starting point!")
        return self._id

    @property
    def inv(self):
        return Hash(Hash.bminv(self.m))

    def __mul__(self, other):
        # return Hash(bmm(self.m, int2cycledbm(other.n)))  # 600us [além de mais lento, não completamente reversível: A¹AB != B]
        return Hash(Hash.bmm(self.m, other.m))  # 10us (60us sem numba)

    def __truediv__(self, other):
        return Hash(Hash.bmm(self.m, other.inv.m))

    def __str__(self):
        return self.id
