Module garoupa.algebra.cyclic.natm
==================================

Classes
-------

`Natm(i, n)`
:   Usage:
    
    >>> a = Natm(1414343245, 2**32)
    >>> b = Natm(77639, 2**32)
    >>> b
    77639
    >>> ~b
    3006515831
    >>> a * b
    3061309019
    >>> a * b * ~b == a
    True

    ### Ancestors (in MRO)

    * garoupa.algebra.abs.element.Element
    * abc.ABC

    ### Class variables

    `i: int`
    :

    `order: int`
    :