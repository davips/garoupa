Module garoupa.misc.core
========================
Hashing and conversion functions used by Hosh

This file exists to facilitate implementation of a compiled faster version in the sister package 'hosh'.
However, the performance of garoupa seems already very high, making the 'rust' implementation not necessary.

Functions
---------

    
`blake3(...)`
:   Construct an incremental hasher object, which can accept any number of
    writes. The interface is similar to `hashlib.blake2b` or `hashlib.md5`
    from the standard library.
    
    Positional arguments:
    - `data` (optional): Input bytes to hash. This is equivalent to calling
      `update` on the returned hasher.
    
    Keyword arguments:
    - `key`: A 32-byte key. Setting this to non-None enables the keyed
      hashing mode.
    - `context`: A context string. Setting this to non-None enables the key
      derivation mode. Context strings should be hardcoded, globally
      unique, and application-specific. `context` and `key` cannot be used
      at the same time.
    - `multithreading`: See the `multithreading` argument on the `update`
      method. This flag only applies to this one function call. It is not a
      persistent setting, and it has no effect if `data` is omitted.

    
`cells_fromid(id, p)`
:   Usage based on ranges from paper:
    
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
        Textual digest
    p
        A big prime number compatible with the amount of bytes, to convert the hash to six cells for a 4x4 matrix
        according to the paper
    
    Returns
    -------
        Six cells for a 4x4 matrix, according to the paper

    
`cells_id_fromblob(blob, etype, nbytes, p)`
:   Takes bytes from blake3, excluding right-most bit, to produce cells and string id.
    
    ps. Blake3 returns a digest with the most significant byte on the right.
    
    Usage:
    
    >>> cells_id_fromblob(b"sdff", "unordered", 48, 18446744073709551557)
    ([0, 0, 0, 0, 0, 12851939186879403454], 'b_25b429914de95be_______________________________________________')
    >>> cells_id_fromblob(b"sdff", "hybrid", 48, 18446744073709551557)
    ([0, 0, 11663386755101441530, 14149014035580258010, 17255310882252753130, 12851939186879403454], 'Et_cac755fd13d8adac82825b91b4671424594642a77a4a2cf9f4dabb065c5e8')
    >>> cells_id_fromblob(b"sdff", "ordered", 48, 18446744073709551557)
    ([7643518115363038250, 15715161175032162863, 11663386755101441530, 14149014035580258010, 17255310882252753129, 12851939186879403454], 'qxcXeFhW8X2tXztiqgTRlQYZYfIuM1JLZVojkHHC01nn0w6Q41ciQMx096xAv59E')
    
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

    
`id_fromcells(cells, digits, p)`
:   Usage based on ranges from paper:
    
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
        Six cells for a 4x4 matrix, according to the paper
    digits
        Number of digits of the identifier
    p
        A big prime number compatible with the amount of bytes, to convert the hash to six cells for a 4x4 matrix
        according to the paper
    Returns
    -------
        Textual digest