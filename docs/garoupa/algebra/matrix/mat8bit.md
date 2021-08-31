Module garoupa.algebra.matrix.mat8bit
=====================================

Classes
-------

`Mat8bit(i)`
:   Element(i: int, order: int)
    
    17x17 with 8 zeros to match 128 bits.
    
    Usage:
    
    >>> a = Mat8bit(127)
    >>> b = Mat8bit(88)
    >>> a * b
    [[1. 0. 0. 0. 1.]
     [0. 1. 0. 0. 1.]
     [0. 0. 1. 1. 1.]
     [0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 1.]]
    >>> (a * b) * ~b == a
    True

    ### Ancestors (in MRO)

    * garoupa.algebra.abs.element.Element
    * abc.ABC

    ### Class variables

    `i: int`
    :

    `order: int`
    :