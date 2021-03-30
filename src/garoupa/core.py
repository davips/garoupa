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


def s_z_perm_id_fromblob(blob, commutative):
    """
    Four i64 segments: A, B, C, D
    Two numbers:
        S = 2^64*A + D
        Z = 2^64*B + C
    |   ~64 bits S34   |   ~64 bits Z128-159   |   64 bits Z128-159   |   64 bits S34   |
    """
    digest = blake3(blob).digest()
    from garoupa import Hash
    s = 0 if commutative else int.from_bytes(digest[:16], byteorder="big") % Hash.orders
    z = int.from_bytes(digest[16:], byteorder="big") % Hash.orderz
    perm = int2pmat(s, 34)
    id = b62enc(s, z)
    return s, z, id, perm


def s_id_fromzperm(z: int, perm: bytes):
    s = pmat2int(perm)
    id = b62enc(s, z)
    return s, id


def s_z_perm_fromid(id):
    s, z = b62dec(id)
    perm = int2pmat(s, 34)
    return s, z, perm


def perm_id_fromsz(s, z):
    perm = int2pmat(s, 34)
    id = b62enc(s, z)
    return perm, id
