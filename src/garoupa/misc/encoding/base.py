#  Copyright (c) 2021. Davi Pereira dos Santos
#  This file is part of the garoupa project.
#  Please respect the license - more about this in the section (*) below.
#
#  garoupa is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  garoupa is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with garoupa.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is illegal and is unethical regarding the effort and
#  time spent here.
"""Different bases to compose an identifier string"""

b64 = tuple("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-.")
b64r = dict((c, v) for v, c in enumerate(b64))

b16 = b64[:16]
b16r = dict((c, v) for v, c in enumerate(b16))

b20 = b64[16:36]
b20r = dict((c, v) for v, c in enumerate(b20))

b2 = b64[:2]
b2r = dict((c, v) for v, c in enumerate(b2))

b8 = b64[:8]
b8r = dict((c, v) for v, c in enumerate(b8))


def dec(string, ralphabet):
    """Convert a little-endian textual digest to a number

    Usage:

    >>> dec("ba", ralphabet=b64r) == 10 * 64 + 11
    True

    Parameters
    ----------
    ralphabet
    string

    Returns
    -------

    """
    num = 0
    b = len(ralphabet)
    i = len(string)
    while i > 0:
        i -= 1
        num = num * b + ralphabet[string[i]]
    return num


def enc(num, alphabet, digits):
    """Convert a number to a little-endian textual digest

    Usage:

    >>> enc(123456, b64, 10)
    '09u0000000'
    >>> n = dec(enc(123456, b64, 10), b64r)
    >>> n == 123456
    True
    >>> try:
    ...     enc(-1, b64, 10)
    ... except Exception as e:
    ...     print(e)
    Cannot encode negative number -1
    """
    encoded = ""
    if num < 0:  # pragma: no cover
        raise Exception(f"Cannot encode negative number {num}")
    b = len(alphabet)
    while num:
        num, rem = divmod(num, b)
        encoded += alphabet[rem]
    return encoded.ljust(digits, alphabet[0])


def id2n(id, p):
    """
    Usage:

    >>> p = 4294967291
    >>> id2n("00000000000000000000000000000000",p)              # Identity
    0
    >>> id2n("0_1000000_______________________",p)              # First unordered
    1
    >>> id2n("0_fffffff_______________________",p) == 16**7 - 1
    True
    >>> id2n("f_affffff_______________________",p) == p - 1     # Last unordered
    True
    >>> id2n("00_10000000000000000000000000000",p)              # First hybrid
    4294967291
    >>> id2n(".._67200000b0efffff59000000cefff",p) == p**4-1    # Last hybrid
    True
    >>> id2n("10000000000000000000000000000000",p) == p**4      # First Ordered
    True
    >>> id2n("oG300obK..f2A000gp...nn000wU....",p) == p**6-1    # Last Ordered
    True
    >>> # Version UT64.4
    >>> p = 18446744073709551557
    >>> id2n("0000000000000000000000000000000000000000000000000000000000000000",p)              # Identity
    0
    >>> id2n("0_100000000000000_______________________________________________",p)              # First unordered
    1
    >>> id2n("0_fffffffffffffff_______________________________________________",p) == 16**15 - 1
    True
    >>> id2n("f_4cfffffffffffff_______________________________________________",p) == p - 1     # Last unordered
    True
    >>> id2n("00_1000000000000000000000000000000000000000000000000000000000000",p)              # First hybrid
    18446744073709551557
    >>> id2n(".._ca5e8b00000000003f673fffffffffff591500000000000041fffffffffff",p) == p**4-1    # Last hybrid
    True
    >>> id2n("1000000000000000000000000000000000000000000000000000000000000000",p) == p**4      # First Ordered
    True
    >>> id2n("owLrhD0000wO2Z50.....z08lH000000MelM......vZb30000000UF.........",p) == p**6-1    # Last Ordered
    True
    >>> try:
    ...     id2n("32t42t4_tr32t32t23t32t32t432t42t4_tr32t32t23t32t32t432t42t4_tr32", p)
    ... except Exception as e:
    ...     print(e)
    Invalid position for '_' in id 32t42t4_tr32t32t23t32t32t432t42t4_tr32t32t23t32t32t432t42t4_tr32
    >>> try:
    ...     id2n("3212t32t432t32t422t32t23t32t32t432t432t32t23t32.................", p)
    ... except Exception as e:
    ...     print(e)
    Ordered id (3212t32t432t32t422t32t23t32t32t432t432t32t23t32.................) with n 39402006196394479212279040100136092515698659329147013992262201319596801387366846232950291543016464135950927013148147 outside allowed range for its kind: [115792089237316193942174975457431254695161196299352022581048345476735855814001;39402006196394478456139629384141450683325994812909116356652328479007639701989040511471346632255226219324457074810248].

    Parameters
    ----------
    id
    p

    Returns
    -------

    """
    if id[1] == "_":
        hexsize = len(id) // 4 - 1
        a = dec(id[:1], b16r)
        b = dec(id[2 : (hexsize + 2)], b16r)
        n = a * 16 ** hexsize + b
        kind, lower, upper = "Unordered", 1, p - 1
    elif id[2] == "_":
        a = dec(id[:2], b64r)
        b = dec(id[3:], b16r)
        n = a * 16 ** (len(id) - 3) + b + p - 1
        kind, lower, upper = "Hybrid", p, p ** 4 - 1
    elif "_" not in id:
        n = dec(id, b64r)
        if n == 0:
            return 0
        n += p ** 4 - 1
        kind, lower, upper = "Ordered", p ** 4, p ** 6 - 1
    else:  # pragma: no cover
        raise Exception(f"Invalid position for '_' in id {id}")
    if not lower <= n <= upper:  # pragma: no cover
        raise Exception(f"{kind} id ({id}) with n {n} outside allowed range for its kind: [{lower};{upper}].")
    return n


def n2id(num, digits, p):
    """
    Usage:

    >>> p = 4294967291
    >>> n2id(0,32,p)    # Identity
    '00000000000000000000000000000000'
    >>> n2id(1,32,p)        # First unordered
    '0_1000000_______________________'
    >>> n2id(16**7-1,32,p)
    '0_fffffff_______________________'
    >>> n2id(p-1,32,p)      # Last unordered
    'f_affffff_______________________'
    >>> n2id(p,32,p)        # First hybrid
    '00_10000000000000000000000000000'
    >>> n2id(p**4-1,32,p)   # Last hybrid
    '.._67200000b0efffff59000000cefff'
    >>> n2id(p**4,32,p)     # First Ordered
    '10000000000000000000000000000000'
    >>> n2id(p**6-1,32,p)   # Last Ordered
    'oG300obK..f2A000gp...nn000wU....'
    >>> # Version UT64.4
    >>> p = 18446744073709551557
    >>> n2id(0,64,p)    # Identity
    '0000000000000000000000000000000000000000000000000000000000000000'
    >>> n2id(1,64,p)        # First unordered
    '0_100000000000000_______________________________________________'
    >>> n2id(16**15-1,64,p)
    '0_fffffffffffffff_______________________________________________'
    >>> n2id(16**15,64,p)
    '1_000000000000000_______________________________________________'
    >>> n2id(p-1,64,p)      # Last unordered
    'f_4cfffffffffffff_______________________________________________'
    >>> n2id(p,64,p)        # First hybrid
    '00_1000000000000000000000000000000000000000000000000000000000000'
    >>> n2id(p**4-1,64,p)   # Last hybrid
    '.._ca5e8b00000000003f673fffffffffff591500000000000041fffffffffff'
    >>> n2id(p**4,64,p)     # First Ordered
    '1000000000000000000000000000000000000000000000000000000000000000'
    >>> n2id(p**6-1,64,p)   # Last Ordered
    'owLrhD0000wO2Z50.....z08lH000000MelM......vZb30000000UF.........'
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

    """
    if num < 0 or num >= p ** 6:  # pragma: no cover
        raise Exception(f"Number {num} outside allowed range: [0;{p ** 6 - 1}]")
    elif num >= p ** 4:
        return enc(num - p ** 4 + 1, b64, digits)
    elif num >= p:
        a, b = divmod(num - p + 1, 16 ** (digits - 3))
        return enc(a, b64, 2) + "_" + enc(b, b16, digits - 3)
    elif num > 0:
        hexsize = digits // 4 - 1
        # a, b = divmod(num, 2 ** (digits-2))
        a, b = divmod(num, 16 ** hexsize)
        # return enc(a, b64, 1) + "_" + enc(b, b2, digits - 2)
        return str(b16[a]) + "_" + enc(b, b16, hexsize) + (digits - hexsize - 2) * "_"
    elif num == 0:
        return "0" * digits


# TODO memoize exponents, by passing an object, e.g.: o.p, o.p4, o.p6
