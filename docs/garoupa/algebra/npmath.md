Module garoupa.algebra.npmath
=============================
Operations using numpy

Functions
---------

    
`bm2int(m)`
:   

    
`bm2int6(m)`
:   

    
`bm2int8bit(m)`
:   

    
`bm2intl(m, bits)`
:   

    
`bminv(m)`
:   

    
`bmm(a, b, mod)`
:   unitriangular matrix (modulo) multiplication

    
`bytes2bm(bs)`
:   

    
`int2bm(n)`
:   

    
`int2bm6(n)`
:   

    
`int2bm8bit(n)`
:   

    
`int2bml(n, l, bits)`
:   

    
`int2m4(n, o, l=4)`
:   Usage:
    
    >>> int2m4(4095, 4, 5)
    array([[1, 3, 3, 3, 3],
           [0, 1, 3, 3, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]], dtype=uint64)

    
`int2ml(n, o, l)`
:   Usage:
    
    >>> from numpy import uint64
    >>> int2ml(4095, 4, 5)
    array([[1, 3, 3, 3, 3],
           [0, 1, 3, 3, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1]], dtype=uint64)

    
`m2intl(m, o)`
:   Usage:
    
    >>> from numpy import array, uint8
    >>> m = array([[1, 3, 3, 3, 3],
    ...            [0, 1, 3, 3, 0],
    ...            [0, 0, 1, 0, 0],
    ...            [0, 0, 0, 1, 0],
    ...            [0, 0, 0, 0, 1]], dtype=np.uint64)
    >>> m2intl(m, 4)
    4095

    
`m42int(m, o)`
:   Usage:
    
    >>> from numpy import array, uint8
    >>> m = array([[1, 3, 3, 3, 3],
    ...            [0, 1, 3, 3, 0],
    ...            [0, 0, 1, 0, 0],
    ...            [0, 0, 0, 1, 0],
    ...            [0, 0, 0, 0, 1]], dtype=np.uint64)
    >>> m42int(m, 4)
    4095

    
`m4inv(m, o)`
:   

    
`m4m(a, b, mod)`
:   unitriangular matrix (modulo) multiplication