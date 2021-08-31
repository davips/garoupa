Module garoupa
==============
GaROUPa solves the problem of determining the identity of multi-valued objects or sequences of events
(and provide extra modules for group theory)

Sub-modules
-----------
* garoupa.algebra
* garoupa.misc

Variables
---------

    
`identity32`
:   Shortcut to the 32-digit identity Hosh object

    
`identity64`
:   Shortcut to the 64-digit identity Hosh object

    
`Ø`
:   Shortcut to the 64-digit identity Hosh object

    
`ø`
:   Shortcut to the 32-digit identity Hosh object

    
`Ħ`
:   Shortcut to create 64-digit Hosh objects

    
`ħ`
:   Shortcut to create 32-digit Hosh objects

Classes
-------

`Hosh(content, etype='default:ordered', version='UT32.4')`
:   Operable hash.
    
    Generate a Hosh object from a binary content or a list of 6 ints.
    
    Usage:
    
    >>> from garoupa import Hosh
    >>> a = Hosh(b"lots of data")
    >>> b = Hosh(b"lots of data 2")
    >>> a.id
    '2Lo3TSO03yIBqYTFR6NKjKdC.oLyb0-.'
    >>> b.id
    'lxqpsidKkkGXHiZg7h7aCUy-eI5esBXS'
    >>> (a * b).id
    'ogOtjU.KnU-CpQqQouvwxhalU2VNUqC-'
    >>> (b * a).id
    'ogOtjU.KnUY7mBeDIWEuE2OzLo9i44B0'
    >>> a * b * ~b == a
    True
    >>> c = Hosh(b"lots of data 3")
    >>> (a * b) * c == a * (b * c)
    True
    >>> e = Hosh(b"lots of data 4")
    >>> f = Hosh(b"lots of data 5")
    >>> e * f != f * e
    True
    >>> a * b != b * a
    True
    >>> x = Hosh(b"lots of data 6", "hybrid")
    >>> y = Hosh(b"lots of data 7", "hybrid")
    >>> z = Hosh(b"lots of data 8", "unordered")
    >>> x * y == y * x
    True
    >>> x * a != a * x
    True
    >>> x * z == z * x
    True
    >>> a * z == z * a
    True
    >>> from garoupa import ø, Ø
    >>> print(ø)  # Handy syntax using ø or Ø for identity.
    00000000000000000000000000000000
    >>> print(ø * "7ysdf98ysdf98ysdf98ysdfysdf98ysd")  # str, bytes or int are converted as id, blob or element rank.
    7ysdf98ysdf98ysdf98ysdfysdf98ysd
    >>> print(ø * "7ysdf98ysdf98ysdf98ysdfysdf98ysd" * "6gdsf76df8gaf87gaf87gaf87agdfa78")
    dOFFu0eLHn4nHvqBpdWh3iN-8PnC1PO6
    >>> print(Ø)  # Version UT64.4
    0000000000000000000000000000000000000000000000000000000000000000
    >>> Ø.h * b"sdff" == Hosh(b"sdff","hybrid","UT64.4")  # etype=hybrid
    True
    >>> print(ø.u * b"sdff")
    3_214e6b0_______________________
    
    Parameters
    ----------
    content
        Binary content to be hashed, or a list of six integers
    etype
        ordered, hybrid, unordered
        According to the subset of the desired element: Z, H\Z or G\H
    version
        UT32.4 or UT64.4 changes the number of digits and robustness against collisions
        UT32.4 is enough for most usages. It accepts more than 4 billion repetitions of the same operation in a row.
        UT64.4 provides unspeakable limits for operations, please see scientific paper for details.

    ### Descendants

    * garoupa.misc.identity.Identity

    ### Class variables

    `shorter`
    :

    ### Static methods

    `fromid(id)`
    :   Usage:
        
        >>> a = Hosh.fromid("abcdefabcdefabcdefabcdefabcdefab")
        >>> a.n
        997946887123826552569543664509734108513592617499281126651
        >>> a.cells
        [682822972, 3959913371, 1088646845, 1948924621, 2273369721, 2635491741]
        >>> a.etype
        'ordered'
        >>> bid = a.id[:2] + "_" + a.id[3:]
        >>> bid
        'ab_defabcdefabcdefabcdefabcdefab'
        >>> b = Hosh.fromid(bid)
        >>> b.id
        'ab_defabcdefabcdefabcdefabcdefab'
        >>> b.n
        54155325045304951634162463017274306469
        >>> b.cells
        [0, 0, 683536302, 823178997, 3937254300, 1531888570]
        >>> b.etype
        'hybrid'
        >>> Hosh.fromid("0000000000000000000000000000000000000000000000000000000000000000") == 0
        True
        
        Parameters
        ----------
        id

    `fromn(n: int, version='UT32.4')`
    :   Hosh representing the given int.
        
        Default 'p' is according to version UT64.4.
        
        Usage:
        
        >>> h = Hosh.fromn(7647544756746324134134)
        >>> h.id
        '00_000000000019e9300ddd405c1c8fc'

    `group_props(version)`
    :   Usage:
        
        >>> from garoupa import Hosh
        >>> Hosh.group_props("UT32.4")
        (4294967291, 6277101691541631771514589274378639120656724268335671295241, 32, 24)
        
        Parameters
        ----------
        version
        
        Returns
        -------

    ### Instance variables

    `etype`
    :   Usage:
        
        >>> from garoupa import Hosh
        >>> Hosh.fromn(5).etype
        'unordered'
        
        Returns
        -------

    `etype_inducer`
    :   Usage:
        
        >>> from garoupa import ø, Hosh
        >>> ø.etype_inducer
        'ordered'
        >>> ø.h.etype_inducer
        'hybrid'
        >>> ø.u.etype_inducer
        'unordered'
        >>> Hosh(b"12124").etype_inducer
        'ordered'
        
        Returns
        -------

    `id`
    :

    `idc`
    :

    `n`
    :

    `sid`
    :   Shorter id (base-922 using up to 2 bytes utf8 per char)
        
        Usage:
        
        >>> from garoupa import ø
        >>> (ø * b'65e987978g').sid
        'ĐãǚħHȩСЭĵʙĞŸιśԵəжʐƙö'
        
        >>> from garoupa import Ø
        >>> (Ø * b'65e987978g').sid
        'ÊŰԝǮʎĹաΦƟzƶӣξʙСʠΠмΌВʜȉΖáςՔĦĢνԱCϔΘҳȖưΎìɚF'
        
        Returns
        -------

    `sidc`
    :   Shorter colored id (base-922 using up to 2 bytes utf8 per char)
        
        Usage:
        
        >>> from garoupa import ø
        >>> print((ø * b'65e987978g').sidc)
        [38;5;75m[1m[48;5;0mĐ[0m[38;5;117m[1m[48;5;0mã[0m[38;5;159m[1m[48;5;0mǚ[0m[38;5;153m[1m[48;5;0mħ[0m[38;5;117m[1m[48;5;0mH[0m[38;5;159m[1m[48;5;0mȩ[0m[38;5;194m[1m[48;5;0mС[0m[38;5;146m[1m[48;5;0mЭ[0m[38;5;74m[1m[48;5;0mĵ[0m[38;5;81m[1m[48;5;0mʙ[0m[38;5;117m[1m[48;5;0mĞ[0m[38;5;158m[1m[48;5;0mŸ[0m[38;5;146m[1m[48;5;0mι[0m[38;5;73m[1m[48;5;0mś[0m[38;5;109m[1m[48;5;0mԵ[0m[38;5;74m[1m[48;5;0mə[0m[38;5;75m[1m[48;5;0mж[0m[38;5;117m[1m[48;5;0mʐ[0m[38;5;159m[1m[48;5;0mƙ[0m[38;5;153m[1m[48;5;0mö[0m
        
        >>> from garoupa import Ø
        >>> print((Ø * b'65e987978g').sidc)
        [38;5;249m[1m[48;5;0mÊ[0m[38;5;249m[1m[48;5;0mŰ[0m[38;5;144m[1m[48;5;0mԝ[0m[38;5;144m[1m[48;5;0mǮ[0m[38;5;246m[1m[48;5;0mʎ[0m[38;5;109m[1m[48;5;0mĹ[0m[38;5;146m[1m[48;5;0mա[0m[38;5;150m[1m[48;5;0mΦ[0m[38;5;182m[1m[48;5;0mƟ[0m[38;5;150m[1m[48;5;0mz[0m[38;5;179m[1m[48;5;0mƶ[0m[38;5;137m[1m[48;5;0mӣ[0m[38;5;104m[1m[48;5;0mξ[0m[38;5;119m[1m[48;5;0mʙ[0m[38;5;175m[1m[48;5;0mС[0m[38;5;109m[1m[48;5;0mʠ[0m[38;5;249m[1m[48;5;0mΠ[0m[38;5;249m[1m[48;5;0mм[0m[38;5;144m[1m[48;5;0mΌ[0m[38;5;144m[1m[48;5;0mВ[0m[38;5;246m[1m[48;5;0mʜ[0m[38;5;109m[1m[48;5;0mȉ[0m[38;5;146m[1m[48;5;0mΖ[0m[38;5;150m[1m[48;5;0má[0m[38;5;182m[1m[48;5;0mς[0m[38;5;150m[1m[48;5;0mՔ[0m[38;5;179m[1m[48;5;0mĦ[0m[38;5;137m[1m[48;5;0mĢ[0m[38;5;104m[1m[48;5;0mν[0m[38;5;119m[1m[48;5;0mԱ[0m[38;5;175m[1m[48;5;0mC[0m[38;5;109m[1m[48;5;0mϔ[0m[38;5;249m[1m[48;5;0mΘ[0m[38;5;249m[1m[48;5;0mҳ[0m[38;5;144m[1m[48;5;0mȖ[0m[38;5;144m[1m[48;5;0mư[0m[38;5;246m[1m[48;5;0mΎ[0m[38;5;109m[1m[48;5;0mì[0m[38;5;146m[1m[48;5;0mɚ[0m[38;5;150m[1m[48;5;0mF[0m
        
        Returns
        -------

    ### Methods

    `convert(self, other)`
    :   Usage:
        
        >>> from garoupa import ø
        >>> ø.convert([0,0,0,0,0,0]).id
        '00000000000000000000000000000000'
        
        >>> from garoupa import Hosh
        >>> ø.convert(0).id
        '00000000000000000000000000000000'
        
        Parameters
        ----------
        other
        
        Returns
        -------

    `short(self, colored=True)`
    :   Usage:
        
        >>> Hosh(b"asdf86fasd").short(colored=False)
        çÙkƝĜưŔнǒēòƣσåŴQӀՏмŷ

    `show(self, colored=True)`
    :   Usage:
        
        >>> Hosh(b"asdf86fasd").show(colored=False)
        8nsZouodGbQ5.9OUrypqCzmYrK1t8hov