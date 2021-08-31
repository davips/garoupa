Module garoupa.algebra.cyclic.nat
=================================

Classes
-------

`Nat(i, n)`
:   Usage:
    
    >>> a = Nat(1414343245,2**32)
    >>> b = Nat(77639,2**32)
    >>> b
    77639
    >>> ~b
    4294889657
    >>> a * b
    1414420884
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