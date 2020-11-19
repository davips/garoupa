#  Copyright (c) 2020. Davi Pereira dos Santos
#  This file is part of the cruipto project.
#  Please respect the license - more about this in the section (*) below.
#
#  cruipto is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  cruipto is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with cruipto.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.
#

import hashlib

from numpy.core.multiarray import ndarray

from cruipto.encoders import dec, enc
from cruipto.hashmath import bmatmul, bmat2int, int2bmat, bmatinv


class Hash:
    last = 2 ** 128 - 1
    base62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    base62rev = {char: idx for idx, char in enumerate("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")}
    _hex, _n, _id, _inv = None, None, None, None

    def __init__(self, identifier):
        if isinstance(identifier, int):
            if identifier > self.last or identifier < 0:
                raise Exception(f"Number should be in the interval [0," f"{self.last}]!")
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
        elif isinstance(identifier, bytes):
            self._hex = hashlib.md5(identifier).hexdigest()
        else:
            raise Exception("Wrong argument type for UUID:", type(identifier))

    @property
    def n(self):
        if self._n is None:
            if self._hex:
                self._n = int(self._hex, 16)
            elif self._m:
                self._n = bmat2int(self._m)
            elif self._id:
                self._n = dec(self._id, lookup=self.base62rev)
            else:
                raise Exception("Missing hash starting point!")
        return self._n

    @property
    def m(self):
        if self._m is None:
            if self._hex or self._id or self._n:
                self._m = int2bmat(self.n)
            else:
                raise Exception("Missing hash starting point!")
        return self._m

    @property
    def hex(self):
        if self._hex is None:
            if self._m or self._id or self._n:
                self._hex = hex(self.n)[2:].rjust(22, "0")
            else:
                raise Exception("Missing hash starting point!")
        return self._hex

    @property
    def id(self):
        if self._id is None:
            if self._m or self._hex or self._n:
                self._id = enc(self.n, alphabet=self.base62)
            else:
                raise Exception("Missing hash starting point!")
        return self._id

    @property
    def inv(self):
        return Hash(bmatinv(self.m))

    def __mul__(self, other):
        return Hash(bmatmul(self.m, other.m))

