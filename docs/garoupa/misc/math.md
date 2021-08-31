Module garoupa.misc.math
========================
Pure Python linear algebra module

Functions
---------

    
`cells2int(m, mod)`
:   Convert cells representing a 4x4 unitriangular matrix to an integer.
    
    Usage:
    
    >>> n = 986723489762345987253897254295863
    >>> cells2int(int2cells(n, 4294967291), 4294967291) == n
    True
    
    Parameters
    ----------
    m
        List with six values
    mod
        Large prime number
    
    Returns
    -------
        Lexicographic rank of the element (at least according to the disposition of cells adopted here)

    
`cellsinv(m, mod)`
:   Inverse of unitriangular matrix modulo 'mod'
    
    'm' given as a list in the format: [a5, a4, a3, a2, a1, a0]
    
    1 a4 a1 a0
    0  1 a2 a3
    0  0  1 a5
    0  0  0  1
    
    Based on https://groupprops.subwiki.org/wiki/Unitriangular_matrix_group:UT(4,p)
    
    >>> e = [42821,772431,428543,443530,42121,7213]
    >>> cellsinv(cellsinv(e, 4294967291), 4294967291)==e
    True
    
    Parameters
    ----------
    m
        List with six values
    mod
        Large prime number
    
    Returns
    -------
        The list that corresponds to the inverse element

    
`cellsmul(a, b, mod)`
:   Multiply two unitriangular matrices 4x4 modulo 'mod'.
    
    'a' and 'b' given as lists in the format: [a5, a4, a3, a2, a1, a0]
    
    1 a4 a1 a0
    0  1 a2 a3
    0  0  1 a5
    0  0  0  1
    
    >>> a, b = [51,18340,56,756,456,344], [781,2340,9870,1234,9134,3134]
    >>> cellsmul(b, cellsinv(b, 4294967291), 4294967291) == [0,0,0,0,0,0]
    True
    >>> c = cellsmul(a, b, 4294967291)
    >>> cellsmul(c, cellsinv(b, 4294967291), 4294967291) == a
    True
    
    Parameters
    ----------
    a
        List with six values
    b
        Another (or the same) list with six values
    mod
        Large prime number
    
    Returns
    -------
        The list that corresponds to the resulting element from multiplication

    
`int2cells(num, mod)`
:   Convert an integer to cells representing a 4x4 unitriangular matrix
    
    >>> e = [42821,772431,428543,443530,42121,7213]
    >>> e == int2cells(cells2int(e,4294967291), 4294967291)
    True
    >>> try:
    ...     int2cells(-1, 10)
    ... except Exception as e:
    ...     print(e)
    Number -1 too large for given mod 10
    
    Parameters
    ----------
    num
    mod
    
    Returns
    -------