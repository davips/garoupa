Module garoupa.algebra.cyclic.zm
================================

Classes
-------

`Zm(n, seed=None)`
:   Usage:
    
    >>> G = Zm(1414343245, seed=0)
    >>> G.comm_degree
    1
    >>> G, ~G
    (Zm1414343245, 906691059)

    ### Ancestors (in MRO)

    * garoupa.algebra.matrix.group.Group

    ### Instance variables

    `comm_degree`
    :   Exact commutativity degree

    ### Methods

    `replace(self, *args, **kwargs)`
    :   Usage:
        
        >>> G = Zm(1414343245, seed=0)
        >>> ~G.replace(seed=1)
        144272509