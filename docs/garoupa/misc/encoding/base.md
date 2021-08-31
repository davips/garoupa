Module garoupa.misc.encoding.base
=================================
Different bases to compose an identifier string

Functions
---------

    
`dec(string, ralphabet)`
:   Usage:
    
    >>> dec("aa", ralphabet=b64r) == 10 * 64 + 10
    True
    
    Parameters
    ----------
    ralphabet
    string
    
    Returns
    -------

    
`enc(num, alphabet, digits)`
:   Usage:
    
    >>> enc(123456, b64, 10)
    '0000000u90'
    >>> n = dec(enc(123456, b64, 10), b64r)
    >>> n == 123456
    True
    >>> try:
    ...     enc(-1, b64, 10)
    ... except Exception as e:
    ...     print(e)
    Cannot encode negative number -1

    
`id2n(id, p)`
:   Usage:
    
    >>> p = 4294967291
    >>> id2n("00000000000000000000000000000000",p)              # Identity
    0
    >>> id2n("0_0000001_______________________",p)              # First unordered
    1
    >>> id2n("0_fffffff_______________________",p) == 16**7 - 1
    True
    >>> id2n("f_ffffffa_______________________",p) == p - 1     # Last unordered
    True
    >>> id2n("00_00000000000000000000000000001",p)              # First hybrid
    4294967291
    >>> id2n(".._fffec00000095fffffe0b00000276",p) == p**4-1    # Last hybrid
    True
    >>> id2n("00000000000000000000000000000001",p) == p**4      # First Ordered
    True
    >>> id2n("....Uw000nn...pg000A2f..Kbo003Go",p) == p**6-1    # Last Ordered
    True
    >>> # Version UT64.4
    >>> p = 18446744073709551557
    >>> id2n("0000000000000000000000000000000000000000000000000000000000000000",p)              # Identity
    0
    >>> id2n("0_000000000000001_______________________________________________",p)              # First unordered
    1
    >>> id2n("0_fffffffffffffff_______________________________________________",p) == 16**15 - 1
    True
    >>> id2n("f_fffffffffffffc4_______________________________________________",p) == p - 1     # Last unordered
    True
    >>> id2n("00_0000000000000000000000000000000000000000000000000000000000001",p)              # First hybrid
    18446744073709551557
    >>> id2n(".._fffffffffff140000000000005195fffffffffff376f30000000000b8e5ac",p) == p**4-1    # Last hybrid
    True
    >>> id2n("0000000000000000000000000000000000000000000000000000000000000001",p) == p**4      # First Ordered
    True
    >>> id2n(".........FU00000003bZv......MleM000000Hl80z.....05Z2Ow0000DhrLwo",p) == p**6-1    # Last Ordered
    True
    >>> try:
    ...     id2n("23rt_4t24t234t23t23t32t23t23rt_4t24t234t23t23t32t23t23rt_4t24t23", p)
    ... except Exception as e:
    ...     print(e)
    Invalid position for '_' in id 23rt_4t24t234t23t23t32t23t23rt_4t24t234t23t23t32t23t23rt_4t24t23
    >>> try:
    ...     id2n(".................23t32t23t234t234t23t23t32t23t224t23t234t23t2123", p)
    ... except Exception as e:
    ...     print(e)
    Ordered id (.................23t32t23t234t234t23t23t32t23t224t23t234t23t2123) with n 39402006196394479212279040100136092515698659329147013992262201319596801387366846232950291543016464135950927013148147 outside allowed range for its kind: [115792089237316193942174975457431254695161196299352022581048345476735855814001;39402006196394478456139629384141450683325994812909116356652328479007639701989040511471346632255226219324457074810248].
    
    Parameters
    ----------
    id
    p
    
    Returns
    -------

    
`n2id(num, digits, p)`
:   Usage:
    
    >>> p = 4294967291
    >>> n2id(0,32,p)    # Identity
    '00000000000000000000000000000000'
    >>> n2id(1,32,p)        # First unordered
    '0_0000001_______________________'
    >>> n2id(16**7-1,32,p)
    '0_fffffff_______________________'
    >>> n2id(p-1,32,p)      # Last unordered
    'f_ffffffa_______________________'
    >>> n2id(p,32,p)        # First hybrid
    '00_00000000000000000000000000001'
    >>> n2id(p**4-1,32,p)   # Last hybrid
    '.._fffec00000095fffffe0b00000276'
    >>> n2id(p**4,32,p)     # First Ordered
    '00000000000000000000000000000001'
    >>> n2id(p**6-1,32,p)   # Last Ordered
    '....Uw000nn...pg000A2f..Kbo003Go'
    >>> # Version UT64.4
    >>> p = 18446744073709551557
    >>> n2id(0,64,p)    # Identity
    '0000000000000000000000000000000000000000000000000000000000000000'
    >>> n2id(1,64,p)        # First unordered
    '0_000000000000001_______________________________________________'
    >>> n2id(16**15-1,64,p)
    '0_fffffffffffffff_______________________________________________'
    >>> n2id(16**15,64,p)
    '1_000000000000000_______________________________________________'
    >>> n2id(p-1,64,p)      # Last unordered
    'f_fffffffffffffc4_______________________________________________'
    >>> n2id(p,64,p)        # First hybrid
    '00_0000000000000000000000000000000000000000000000000000000000001'
    >>> n2id(p**4-1,64,p)   # Last hybrid
    '.._fffffffffff140000000000005195fffffffffff376f30000000000b8e5ac'
    >>> n2id(p**4,64,p)     # First Ordered
    '0000000000000000000000000000000000000000000000000000000000000001'
    >>> n2id(p**6-1,64,p)   # Last Ordered
    '.........FU00000003bZv......MleM000000Hl80z.....05Z2Ow0000DhrLwo'
    >>> p = 4294967291
    >>> try:
    ...     n2id(p**6, 32, p)
    ... except Exception as e:
    ...     print(e)
    Number 6277101691541631771514589274378639120656724268335671295241 outside allowed range: [0;6277101691541631771514589274378639120656724268335671295240]
    >>> try:
    ...     n2id(-1, 32, p)
    ... except Exception as e:
    ...     print(e)
    Number -1 outside allowed range: [0;6277101691541631771514589274378639120656724268335671295240]
    
    Parameters
    ----------
    num
    digits
    p
    
    Returns
    -------