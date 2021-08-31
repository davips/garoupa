Module garoupa.misc.encoding.base777
====================================
Base to enable shorter ids, but at the expense of heavily adopting utf-8 (up to 2-byte) chars

777 chars provide 19.99631153679756 and 39.99262307569413 digits for 32 and 64 versions.
The choice is not arbitrary. 777 is ideal to balance variability even in the most significant digit
for both versions UT32.4 and UT64.4 of Hosh.

Functions
---------

    
`b777dec(string)`
:   Usage:
    
    >>> b777dec("ևև") == 777**2 - 1
    True
    
    Parameters
    ----------
    string
    
    Returns
    -------

    
`b777enc(num, digits)`
:   Usage:
    
    >>> b777enc(123456, 10)
    '00000000ģӪ'
    >>> n = b777dec(b777enc(123456, 10))
    >>> n == 123456
    True