Module garoupa.algebra.matrix.mat
=================================

Classes
-------

`Mat(i, n, mod=2)`
:   Element(i: int, order: int)
    
    nxn     modulo o
    Usage:
    
    >>> a = Mat(4783632, 6, 10)
    >>> a
    [[1 2 3 6 3 8]
     [0 1 7 4 0 0]
     [0 0 1 0 0 0]
     [0 0 0 1 0 0]
     [0 0 0 0 1 0]
     [0 0 0 0 0 1]]
    >>> a2 = a * a
    >>> a2
    [[1 4 0 0 6 6]
     [0 1 4 8 0 0]
     [0 0 1 0 0 0]
     [0 0 0 1 0 0]
     [0 0 0 0 1 0]
     [0 0 0 0 0 1]]
    >>> b = Mat(9947632, 6, 10)
    >>> a * b * a2  * ~a2 * ~b == a
    True

    ### Ancestors (in MRO)

    * garoupa.algebra.abs.element.Element
    * abc.ABC

    ### Class variables

    `i: int`
    :

    `order: int`
    :