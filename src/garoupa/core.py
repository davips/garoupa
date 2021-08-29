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

from blake3 import blake3

from garoupa.encoding import *
from garoupa.math import cells2int, int2cells


def cells_id_fromblob(blob, etype, bytes, p):
    """Takes bytes from blake3 excluding right-most bit.

    ps. Blake3 returns a digest with the most significant byte on the right.

    Usage:

    >>> cells_id_fromblob(b"sdff", "unordered", 48, 18446744073709551557)
    ([0, 0, 0, 0, 0, 12851939186879403454], 'b_25b429914de95be_______________________________________________')
    >>> cells_id_fromblob(b"sdff", "hybrid", 48, 18446744073709551557)
    ([0, 0, 11663386755101441530, 14149014035580258010, 17255310882252753130, 12851939186879403454], 'Et_cac755fd13d8adac82825b91b4671424594642a77a4a2cf9f4dabb065c5e8')
    >>> cells_id_fromblob(b"sdff", "ordered", 48, 18446744073709551557)
    ([7643518115363038250, 15715161175032162863, 11663386755101441530, 14149014035580258010, 17255310882252753129, 12851939186879403454], 'qxcXeFhW8X2tXztiqgTRlQYZYfIuM1JLZVojkHHC01nn0w6Q41ciQMx096xAv59E')
    >>> try:
    ...     cells_id_fromblob(b"sdff", "t2323rt", 48, 18446744073709551557)
    ... except Exception as e:
    ...     print(e)
    ('Unknown etype:', 't2323rt')
    """
    digest = blake3(blob).digest(length=bytes)
    n = int.from_bytes(digest, byteorder="little") >> 1
    if etype == "unordered":
        n %= p
    elif etype == "hybrid":
        n = (p + n) % p ** 4
    elif etype == "ordered":
        n = (p ** 4 + n) % p ** 6
    else:
        raise Exception("Unknown etype:", etype)  # pragma: no cover
    cells = int2cells(n, p)
    digits = 4 * bytes // 3
    return cells, id_fromcells(cells, digits, p)


def id_fromcells(cells, digits, p):
    """
    Usage based on ranges from paper:

    >>> p = 4294967291
    >>> id_fromcells([0,0,0,0,0,0], 32, p) == '00000000000000000000000000000000'
    True
    >>> id_fromcells([0,0,0,0,0,p-1], 32, p) == 'f_ffffffa_______________________'
    True
    >>> id_fromcells([0,0,0,0,1,0], 32, p) == '00_00000000000000000000000000001'
    True
    >>> res,c1 = divmod(2**120-1+p-1, p)
    >>> res,c2 = divmod(res, p)
    >>> c4,c3 = divmod(res, p)
    >>> id_fromcells([0,0,c4,c3,c2,c1], 32, p) == '0f_fffffffffffffffffffffffffffff'
    True
    >>> id_fromcells([0,0,c4,c3,c2,c1+1], 32, p) == '0g_00000000000000000000000000000'
    True
    >>> id_fromcells([0,0,p-1,p-1,p-1,p-1], 32, p) == '.._fffec00000095fffffe0b00000276'
    True
    >>> id_fromcells([0,1,0,0,0,0], 32, p) == '00000000000000000000000000000001'
    True
    >>> id_fromcells([p-1,p-1,p-1,p-1,p-1,p-1], 32, p) == '....Uw000nn...pg000A2f..Kbo003Go'
    True

    Parameters
    ----------
    cells
    digits
    p

    Returns
    -------

    """
    num = cells2int(cells, p)
    return n2id(num, digits, p)


def cells_fromid(id, p):
    """
    Usage based on ranges from paper:

    >>> p = 4294967291
    >>> cells_fromid('00000000000000000000000000000000', p) == [0,0,0,0,0,0]
    True
    >>> cells_fromid('f_ffffffa_______________________', p) == [0,0,0,0,0,p-1]
    True
    >>> cells_fromid('00_00000000000000000000000000001', p) == [0,0,0,0,1,0]
    True
    >>> res,c1 = divmod(16**30 - 1 + p - 1, p)
    >>> res,c2 = divmod(res, p)
    >>> c4,c3 = divmod(res, p)
    >>> cells_fromid('0f_fffffffffffffffffffffffffffff', p) == [0,0,c4,c3,c2,c1]
    True
    >>> cells_fromid('0g_00000000000000000000000000000', p) == [0,0,c4,c3,c2,c1+1]
    True
    >>> cells_fromid('.._fffec00000095fffffe0b00000276', p) == [0,0,p-1,p-1,p-1,p-1]
    True
    >>> cells_fromid('00000000000000000000000000000001', p) == [0,1,0,0,0,0]
    True
    >>> cells_fromid('....Uw000nn...pg000A2f..Kbo003Go', p) == [p-1,p-1,p-1,p-1,p-1,p-1]
    True

    Parameters
    ----------
    id
    p

    Returns
    -------

    """
    return int2cells(id2n(id, p), p)
