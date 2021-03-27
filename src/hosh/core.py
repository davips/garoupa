#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the hoshy project.
#  Please respect the license - more about this in the section (*) below.
#
#  hoshy is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  hoshy is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with hoshy.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.
from blake3 import blake3

from hosh.base62 import b62enc, b62dec
from hosh.math import int2pmat, pmat2int

# def n_bin_id_fromblob(blob):
#     digest = blake3(blob).digest()
#     msb = int.from_bytes(digest[:16], byteorder="big")
#     lsb = int.from_bytes(digest[16:16], byteorder="big")

def n_bin_id_fromblob(blob, size):
    if size == 57:
        skip = 0
        mask = 2 ** 254 - 1
    elif size == 34:
        skip = 16
        mask = 2 ** 127 - 1
    else:
        raise Exception("Wrong size:", size)
    digest = blake3(blob).digest()[skip:]
    n = int.from_bytes(digest, byteorder="big") & mask
    bin = int2pmat(n, size)
    id = b62enc(n, size)
    return n, bin, id


def n_id_fromperm(bin, size):
    n = pmat2int(bin)
    id = b62enc(n, size)
    return n, id


def n_bin_fromid(id, size):
    n = b62dec(id)
    bin = int2pmat(n, size)
    return n, bin


def bin_id_fromn(n, size):
    bin = int2pmat(n, size)
    id = b62enc(n, size)
    return bin, id
