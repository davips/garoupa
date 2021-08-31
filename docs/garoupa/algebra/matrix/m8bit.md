Module garoupa.algebra.matrix.m8bit
===================================

Classes
-------

`M8bit(seed=None)`
:   Usage:
    
    >>> G = M8bit(seed=0)
    >>> G, ~G
    (M8bit, [[1. 0. 1. 1. 0.]
     [0. 1. 1. 1. 0.]
     [0. 0. 1. 0. 0.]
     [0. 0. 0. 1. 0.]
     [0. 0. 0. 0. 1.]])

    ### Ancestors (in MRO)

    * garoupa.algebra.matrix.group.Group

    ### Methods

    `replace(self, *args, **kwargs)`
    :   Usage:
        
        >>> G = M8bit(seed=0)
        >>> ~G.replace(seed=1)
        [[1. 0. 0. 0. 1.]
         [0. 1. 0. 0. 0.]
         [0. 0. 1. 1. 0.]
         [0. 0. 0. 1. 0.]
         [0. 0. 0. 0. 1.]]