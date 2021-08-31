Module garoupa.algebra.cyclic.z
===============================

Classes
-------

`Z(n, seed=None)`
:   Usage:
    
    >>> G = Z(1414343245, seed=0)
    >>> G.comm_degree
    1
    >>> G, ~G
    (Z1414343245, 906691059)

    ### Ancestors (in MRO)

    * garoupa.algebra.matrix.group.Group

    ### Instance variables

    `comm_degree`
    :   Exact commutativity degree

    ### Methods

    `replace(self, *args, **kwargs)`
    :   Usage:
        
        >>> G = Z(1414343245, seed=0)
        >>> ~G.replace(seed=1)
        144272509