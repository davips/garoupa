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
#  part of this work is illegal and unethical regarding the effort and
#  time spent here.
from sys import maxsize
from typing import Union

from garoupa.misc.core import cells_id_fromblob, cells_fromid, id_fromcells
from garoupa.misc.encoding.base777 import b777enc
from garoupa.misc.exception import (
    WrongOperands,
    WrongContent,
    DanglingEtype,
    CellValueTooHigh,
    WrongIdentifier,
    ElementTooHigh,
    WrongVersion,
)
from garoupa.misc.math import int2cells, cells2int, cellsmul, cellsinv
from garoupa.misc.colors import colorize128bit


class Hosh:
    """
    Operable hash.

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
        According to the subset of the desired element: Z, H\\Z or G\\H
    version
        UT32.4 or UT64.4 changes the number of digits and robustness against collisions
        UT32.4 is enough for most usages. It accepts more than 4 billion repetitions of the same operation in a row.
        UT64.4 provides unspeakable limits for operations, please see scientific paper for details.
    """

    shorter = False
    _repr = None
    _n, _id, _idc, _sid, _sidc, _etype = None, None, None, None, None, None
    _etype_inducer, _bits = None, None

    def __init__(self, content, etype="default:ordered", version="UT32.4"):
        self.version = version
        self.p, self.order, self.digits, self.bytes = self.group_props(version)
        if isinstance(content, list):
            if etype != "default:ordered":
                raise DanglingEtype(f"Cannot set etype={etype} when providing cells ({content}).")
            if max(content) >= self.p:
                raise CellValueTooHigh(f"A cell value exceeds the limit for the group: {max(content)} >= {self.p}")
            self.cells = content
        elif isinstance(content, bytes):
            if etype == "default:ordered":
                etype = "ordered"
            self.cells, self._id = cells_id_fromblob(content, etype, self.bytes, self.p)
        else:
            raise WrongContent(
                f"No valid content provided: {content}\n" f"It should be a bytes object to be hashed or a list of ints."
            )

    @property
    def etype(self):
        """
        Type of this element

        Usage:

        >>> from garoupa import Hosh
        >>> Hosh.fromn(5).etype
        'unordered'

        Returns
        -------
        'ordered', 'hybrid' or 'unordered'
        """
        if self._etype is None:
            if sum(self.cells[:5]) == 0:
                self._etype = "unordered"
            elif sum(self.cells[:2]) == 0:
                self._etype = "hybrid"
            else:
                self._etype = "ordered"
        return self._etype

    @property
    def etype_inducer(self):
        """
        Type this element uses to coerce an element of undefined type.

        Usage:

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
        'ordered', 'hybrid', 'unordered'
        """
        if self._etype_inducer is None:
            self._etype_inducer = self.etype
        return self._etype_inducer

    @property
    def id(self):
        """
        Textual representation of this element

        Returns
        -------
        Textual representation
        """
        if self._id is None:
            self._id = id_fromcells(self.cells, self.digits, self.p)
        return self._id

    @classmethod
    def fromid(cls, id):
        """
        Create an element from a textual id.

        Usage:

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

        Parameters
        ----------
        id

        Returns
        -------
        A new Hosh object
        """
        if len(id) == 32:
            version = "UT32.4"
        elif len(id) == 64:
            version = "UT64.4"
        else:
            raise WrongIdentifier(f"Wrong identifier length: {len(id)}   id:[{id}]")
        return Hosh(cells_fromid(id, p=cls.group_props(version)[0]), version=version)

    @classmethod
    def fromn(cls, n: int, version="UT32.4"):
        """
        Create a Hosh object representing the given int.

        Default 'p' is according to version UT64.4.

        Usage:

        >>> h = Hosh.fromn(7647544756746324134134)
        >>> h.id
        '00_000000000019e9300ddd405c1c8fc'

        Parameters
        ----------
        n
        version

        Returns
        -------
        A new Hosh object
        """
        p, order, _, _ = cls.group_props(version)
        if n > order:
            raise ElementTooHigh(f"Element outside allowed range: {n} >= {order}")
        return Hosh(int2cells(n, p), version=version)

    @property
    def n(self):
        """
        Lexicographic rank of this eloement (according to the format adopted in internal integer cells.

        Returns
        -------
        Number
        """
        if self._n is None:
            self._n = cells2int(self.cells, self.p)
        return self._n

    @property
    def sid(self):
        """
        Shorter id (base-922 using up to 2 bytes utf8 per char)

        Usage:

        >>> from garoupa import ø
        >>> (ø * b'65e987978g').sid
        'ĐãǚħHȩСЭĵʙĞŸιśԵəжʐƙö'

        >>> from garoupa import Ø
        >>> (Ø * b'65e987978g').sid
        'ÊŰԝǮʎĹաΦƟzƶӣξʙСʠΠмΌВʜȉΖáςՔĦĢνԱCϔΘҳȖưΎìɚF'

        Returns
        -------
        Short utf-8 textual representation
        """
        if self._sid is None:
            self._sid = b777enc(self.n, self.digits * 5 // 8)
        return self._sid

    @property
    def idc(self):
        """
        Colored textual representation of this element

        Returns
        -------
        Textual representation
        """
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
        \x1b[38;5;75m\x1b[1m\x1b[48;5;0mĐ\x1b[0m\x1b[38;5;117m\x1b[1m\x1b[48;5;0mã\x1b[0m\x1b[38;5;159m\x1b[1m\x1b[48;5;0mǚ\x1b[0m\x1b[38;5;153m\x1b[1m\x1b[48;5;0mħ\x1b[0m\x1b[38;5;117m\x1b[1m\x1b[48;5;0mH\x1b[0m\x1b[38;5;159m\x1b[1m\x1b[48;5;0mȩ\x1b[0m\x1b[38;5;194m\x1b[1m\x1b[48;5;0mС\x1b[0m\x1b[38;5;146m\x1b[1m\x1b[48;5;0mЭ\x1b[0m\x1b[38;5;74m\x1b[1m\x1b[48;5;0mĵ\x1b[0m\x1b[38;5;81m\x1b[1m\x1b[48;5;0mʙ\x1b[0m\x1b[38;5;117m\x1b[1m\x1b[48;5;0mĞ\x1b[0m\x1b[38;5;158m\x1b[1m\x1b[48;5;0mŸ\x1b[0m\x1b[38;5;146m\x1b[1m\x1b[48;5;0mι\x1b[0m\x1b[38;5;73m\x1b[1m\x1b[48;5;0mś\x1b[0m\x1b[38;5;109m\x1b[1m\x1b[48;5;0mԵ\x1b[0m\x1b[38;5;74m\x1b[1m\x1b[48;5;0mə\x1b[0m\x1b[38;5;75m\x1b[1m\x1b[48;5;0mж\x1b[0m\x1b[38;5;117m\x1b[1m\x1b[48;5;0mʐ\x1b[0m\x1b[38;5;159m\x1b[1m\x1b[48;5;0mƙ\x1b[0m\x1b[38;5;153m\x1b[1m\x1b[48;5;0mö\x1b[0m

        >>> from garoupa import Ø
        >>> print((Ø * b'65e987978g').sidc)
        \x1b[38;5;249m\x1b[1m\x1b[48;5;0mÊ\x1b[0m\x1b[38;5;249m\x1b[1m\x1b[48;5;0mŰ\x1b[0m\x1b[38;5;144m\x1b[1m\x1b[48;5;0mԝ\x1b[0m\x1b[38;5;144m\x1b[1m\x1b[48;5;0mǮ\x1b[0m\x1b[38;5;246m\x1b[1m\x1b[48;5;0mʎ\x1b[0m\x1b[38;5;109m\x1b[1m\x1b[48;5;0mĹ\x1b[0m\x1b[38;5;146m\x1b[1m\x1b[48;5;0mա\x1b[0m\x1b[38;5;150m\x1b[1m\x1b[48;5;0mΦ\x1b[0m\x1b[38;5;182m\x1b[1m\x1b[48;5;0mƟ\x1b[0m\x1b[38;5;150m\x1b[1m\x1b[48;5;0mz\x1b[0m\x1b[38;5;179m\x1b[1m\x1b[48;5;0mƶ\x1b[0m\x1b[38;5;137m\x1b[1m\x1b[48;5;0mӣ\x1b[0m\x1b[38;5;104m\x1b[1m\x1b[48;5;0mξ\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0mʙ\x1b[0m\x1b[38;5;175m\x1b[1m\x1b[48;5;0mС\x1b[0m\x1b[38;5;109m\x1b[1m\x1b[48;5;0mʠ\x1b[0m\x1b[38;5;249m\x1b[1m\x1b[48;5;0mΠ\x1b[0m\x1b[38;5;249m\x1b[1m\x1b[48;5;0mм\x1b[0m\x1b[38;5;144m\x1b[1m\x1b[48;5;0mΌ\x1b[0m\x1b[38;5;144m\x1b[1m\x1b[48;5;0mВ\x1b[0m\x1b[38;5;246m\x1b[1m\x1b[48;5;0mʜ\x1b[0m\x1b[38;5;109m\x1b[1m\x1b[48;5;0mȉ\x1b[0m\x1b[38;5;146m\x1b[1m\x1b[48;5;0mΖ\x1b[0m\x1b[38;5;150m\x1b[1m\x1b[48;5;0má\x1b[0m\x1b[38;5;182m\x1b[1m\x1b[48;5;0mς\x1b[0m\x1b[38;5;150m\x1b[1m\x1b[48;5;0mՔ\x1b[0m\x1b[38;5;179m\x1b[1m\x1b[48;5;0mĦ\x1b[0m\x1b[38;5;137m\x1b[1m\x1b[48;5;0mĢ\x1b[0m\x1b[38;5;104m\x1b[1m\x1b[48;5;0mν\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0mԱ\x1b[0m\x1b[38;5;175m\x1b[1m\x1b[48;5;0mC\x1b[0m\x1b[38;5;109m\x1b[1m\x1b[48;5;0mϔ\x1b[0m\x1b[38;5;249m\x1b[1m\x1b[48;5;0mΘ\x1b[0m\x1b[38;5;249m\x1b[1m\x1b[48;5;0mҳ\x1b[0m\x1b[38;5;144m\x1b[1m\x1b[48;5;0mȖ\x1b[0m\x1b[38;5;144m\x1b[1m\x1b[48;5;0mư\x1b[0m\x1b[38;5;246m\x1b[1m\x1b[48;5;0mΎ\x1b[0m\x1b[38;5;109m\x1b[1m\x1b[48;5;0mì\x1b[0m\x1b[38;5;146m\x1b[1m\x1b[48;5;0mɚ\x1b[0m\x1b[38;5;150m\x1b[1m\x1b[48;5;0mF\x1b[0m

        Returns
        -------
        Short utf-8 colored textual representation
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

    def __mul__(self, other: Union["Hosh", str, bytes, int]):
        return Hosh(cellsmul(self.cells, self.convert(other).cells, self.p), version=self.version)

    def __invert__(self):
        return Hosh(cellsinv(self.cells, self.p), version=self.version)

    def __truediv__(self, other):
        return Hosh(cellsmul(self.cells, cellsinv(self.convert(other).cells, self.p), self.p), version=self.version)

    def __add__(self, other):
        """Matrix addition modulo p, keeping unidiagonal"""
        cells = list(map(lambda x, y: (x + y) % self.p, self.cells, self.convert(other).cells))
        return Hosh(cells, version=self.version)
        # REMINDER: these 2 codes produce different results!
        # return Hosh.fromn((self.n + self.convert(other).n) % self.order, self.version)

    # def __sub__(self, other):
    #     return Hosh.fromn((self.n - self.convert(other).n) % self.order, version=self.version)

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
        8nsZouodGbQ5.9OUrypqCzmYrK1t8hov
        """
        return print(self.idc if colored else self.id)

    def short(self, colored=True):
        """
        Usage:

        >>> Hosh(b"asdf86fasd").short(colored=False)
        çÙkƝĜưŔнǒēòƣσåŴQӀՏмŷ
        """
        return print(self.sidc if colored else self.sid)

    def __hash__(self):
        return self.n % maxsize

    def convert(self, other):
        """
        Usage:

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

        """
        if isinstance(other, str):
            other = Hosh.fromid(other)
        elif isinstance(other, bytes):
            other = Hosh(other, etype=self.etype_inducer, version=self.version)
        elif isinstance(other, int):
            other = Hosh.fromn(other, version=self.version)
        elif isinstance(other, list):
            other = Hosh(other, version=self.version)
        elif not isinstance(other, Hosh):
            raise WrongOperands(
                id(self.__class__), id(other.__class__), f"Cannot convert {type(other)} to {type(self)}."
            )
        if self.version != other.version:
            raise WrongVersion(f"Incompatible operands: {self.version} != {other.version}")
        return other

    @classmethod
    def group_props(cls, version):
        """
        Usage:

        >>> from garoupa import Hosh
        >>> Hosh.group_props("UT32.4")
        (4294967291, 6277101691541631771514589274378639120656724268335671295241, 32, 24)

        Parameters
        ----------
        version

        Returns
        -------

        """
        if version == "UT32.4":
            return 4294967291, 6277101691541631771514589274378639120656724268335671295241, 32, 24
        elif version == "UT64.4":
            return (
                18446744073709551557,
                39402006196394478456139629384141450683325994812909116356652328479007639701989040511471346632255226219324457074810249,
                64,
                48,
            )
        raise WrongVersion("Unknown version:", version)
