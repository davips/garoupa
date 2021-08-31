Module garoupa.misc.helper
==========================
Just shortcuts

Classes
-------

`Helper(version: str)`
:   Internal use only.
    
    Not to be directly instantiated.

    ### Class variables

    `version: str`
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

    ### Methods

    `h(self, blob)`
    :

    `u(self, blob)`
    :