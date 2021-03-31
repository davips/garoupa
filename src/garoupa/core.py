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

from blake3 import blake3

from garoupa.base62 import b62enc, b62dec
from garoupa.math import int2pmat, pmat2int


def zs_perm_id_fromblob(blob, commutative):
    digest = blake3(blob).digest()
    from garoupa import Hash
    z = int.from_bytes(digest[:16], byteorder="big") % Hash.orderz
    s = 0 if commutative else int.from_bytes(digest[16:], byteorder="big") % Hash.orders
    perm = int2pmat(s, 34)
    id = b62enc(z, s)
    return z, s, perm, id


def s_id_fromzperm(z: int, perm: bytes):
    s = pmat2int(perm)
    id = b62enc(z, s)
    return s, id


def zs_perm_fromid(id):
    z, s = b62dec(id)
    perm = int2pmat(s, 34)
    return z, s, perm


def perm_id_fromzs(z, s):
    perm = int2pmat(s, 34)
    id = b62enc(z, s)
    return perm, id
