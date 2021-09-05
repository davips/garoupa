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
#  part of this work is illegal and unethical regarding the effort and
#  time spent here.
"""Hashing and conversion functions used by Hosh

This file exists to facilitate implementation of a compiled faster version in the sister package 'hosh'.
However, the performance of GaROUPa seems already very high, making the 'rust' implementation not necessary."""

from blake3 import blake3

from garoupa.misc.encoding.base import n2id, id2n
from garoupa.misc.exception import WrongEType
from garoupa.misc.math import cells2int, int2cells


def cells_id_fromblob(blob, etype, nbytes, p):
    """
    Takes bytes from blake3, excluding right-most bit, to produce cells and string id.

    ps. Blake3 returns a digest with the most significant byte on the right.

    Usage:

    >>> cells_id_fromblob(b"sdff", "unordered", 48, 18446744073709551557)
    ([0, 0, 0, 0, 0, 12851939186879403454], 'b_eb59ed419924b52_______________________________________________')
    >>> cells_id_fromblob(b"sdff", "hybrid", 48, 18446744073709551557)
    ([0, 0, 11663386755101441530, 14149014035580258010, 17255310882252753130, 12851939186879403454], 'tE_8e5c560bbad4f9fc2a4a77a2464954241764b19b52828cada8d31df557cac')
    >>> cells_id_fromblob(b"sdff", "ordered", 48, 18446744073709551557)
    ([7643518115363038250, 15715161175032162863, 11663386755101441530, 14149014035580258010, 17255310882252753129, 12851939186879403454], 'E95vAx690xMQic14Q6w0nn10CHHkjoVZLJ1MuIfYZYQlRTgqitzXt2X8WhFeXcxq')

    Parameters
    ----------
    blob
        Bytes object
    etype
        Type of element: 'unordered', 'ordered', 'hybrid'
    nbytes
        Number of bytes to keep from blake3
    p
        A big prime number compatible with the amount of bytes, to convert the hash to six cells for a 4x4 matrix
        according to the paper.

    Returns
    -------
    The name says it all
    """
    digest = blake3(blob).digest(length=nbytes)
    n = int.from_bytes(digest, byteorder="little") >> 1
    if etype == "unordered":
        n %= p
    elif etype == "hybrid":
        n = (p + n) % p ** 4
    elif etype == "ordered":
        n = (p ** 4 + n) % p ** 6
    else:
        raise WrongEType("Unknown etype:", etype)
    cells = int2cells(n, p)
    digits = 4 * nbytes // 3
    return cells, id_fromcells(cells, digits, p)


def id_fromcells(cells, digits, p):
    """
    Usage based on ranges from paper:

    >>> p = 4294967291
    >>> id_fromcells([0,0,0,0,0,0], 32, p) == '00000000000000000000000000000000'
    True
    >>> id_fromcells([0,0,0,0,0,p-1], 32, p) == 'f_affffff_______________________'
    True
    >>> id_fromcells([0,0,0,0,1,0], 32, p) == '00_10000000000000000000000000000'
    True
    >>> res,c1 = divmod(2**120-1+p-1, p)
    >>> res,c2 = divmod(res, p)
    >>> c4,c3 = divmod(res, p)
    >>> id_fromcells([0,0,c4,c3,c2,c1], 32, p) == 'f0_fffffffffffffffffffffffffffff'
    True
    >>> id_fromcells([0,0,c4,c3,c2,c1+1], 32, p) == 'g0_00000000000000000000000000000'
    True
    >>> id_fromcells([0,0,p-1,p-1,p-1,p-1], 32, p) == '.._67200000b0efffff59000000cefff'
    True
    >>> id_fromcells([0,1,0,0,0,0], 32, p) == '10000000000000000000000000000000'
    True
    >>> id_fromcells([p-1,p-1,p-1,p-1,p-1,p-1], 32, p) == 'oG300obK..f2A000gp...nn000wU....'
    True

    Parameters
    ----------
    cells
        Six cells for a 4x4 matrix, according to the paper
    digits
        Number of digits of the identifier
    p
        A big prime number compatible with the amount of bytes, to convert the hash to six cells for a 4x4 matrix
        according to the paper
    Returns
    -------
        Textual digest

    """
    num = cells2int(cells, p)
    return n2id(num, digits, p)


def cells_fromid(id, p):
    """
    Usage based on ranges from paper:

    >>> p = 4294967291
    >>> cells_fromid('00000000000000000000000000000000', p) == [0,0,0,0,0,0]
    True
    >>> cells_fromid('f_affffff_______________________', p) == [0,0,0,0,0,p-1]
    True
    >>> cells_fromid('00_10000000000000000000000000000', p) == [0,0,0,0,1,0]
    True
    >>> res,c1 = divmod(16**30 - 1 + p - 1, p)
    >>> res,c2 = divmod(res, p)
    >>> c4,c3 = divmod(res, p)
    >>> cells_fromid('f0_fffffffffffffffffffffffffffff', p) == [0,0,c4,c3,c2,c1]
    True
    >>> cells_fromid('g0_00000000000000000000000000000', p) == [0,0,c4,c3,c2,c1+1]
    True
    >>> cells_fromid('.._67200000b0efffff59000000cefff', p) == [0,0,p-1,p-1,p-1,p-1]
    True
    >>> cells_fromid('10000000000000000000000000000000', p) == [0,1,0,0,0,0]
    True
    >>> cells_fromid('oG300obK..f2A000gp...nn000wU....', p) == [p-1,p-1,p-1,p-1,p-1,p-1]
    True

    Parameters
    ----------
    id
        Textual digest
    p
        A big prime number compatible with the amount of bytes, to convert the hash to six cells for a 4x4 matrix
        according to the paper

    Returns
    -------
        Six cells for a 4x4 matrix, according to the paper
    """
    return int2cells(id2n(id, p), p)
