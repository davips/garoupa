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
#  part of this work is a crime and is unethical regarding the effort and
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
    'fw-IowLZVKdeXCNkqsTHFiIe06Pv0.oaAXY.fN6xJ2E7.fe36iBXxOYpmm83Q7ZL'
    >>> b.id
    'ttXOjA4WLwyrOF6tk2YJeYHhrydN6hrm315uFyZRa9Z0OBPm2NWRkoOYtNHYGlwv'
    >>> (a * b).id
    'I-WuI4QUFeHGKfTNKvQq1X5jqz-rfMJC19-pIAVniOF3ScY-1ac3fMqhAElcjexK'
    >>> (b * a).id
    'I-WuI4QUFeHGKfTNKvQq1-T.MqLLanrR4nsDP4B2SuNUeN7xgiWFtVokR7Qcb05-'
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
    0000000000000000000000T6pyeleVnuHDGVuV5pKpby2rejp3txYcmGbCu7u2dh
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
    def fromid(cls, id, version="UT32.4"):
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
        if len(id) != 32 and "32" in version or len(id) != 64 and "64" in version:
            raise Exception(f"Wrong identifier length for {version}: {len(id)}   id:[{id}]")
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
        '0000000000000000000000000000000000000000000000000001DFc0Ttk5MszS'
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
        'sӓĔՇƍǗЋӭȚrсЪƆЬŬĻüɸÓÉ'

        >>> from garoupa import Ø
        >>> (Ø * b'65e987978g').sid
        'rɠȲÃǟƑǒȨɑǛõɚėǜտбǯӳČɟӟоňŰΞԐƆûȋʝƮǎƭλψƥɞȳɦՑ'

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
        \x1b[38;5;131m\x1b[1m\x1b[48;5;0ms\x1b[0m\x1b[38;5;240m\x1b[1m\x1b[48;5;0mӓ\x1b[0m\x1b[38;5;61m\x1b[1m\x1b[48;5;0mĔ\x1b[0m\x1b[38;5;65m\x1b[1m\x1b[48;5;0mՇ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mƍ\x1b[0m\x1b[38;5;238m\x1b[1m\x1b[48;5;0mǗ\x1b[0m\x1b[38;5;238m\x1b[1m\x1b[48;5;0mЋ\x1b[0m\x1b[38;5;239m\x1b[1m\x1b[48;5;0mӭ\x1b[0m\x1b[38;5;239m\x1b[1m\x1b[48;5;0mȚ\x1b[0m\x1b[38;5;60m\x1b[1m\x1b[48;5;0mr\x1b[0m\x1b[38;5;95m\x1b[1m\x1b[48;5;0mс\x1b[0m\x1b[38;5;96m\x1b[1m\x1b[48;5;0mЪ\x1b[0m\x1b[38;5;61m\x1b[1m\x1b[48;5;0mƆ\x1b[0m\x1b[38;5;137m\x1b[1m\x1b[48;5;0mЬ\x1b[0m\x1b[38;5;133m\x1b[1m\x1b[48;5;0mŬ\x1b[0m\x1b[38;5;65m\x1b[1m\x1b[48;5;0mĻ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mü\x1b[0m\x1b[38;5;240m\x1b[1m\x1b[48;5;0mɸ\x1b[0m\x1b[38;5;61m\x1b[1m\x1b[48;5;0mÓ\x1b[0m\x1b[38;5;65m\x1b[1m\x1b[48;5;0mÉ\x1b[0m

        >>> from garoupa import Ø
        >>> print((Ø * b'65e987978g').sidc)
        \x1b[38;5;167m\x1b[1m\x1b[48;5;0mr\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mɠ\x1b[0m\x1b[38;5;95m\x1b[1m\x1b[48;5;0mȲ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mÃ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mǟ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mƑ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mǒ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mȨ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mɑ\x1b[0m\x1b[38;5;168m\x1b[1m\x1b[48;5;0mǛ\x1b[0m\x1b[38;5;173m\x1b[1m\x1b[48;5;0mõ\x1b[0m\x1b[38;5;203m\x1b[1m\x1b[48;5;0mɚ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mė\x1b[0m\x1b[38;5;168m\x1b[1m\x1b[48;5;0mǜ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mտ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mб\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mǯ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mӳ\x1b[0m\x1b[38;5;95m\x1b[1m\x1b[48;5;0mČ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mɟ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mӟ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mо\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mň\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mŰ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mΞ\x1b[0m\x1b[38;5;168m\x1b[1m\x1b[48;5;0mԐ\x1b[0m\x1b[38;5;173m\x1b[1m\x1b[48;5;0mƆ\x1b[0m\x1b[38;5;203m\x1b[1m\x1b[48;5;0mû\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mȋ\x1b[0m\x1b[38;5;168m\x1b[1m\x1b[48;5;0mʝ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mƮ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mǎ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mƭ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mλ\x1b[0m\x1b[38;5;95m\x1b[1m\x1b[48;5;0mψ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mƥ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mɞ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mȳ\x1b[0m\x1b[38;5;131m\x1b[1m\x1b[48;5;0mɦ\x1b[0m\x1b[38;5;167m\x1b[1m\x1b[48;5;0mՑ\x1b[0m

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
        return Hosh.fromn((self.n + self.convert(other).n) % self.order, self.version)

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
        7xoxnm1KL3mqmGpKe1PYxrQEzupxLnsx8rb1JHagl2mBdq.k1xZ.N0XcaPsu-o6J
        """
        return print(self.idc if colored else self.id)

    def short(self, colored=True):
        """
        Usage:

        >>> Hosh(b"asdf86fasd").short(colored=False)
        ÙՉԸͻЬǧӡȕɷʜrżșƕπùcսȑϳՑͶӚǦýՎѐЄƱϫŉñŸɃmЬΦȎʀʓ
        """
        return print(self.sidc if colored else self.sid)

    def __hash__(self):
        return self.n

    def convert(self, other):
        if isinstance(other, Hosh):
            if self.version != other.version:
                raise Exception(f"Incompatible operands: {self.version} != {other.version}")
            return other
        if isinstance(other, str):
            return Hosh.fromid(other, version=self.version)
        if isinstance(other, bytes):
            return Hosh(other, etype=self.etype, version=self.version)
        if isinstance(other, int):
            return Hosh.fromn(other, version=self.version)
        if isinstance(other, list):
            return Hosh.fromcells(other, version=self.version)
        raise Exception(f"Cannot convert type {type(other)}.")

    @classmethod
    def group_props(cls, version):
        if version == "UT32.4":
            return 4294967291, 6277101691541631771514589274378639120656724268335671295241, 32, 24
        elif version == "UT64.4":
            return 18446744073709551557, 39402006196394478456139629384141450683325994812909116356652328479007639701989040511471346632255226219324457074810249, 64, 48
        raise Exception("Unknown version:", version)
