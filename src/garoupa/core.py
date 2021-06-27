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

from garoupa.base64 import b64enc, b64dec
from garoupa.math import m42int, int2m4


def cells_id_fromblob(blob, bytes, p):
    """Takes bytes from blake3 excluding rightmost bit.

    Blake3 return a digest with the first byte to the left."""
    digest = blake3(blob).digest(length=bytes)
    n = int.from_bytes(digest, byteorder="big") >> 1
    cells = int2m4(n, p)
    digits = bytes + bytes // 3
    id = b64enc(n, digits)
    return cells, id


def id_fromcells(cells, digits, p):
    num = m42int(cells, p)
    id = b64enc(num, digits)
    return id


def cells_fromid(id, p):
    num = b64dec(id)
    return int2m4(num, p)
