# encoders

import hashlib
import struct
from typing import Dict, List

import cruipto.alphabets as alph


def md5_int(bytes_content: bytes):
    """Return MD5 hash as integer.

    Generates a hash intended for unique identification of content
     (unique for any reasonably finite universe).

    It is preferred to generate such hash on compressed data,
    since MD5 is much slower for large data than the compression itself.

    Parameters
    ----------
    bytes_content
        encoded content; it can be a packed object, a text, JSON,...

    Returns
    -------
        a big integer in [0; 2^128[
    """
    return int.from_bytes(hashlib.md5(bytes_content).digest(), "big")  # or little? or whatever?


def enc(number: int, alphabet: str = alph.letters800, padding: int = 14) -> str:
    """Encode an integer to base-n. n = len(alphabet).

    The default is base-800 since it is enough to represent MD5 as 18 chars in
    utf8 (1-2 bytes each char).
    The selected default alphabet contains only word characters.
    This alphabet is intended to be printable and to be free of
    disruptive characters, i.e. any combination of adjacent characters will be
    understood as a single word by most linux terminals and editors.
    This can be seen as the subset of 'double-click-friendly chars'.

    The following list shows how the alphabet size relates to the number of
    necessary digits to represent the biggest MD5 number (2^128).
    The hexdigest already uses 32 digits, so we want less than that.
    According to the list below, good choices for the alphabet size would be in
    the range 85-185 to keep 1 byte for each (latin1 range).

    alphabet-size   number-of-digits   comments
    2 128 # crude md5 as binary string
    16 32 # hexdigest as string
    24 28
    41 24 # reducing from 32 to 24 is kind of a improvement
    48 23
    57 22 # possible to type with an US keyboard
    69 21
    85 20 # base64 library provides base85, but it is not double_click_friendly
    107 19 # super friendly (our default choice)
    139 18 # not terminator/intellij friendly
    185 17 # not double_click_friendly
    256 16 # would include lots of unprintable characters
    371 15 # 371 and beyond is outside a single byte and latin1
    566 14 # idem
    16-bit 4 # idem
    32-bit 2 # UTF-8?

    147 is the size of the largest subset of latin1 that is
    double_click_friendly. Latin1 is compatible with UTF-8 and extends ASCII.

    Example alphabets are given below:

    gnome-terminal friendly (147)  [\\ <- escaped slash]
#%&+,-./0123456789=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ\\_abcdefghijklmnopqrstuvwxyz
~ª²³µ·¹º¼½¾ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþ

    gnome-terminal/terminator/intellij friendly (125)
#0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz
ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþ

    gnome-terminal/terminator/intellij[ctrl+w] friendly (124)
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz
ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþ

    gnome-terminal/terminator/intellij without _ and some twin chars (107)
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
ÁÂÄÅÆÉÊËÍÎÏÐÑÓÔÖÚÛÜÝÞßáâäåæçéêëíîïðñóôöøúûüýþ

    typeable and double-clickable (63)
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz

14:
ÂɕÃѓνʓʅŶTČϒËzЂ

23:
D2eEFG4HIj1NOP764Qstya8

In [7]: math.log(factorial(35), 62)
Out[7]: 22.32449128323706

14: ÂɕÃѓνʓʅŶTČϒËzЂ

     ÂɕÃѓ
    νʓʅŶT
    ČϒËzЂ


23: D2eEFG4HIj1NOP764Qstya8

     D2eEF
    G4HIj1
    NOP764
    Qstya8


    Parameters
    ----------
    number
        Usually a big MD5-like int
    alphabet
        String with allowed digits
    padding
        Length of output

    Returns
    -------
        String representing a base-800 number (or any other base, depending on the given alphabet length)
    """
    l = len(alphabet)
    res = []
    while number > 0:
        number, rem = divmod(number, l)
        res.append(alphabet[rem])
        if number == 0:
            break
    return "".join(res)[::-1].rjust(padding, "0")


def dec(digits: str, lookup: Dict[str, int] = alph.lookup800) -> int:
    """Decode digits from base-len(alphabet).
    
    See enc() for more info.
    
    Parameters
    ----------
    digits

    lookup

    Returns
    -------
        Number in decimal base
    """
    res = 0
    last = len(digits) - 1
    base = len(lookup)
    for i, d in enumerate(digits):
        res += lookup[d] * pow(base, last - i)
    return res


# Useful, but not really used functions. ====================================
def encrypt(msg: bytes, key: bytes) -> bytes:
    """AES 16 bytes encryption."""
    from Crypto.Cipher import AES

    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)


def decrypt(encrypted_msg: bytes, key: bytes) -> bytes:
    """AES 16 bytes decryption."""
    from Crypto.Cipher import AES

    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(encrypted_msg)


def integers2bytes(lst, n=4) -> bytes:
    """Each int becomes N bytes. max=4294967294 for 4 bytes"""
    return b"".join(d.to_bytes(n, byteorder="little") for d in lst)


def bytes2integers(bytes_content: bytes, n=4) -> List[int]:
    """Each 4 bytes become an int."""
    return [int.from_bytes(bytes_content[i: i + n], "little") for i in range(0, len(bytes_content), n)]


# def float2bytes(*lst) -> bytes:
#     """Each float becomes 8 bytes. max=4294967294"""
#     return struct.pack("!" + str(len(lst)) + "d", *lst)
#
#
# def bytes2float(bytes_content: bytes) -> List[float]:
#     """Each 8 bytes become a float."""
#     return struct.unpack("!" + str(len(bytes_content) // 8) + "d", bytes_content)


# Dirty and fast encoders, ....
def pmatrix2pretty(m: List[int], alphabet: str) -> str:  # =alphabet1224
    """Convert a permutation matrix to a string using the given alphabet.

    The alphabet should have at least |m|² - 1 letters.
    When compared to the straight math conversion, this implementation will
    provide a shorter text (20 vs 18) through a faster conversion (44us vs 5us)
    at the expense of size in bytes (increasing from 20 to ~34 in RAM and from
    20 to 36 in a fixed length CHAR field in a database; latin1 vs utf8).
    In a 1MiB/s network, this would lead to extra 18us,
    still far from ~40us savings.
    """
    # TODO: Create an alphabet for 58x58 (3363 letters).
    side = len(m)
    lst = [alphabet[m[i + 1] + side * m[i]] for i in range(0, side - 1, 2)]
    if side % 2 == 1:
        lst.append(alphabet[m[side - 1]])
    return "".join(lst)


def pretty2pmatrix(text: str, side: int, alphabet_dict: Dict[str, int]) -> List[int]:  # =alphabet1224dic
    """See pmatrix2pretty."""
    m = [x for d in text[:-1] for x in divmod(alphabet_dict[d], side)]
    if side % 2 == 1:
        m.append(alphabet_dict[text[-1]])
    return m
