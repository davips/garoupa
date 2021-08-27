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
from typing import Union

from garoupa.base777 import b777enc
from garoupa.colors import colorize128bit
from garoupa.core import cells_id_fromblob, id_fromcells, cells_fromid
from garoupa.math import int2m4, m42int, m4m, m4inv


class Hosh:
    """
    etype = ordered, hybrid, unordered
    According to subgroup: Z, H\\Z or G\\H

    Usage:

    >>> a = Hosh(b"lots of data")
    >>> b = Hosh(b"lots of data 2")
    >>> a.id
    '2Lo3TSO03yIBqYTFR6NKjKdC.oLyb0--'
    >>> b.id
    'lxqpsidKkkGXHiZg7h7aCUy-eI5esBXR'
    >>> (a * b).id
    'ogOtjU.KnUWCpQr8ouvvXJBxqkTZyFWc'
    >>> (b * a).id
    'ogOtjU.KnUU7mBeXIWEu2wWv2aOkuOru'
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
    dOFFu0eLHn0nHvqVpdWgtHXmGGqPLQWl
    >>> print(Ø)  # Version UT64.4
    0000000000000000000000000000000000000000000000000000000000000000
    >>> print(Ø.h * b"sdff")  # etype=hybrid
    000000000000000000000a7sH7lvQjSaSIwE9rArhD52hphAaDuAEI-vjqKMpsnD
    """
    shorter = False
    _repr = None
    _n, _id, _idc, _sid, _sidc, _cells = None, None, None, None, None, None
    _bits = None

    def __init__(self, blob, etype="ordered", version="UT32.4"):
        self.etype, self.version = etype, version
        self.p, self.order, self.digits, self.bytes = self.group_props(version)
        if blob is not None:  # None is for internal use only.
            self._cells, self._id = cells_id_fromblob(blob, etype, self.bytes, self.p)

    @classmethod
    def fromcells(cls, cells, version="UT32.4"):
        hosh = Hosh(None, version=version)
        hosh._cells = cells
        if sum(cells[:4]) == 0:
            hosh.etype = "unordered"
        elif sum(cells[:2]) == 0:
            hosh.etype = "hybrid"
        return hosh

    @classmethod
    def fromid(cls, id):
        """
        Usage:

        >>> Hosh.fromid("I-WuI4QUFeHGKfTNKvQq1.nvrF1g78jBUgN73RMYyoXehzfULkYQHPYdppZW5ar2").n
        27694086209736845103299750681684630473246580734449841275786785442935721031358612476242143296609286791135053038790338
        >>> Hosh.fromid("I-WuI4QUFeHGKfTNKvQq1.nvrF1g78jBUgN73RMYyoXehzfULkYQHPYdppZW5ar2").cells
        [12965474857293227450, 4805863185154552840, 16510049226032775365, 6860254296570243509, 18322175770473372666, 17035651294132294200]

        Parameters
        ----------
        id
        version
        """
        if len(id) == 32:
            version = "UT32.4"
        elif len(id) == 64:
            version = "UT64.4"
        else:
            raise Exception(f"Wrong identifier length: {len(id)}   id:[{id}]")
        hosh = Hosh(None, version=version)
        hosh._id = id
        return hosh

    @classmethod
    def fromn(cls, n: int, version="UT32.4"):
        """Hosh representing the given int.

        Default 'p' is according to version UT64.4.

        Usage:

        >>> h = Hosh.fromn(7647544756746324134134)
        >>> h.id
        '00000000000000000001DFc0Ttk5MszS'
        """
        p, order, _, _ = cls.group_props(version)
        if n > order:
            raise Exception(f"Element outside allowed range: {n} >= {order}")
        return Hosh.fromcells(int2m4(n, p), version)

    def calculate(self):
        if self._cells is not None:
            self._id = id_fromcells(self._cells, self.digits, self.p)
        elif self._id is not None:
            self._cells = cells_fromid(self._id, self.p)
        else:
            raise Exception("Missing argument.")
        if self.n >= self.order:
            raise Exception(f"Element outside allowed range: {self.n} >= {self.order}")

    @property
    def cells(self):
        if self._cells is None:
            self.calculate()
        return self._cells

    @property
    def n(self):
        if self._n is None:
            self._n = m42int(self.cells, self.p)
        return self._n

    @property
    def id(self):
        if self._id is None:
            self.calculate()
        return self._id

    @property
    def sid(self):
        """
        Shorter id (base-922 using up to 2 bytes utf8 per char)

        Usage:

        >>> from garoupa import ø
        >>> (ø * b'65e987978g').sid
        'ĐãǚħHȩИЅՌɠźȪϔUνřǒšWն'

        >>> from garoupa import Ø
        >>> (Ø * b'65e987978g').sid
        'ÊŰԝǮʎĹաΦƟzƶӣξȘբZŖΫįկȯӱđՇՌɘö0ÁѳИσՔMïϾTрвЄ'

        Returns
        -------

        """
        if self._sid is None:
            if self._n is None:
                self.calculate()
            self._sid = b777enc(self._n, self.digits * 5 // 8)
        return self._sid

    @property
    def idc(self):
        if self._idc is None:
            self._idc = colorize128bit(self.id, self.digits)
        return self._idc

    @property
    def sidc(self):
        """
        Shorter colored id (base-922 using up to 2 bytes utf8 per char)

        Usage:

        >>> from garoupa import ø
        >>> print((ø * b'65e987978g').sidc)
        \x1b[38;5;73m\x1b[1m\x1b[48;5;0mĐ\x1b[0m\x1b[38;5;78m\x1b[1m\x1b[48;5;0mã\x1b[0m\x1b[38;5;109m\x1b[1m\x1b[48;5;0mǚ\x1b[0m\x1b[38;5;84m\x1b[1m\x1b[48;5;0mħ\x1b[0m\x1b[38;5;109m\x1b[1m\x1b[48;5;0mH\x1b[0m\x1b[38;5;78m\x1b[1m\x1b[48;5;0mȩ\x1b[0m\x1b[38;5;114m\x1b[1m\x1b[48;5;0mИ\x1b[0m\x1b[38;5;78m\x1b[1m\x1b[48;5;0mЅ\x1b[0m\x1b[38;5;72m\x1b[1m\x1b[48;5;0mՌ\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0mɠ\x1b[0m\x1b[38;5;65m\x1b[1m\x1b[48;5;0mź\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0mȪ\x1b[0m\x1b[38;5;72m\x1b[1m\x1b[48;5;0mϔ\x1b[0m\x1b[38;5;72m\x1b[1m\x1b[48;5;0mU\x1b[0m\x1b[38;5;72m\x1b[1m\x1b[48;5;0mν\x1b[0m\x1b[38;5;77m\x1b[1m\x1b[48;5;0mř\x1b[0m\x1b[38;5;73m\x1b[1m\x1b[48;5;0mǒ\x1b[0m\x1b[38;5;78m\x1b[1m\x1b[48;5;0mš\x1b[0m\x1b[38;5;109m\x1b[1m\x1b[48;5;0mW\x1b[0m\x1b[38;5;84m\x1b[1m\x1b[48;5;0mն\x1b[0m

        >>> from garoupa import Ø
        >>> print((Ø * b'65e987978g').sidc)
        \x1b[38;5;137m\x1b[1m\x1b[48;5;0mÊ\x1b[0m\x1b[38;5;101m\x1b[1m\x1b[48;5;0mŰ\x1b[0m\x1b[38;5;95m\x1b[1m\x1b[48;5;0mԝ\x1b[0m\x1b[38;5;242m\x1b[1m\x1b[48;5;0mǮ\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0mʎ\x1b[0m\x1b[38;5;132m\x1b[1m\x1b[48;5;0mĹ\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0mա\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mΦ\x1b[0m\x1b[38;5;240m\x1b[1m\x1b[48;5;0mƟ\x1b[0m\x1b[38;5;240m\x1b[1m\x1b[48;5;0mz\x1b[0m\x1b[38;5;241m\x1b[1m\x1b[48;5;0mƶ\x1b[0m\x1b[38;5;72m\x1b[1m\x1b[48;5;0mӣ\x1b[0m\x1b[38;5;143m\x1b[1m\x1b[48;5;0mξ\x1b[0m\x1b[38;5;143m\x1b[1m\x1b[48;5;0mȘ\x1b[0m\x1b[38;5;143m\x1b[1m\x1b[48;5;0mբ\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mZ\x1b[0m\x1b[38;5;137m\x1b[1m\x1b[48;5;0mŖ\x1b[0m\x1b[38;5;101m\x1b[1m\x1b[48;5;0mΫ\x1b[0m\x1b[38;5;95m\x1b[1m\x1b[48;5;0mį\x1b[0m\x1b[38;5;242m\x1b[1m\x1b[48;5;0mկ\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0mȯ\x1b[0m\x1b[38;5;132m\x1b[1m\x1b[48;5;0mӱ\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0mđ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mՇ\x1b[0m\x1b[38;5;240m\x1b[1m\x1b[48;5;0mՌ\x1b[0m\x1b[38;5;240m\x1b[1m\x1b[48;5;0mɘ\x1b[0m\x1b[38;5;241m\x1b[1m\x1b[48;5;0mö\x1b[0m\x1b[38;5;72m\x1b[1m\x1b[48;5;0m0\x1b[0m\x1b[38;5;143m\x1b[1m\x1b[48;5;0mÁ\x1b[0m\x1b[38;5;143m\x1b[1m\x1b[48;5;0mѳ\x1b[0m\x1b[38;5;143m\x1b[1m\x1b[48;5;0mИ\x1b[0m\x1b[38;5;107m\x1b[1m\x1b[48;5;0mσ\x1b[0m\x1b[38;5;137m\x1b[1m\x1b[48;5;0mՔ\x1b[0m\x1b[38;5;101m\x1b[1m\x1b[48;5;0mM\x1b[0m\x1b[38;5;95m\x1b[1m\x1b[48;5;0mï\x1b[0m\x1b[38;5;242m\x1b[1m\x1b[48;5;0mϾ\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0mT\x1b[0m\x1b[38;5;132m\x1b[1m\x1b[48;5;0mр\x1b[0m\x1b[38;5;71m\x1b[1m\x1b[48;5;0mв\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mЄ\x1b[0m

        Returns
        -------

        """
        if self._sidc is None:
            self._sidc = colorize128bit(self.sid, self.digits * 5 // 8)
        return self._sidc

    def __repr__(self):
        if self._repr is None:
            self._repr = self.sidc if Hosh.shorter else self.idc
        return self._repr

    # @property
    # def bits(self):
    #     if self._bits is None:
    #         self._bits = bin(self.n)[2:].rjust(256, "0")
    #     return self._bits

    def __mul__(self, other: Union['Hosh', str, bytes, int]):
        return Hosh.fromcells(m4m(self.cells, self.convert(other).cells, self.p), self.version)

    def __invert__(self):
        return Hosh.fromcells(m4inv(self.cells, self.p), self.version)

    def __truediv__(self, other):
        return Hosh.fromcells(m4m(self.cells, m4inv(self.convert(other).cells, self.p), self.p), self.version)

    def __add__(self, other):
        """Matrix addition modulo p, keeping unidiagonal"""
        return Hosh.fromcells(
            list(map(lambda x, y: (x + y) % self.p, self.cells, self.convert(other).cells)), self.version
        )
        # REMINDER: these 2 codes produce different results!
        # return Hosh.fromn((self.n + self.convert(other).n) % self.order, self.version)

    def __sub__(self, other):
        return Hosh.fromn((self.n - self.convert(other).n) % self.order, self.version)

    def __str__(self):
        return self.sid if Hosh.shorter else self.id

    def __eq__(self, other):
        return self.n == self.convert(other).n

    def __ne__(self, other):
        return self.n != self.convert(other).n

    def show(self, colored=True):
        """
        Usage:

        >>> Hosh(b"asdf86fasd").show(colored=False)
        8nsZouodGbQ5.9OUrypqCzmYrK1t8hou
        """
        return print(self.idc if colored else self.id)

    def short(self, colored=True):
        """
        Usage:

        >>> Hosh(b"asdf86fasd").short(colored=False)
        çÙkƝĜưŉЗßîōɨϱӲXеșηȧð
        """
        return print(self.sidc if colored else self.sid)

    def __hash__(self):
        return self.n

    def convert(self, other):
        if isinstance(other, str):
            other = Hosh.fromid(other)
        elif isinstance(other, bytes):
            other = Hosh(other, etype=self.etype, version=self.version)
        elif isinstance(other, int):
            other = Hosh.fromn(other, version=self.version)
        elif isinstance(other, list):
            other = Hosh.fromcells(other, version=self.version)
        elif not isinstance(other, Hosh):
            raise Exception(f"Cannot convert type {type(other)}.")
        if self.version != other.version:
            raise Exception(f"Incompatible operands: {self.version} != {other.version}")
        return other

    @classmethod
    def group_props(cls, version):
        if version == "UT32.4":
            return 4294967291, 6277101691541631771514589274378639120656724268335671295241, 32, 24
        elif version == "UT64.4":
            return 18446744073709551557, 39402006196394478456139629384141450683325994812909116356652328479007639701989040511471346632255226219324457074810249, 64, 48
        raise Exception("Unknown version:", version)
