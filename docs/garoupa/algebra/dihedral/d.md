Module garoupa.algebra.dihedral.d
=================================

Classes
-------

`D(n, seed=None)`
:   Usage:
    
    >>> G = D(1414343245, seed=0)
    >>> round(G.comm_degree, 2)
    0.25
    >>> G, ~G, G^2
    (D1414343245, ds1627694678, D1414343245×D1414343245)

    ### Ancestors (in MRO)

    * garoupa.algebra.matrix.group.Group

    ### Instance variables

    `comm_degree`
    :   Exact commutativity degree

    `order_hist`
    :   Sorted histogram of element orders.
        
        Based on Gabriel Dalforno code.
        
        Usage:
        
        >>> D(7).order_hist
        {1: 1, 2: 7, 7: 6}

    ### Methods

    `euler(self, d)`
    :   Euler Totient Function
        Based on Gabriel Dalforno code.

    `replace(self, *args, **kwargs)`
    :   Usage:
        
        >>> G = D(1414343245, seed=0)
        >>> ~G.replace(seed=1)
        dr1222356005