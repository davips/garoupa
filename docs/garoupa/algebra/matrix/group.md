Module garoupa.algebra.matrix.group
===================================

Classes
-------

`Group(identity: garoupa.algebra.abs.element.Element, sorted: <built-in function callable>, seed: int = None)`
:   

    ### Descendants

    * garoupa.algebra.cyclic.z.Z
    * garoupa.algebra.cyclic.zm.Zm
    * garoupa.algebra.dihedral.d.D
    * garoupa.algebra.matrix.m.M
    * garoupa.algebra.matrix.m128bit.M128bit
    * garoupa.algebra.matrix.m8bit.M8bit
    * garoupa.algebra.product.product.Product
    * garoupa.algebra.symmetric.s.S

    ### Static methods

    `gcd(a, b)`
    :   Greatest common divisor
        
        Usage:
        
        >>> from garoupa.algebra.dihedral import D
        >>> D.gcd(32, 12)
        4
        
        Based on Gabriel Dalforno code.

    `lcm(a, b)`
    :   Least common multiple
        
        Usage:
        
        >>> from garoupa.algebra.dihedral import D
        >>> D.lcm(32, 12)
        96
        
        Based on Gabriel Dalforno code.

    ### Instance variables

    `comm_degree`
    :

    `order_hist`
    :

    `pi`
    :   Chance of stopping a repetition exactly at identity

    ### Methods

    `compact_order_hist(self, binsize, preserve_upto=0, max_histsize=inf, hist=None)`
    :   Compact histogram of element orders.
        
        Usage:
        
        >>> from garoupa.algebra.dihedral import D
        >>> (D(7) * D(19)).order_hist
        {1: 1, 2: 159, 7: 6, 14: 114, 19: 18, 38: 126, 133: 108}
        >>> (D(7) * D(19)).compact_order_hist(1)
        {1: 1, 2: 159, 7: 6, 14: 114, 19: 18, 38: 126, 133: 108}
        >>> (D(7) * D(19)).compact_order_hist(3)
        {1: 160, 7: 6, 14: 114, 19: 18, 38: 126, 133: 108}
        >>> (D(7) * D(19)).compact_order_hist(10)
        {2: 166, 14: 132, 38: 126, 133: 108}

    `compact_order_hist_lowmem(self, max_histsize, preserve_upto, initial_binsize=1)`
    :

    `pi_lowmem(self, max_histsize, preserve_upto=0, initial_binsize=1)`
    :   Approximmate Chance of stopping a repetition exactly at identity - memory-friendly

    `replace(self, *args, **kwargs)`
    :

    `sampled_commuting_freq(self, pairs=5000, runs=1000000000000, exitonhit=False)`
    :   Usage:
        
        >>> from garoupa.algebra.matrix import M
        >>> G = M(5, seed=0)
        >>> max(sorted(G.sampled_commuting_freq(pairs=1000, runs=4)))
        (272, 4000)

    `sampled_orders(self, sample=100, width=10, limit=100, logfreq=10, exitonhit=False)`
    :   Histogram of element orders. Detect identity after many repetitions
        
        Usage:
        
        >>> from garoupa.algebra.symmetric import S
        >>> tot = 0
        >>> list(S(6, seed=0).sampled_orders(sample=1, width=2))
        [{(5, 8): 1}]
        >>> for hist in S(6, seed=0).sampled_orders(width=2):
        ...     print(hist)
        {(-1, 2): 1, (1, 4): 20, (3, 6): 45, (5, 8): 34}

    `samplei(self)`
    :