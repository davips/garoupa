Module garoupa.algebra.math
===========================
Operations with permutations

Functions
---------

    
`int2pmat(number, side)`
:   Convert number into permutation.
    
    Pads to side.
    
    Usage:
    
    >>> int2pmat(4, 4)
    [0, 2, 1, 3]
    
    Parameters
    ----------
    number
    side
    
    Returns
    -------

    
`pmat2int(matrix)`
:   Convert permutation to number.
    
    Usage:
    
    >>> pmat2int([0, 2, 1, 3])
    4
    
    Parameters
    ----------
    matrix
    
    Returns
    -------

    
`pmat_inv(m)`
:   

    
`pmat_mult(a, b)`
:   Multiply two permutations.
    
    Parameters
    ----------
    a
        list of positive integers plus zero
    b
        list of positive integers plus zero
    
    Returns
    -------

    
`pmat_transpose(m)`
:   Transpose a permutation.
    
    Original author (CC BY-SA 4.0 LICENSE):
    https://codereview.stackexchange.com/questions/241511/how-to-efficiently-fast-calculate-the-transpose-of-a-permutation-matrix-in-p/241524?noredirect=1#comment473994_241524
    
    Parameters
    ----------
    m
        list of positive integers plus zero
    
    Returns
    -------
        list of positive integers plus zero