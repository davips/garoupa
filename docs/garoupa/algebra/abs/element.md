Module garoupa.algebra.abs.element
==================================

Classes
-------

`Element(i: int, order: int)`
:   Element(i: int, order: int)

    ### Ancestors (in MRO)

    * abc.ABC

    ### Descendants

    * garoupa.algebra.cyclic.nat.Nat
    * garoupa.algebra.cyclic.natm.Natm
    * garoupa.algebra.dihedral.dr.Dr
    * garoupa.algebra.dihedral.ds.Ds
    * garoupa.algebra.matrix.mat.Mat
    * garoupa.algebra.matrix.mat128bit.Mat128bit
    * garoupa.algebra.matrix.mat8bit.Mat8bit
    * garoupa.algebra.product.tuple.Tuple
    * garoupa.algebra.symmetric.perm.Perm

    ### Class variables

    `i: int`
    :

    `order: int`
    :

    ### Instance variables

    `hosh`
    :   Usage:
        
        >>> from garoupa.algebra.dihedral import Ds
        >>> Ds(64**2,64**5).hosh.id
        '0_0001000_______________________'

    `id`
    :   Usage:
        
        >>> from garoupa.algebra.dihedral import Ds
        >>> Ds(64**2,64**5).id
        '0_0001000_______________________'