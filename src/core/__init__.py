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

from core.base62 import b62enc, b62dec
from core.math import int2pmat, pmat2int


def n_bin_id_fromblob(blob):
    digest = blake3(blob).digest()[16:]
    n = int.from_bytes(digest, byteorder="big") & (2 ** 127 - 1)
    bin = int2pmat(n)
    id = b62enc(n)
    return n, bin, id


def n_id_fromperm(bin):
    n = pmat2int(bin)
    id = b62enc(n)
    return n, id


def n_bin_fromid(id):
    n = b62dec(id)
    bin = int2pmat(n)
    return n, bin


def bin_id_fromn(n):
    bin = int2pmat(n)
    id = b62enc(n)
    return bin, id
