Module garoupa.misc.identity
============================
Some shortcuts to the null operand and to ease creating elements

Classes
-------

`Identity(version, etype_inducer='ordered')`
:   Identity element
    
    An Identity object is an innocuous identifier that represents a real world process that does nothing,
    or an empty data structure.
    It is also useful as a shortcut to coerce some Python values directly to a Hosh object through multiplication.
    
    Parameters
    ----------
    version
        UT32.4 or UT64.4 changes the number of digits and robustness against collisions
    etype_inducer
        Element type of a future multiplication by a raw Python value: 'unordered', 'ordered', 'hybrid'

    ### Ancestors (in MRO)

    * garoupa.hosh.Hosh

    ### Descendants

    * garoupa.misc.identity.Ø
    * garoupa.misc.identity.ø

    ### Instance variables

    `h`
    :   Shortcut to induce etype=hybrid in the next operand, when it is given as a bytes object.
        default=Ordered, h=Hybrid and u=Unordered
        
        Usage:
        
        >>> from garoupa import Hosh, ø, Ø
        >>> a = ø.h * b"654"
        >>> print(a)
        rf_a6340cfb8d0a6b7451ecb1a8317a1
        >>> b = Ø.h * b"654"
        >>> print(b)
        rh_dc705c5c6cff41d8fe4f49956e425b275f3c091372d4a0ba8c673caa46edc
        >>> Hosh(b"654", "hybrid", "UT32.4") == a and b == Hosh(b"654","hybrid", "UT64.4")
        True

    `u`
    :   Shortcut to induce etype=unordered in the next operand, when it is not a ready Hosh object.
        default=Ordered, h=Hybrid and u=Unordered
        
        Usage:
        
        >>> from garoupa import ø, Ø, Hosh
        >>> a = ø.u * b"654"
        >>> print(a)
        2_e2b898e_______________________
        >>> b = Ø.u * b"654"
        >>> print(b)
        f_ec361e9ebb223fc_______________________________________________
        >>> Hosh(b"654", "unordered", "UT32.4") == a and b == Hosh(b"654","unordered", "UT64.4")
        True

`Ø(etype_inducer='ordered')`
:   64-digit identity element
    
    An Identity object is an innocuous identifier that represents a real world process that does nothing,
    or an empty data structure.
    It is also useful as a shortcut to coerce some Python values directly to a Hosh object through multiplication.
    
    Normal usage (as an already instantiated object:
    
    >>> from garoupa import Ø
    >>> Ø.id
    '0000000000000000000000000000000000000000000000000000000000000000'
    >>> print(Ø * 872696823986235926596245)
    00_00000000000000000000000000000000000000000b8cbfd58058b15174ad1
    
    Parameters
    ----------
    etype_inducer
        Element type of a future multiplication by a raw Python value: 'unordered', 'ordered', 'hybrid'

    ### Ancestors (in MRO)

    * garoupa.misc.identity.Identity
    * garoupa.hosh.Hosh

`ø(etype_inducer='ordered')`
:   32-digit identity element
    
    An Identity object is an innocuous identifier that represents a real world process that does nothing,
    or an empty data structure.
    It is also useful as a shortcut to coerce some Python values directly to a Hosh object through multiplication.
    
    Normal usage (as an already instantiated object:
    
    >>> from garoupa import ø
    >>> ø.id
    '00000000000000000000000000000000'
    >>> print(ø * 872696823986235926596245)
    00_000000000b8ccfd58058a15174a9b
    
    Parameters
    ----------
    etype_inducer
        Element type of a future multiplication by a raw Python value: 'unordered', 'ordered', 'hybrid'

    ### Ancestors (in MRO)

    * garoupa.misc.identity.Identity
    * garoupa.hosh.Hosh