Module garoupa.algebra.product.product
======================================

Classes
-------

`Product(*groups, seed=None)`
:   

    ### Ancestors (in MRO)

    * garoupa.algebra.matrix.group.Group

    ### Static methods

    `order_hist_mul(hista, histb)`
    :   Histogram of element orders for a product of 2 groups.
        
        Usage:
        
        >>> from garoupa.algebra.dihedral import D
        >>> Product.order_hist_mul(D(5).order_hist, D(7).order_hist)
        {1: 1, 2: 47, 5: 4, 7: 6, 10: 28, 14: 30, 35: 24}
        
        Based on Gabriel Dalforno code.

    ### Instance variables

    `comm_degree`
    :

    `order_hist`
    :   Sorted histogram of element orders.
        
        Usage:
        
        >>> from garoupa.algebra.dihedral import D
        >>> (D(3) * D(5) * D(7)).order_hist
        {1: 1, 2: 191, 3: 2, 5: 4, 6: 94, 7: 6, 10: 124, 14: 138, 15: 8, 21: 12, 30: 56, 35: 24, 42: 60, 70: 72, 105: 48}

    ### Methods

    `compact_order_hist_lowmem(self, max_histsize, preserve_upto, initial_binsize=1, show_timestamp=True)`
    :   Memory-friendly histogram of element orders in a direct product
        
        Compact largest intermediate histograms during calculation to avoid memory exhaustion.
        Nested products will also be processed through this method.
        Final and temporary hist may exceed max_histsize by a factor of 2 at most.
        
        Usage:
        
        >>> from garoupa.algebra.dihedral import D
        >>> Product.order_hist_mul(D(7).order_hist, D(19).order_hist)
        {1: 1, 2: 159, 7: 6, 14: 114, 19: 18, 38: 126, 133: 108}
        >>> G = D(3) * D(5) * D(7) * D(9)
        >>> G.compact_order_hist(binsize=20)
        {9: 7936, 29: 1064, 42: 1176, 69: 1044, 90: 1080, 105: 192, 126: 1188, 210: 576, 315: 432, 630: 432}
        >>> G.compact_order_hist_lowmem(max_histsize=5, preserve_upto=0, show_timestamp=False)  # doctest: +NORMALIZE_WHITESPACE
        Pi: 0.28944444444444445         Hist size: 7     False  D3*D5 [1] [1]
        Pi: 0.1997278911564626  Hist size: 10    False  D3*D5*D7 [2] [1]
        Pi: 0.09817901234567901         Hist size: 12    False  D3*D5*D7*D9 [4] [1]
        {3: 1134, 6: 3402, 9: 2268, 10: 2020, 30: 1076, 35: 84, 70: 1476, 90: 1548, 105: 312, 210: 576, 315: 792, 630: 432}
        >>> G.compact_order_hist_lowmem(max_histsize=5, preserve_upto=10, show_timestamp=False)  # doctest: +NORMALIZE_WHITESPACE
        Pi: 0.28944444444444445         Hist size: 7     False  D3*D5 [1] [1]
        Pi: 0.17061791383219957         Hist size: 15    False  D3*D5*D7 [2] [1]
        Pi: 0.11385896951373144         Hist size: 24    False  D3*D5*D7*D9 [4] [1]
        {1: 1, 2: 1919, 3: 8, 5: 4, 6: 1600, 9: 18, 10: 36, 12: 3240, 15: 8, 18: 1746, 21: 36, 30: 672, 35: 24, 36: 1620, 42: 828, 45: 24, 63: 72, 70: 936, 90: 336, 105: 192, 126: 360, 210: 576, 315: 432, 630: 432}

    `replace(self, *args, **kwargs)`
    :