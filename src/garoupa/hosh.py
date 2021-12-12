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

from garoupa.groups import UT40_4, groups
from garoupa.misc.colors import ansi2html, id2ansi, id2rgb
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


class Hosh:
    """
    Operable hash.

    Generate a Hosh object from a binary content or a list of 6 ints.

    Usage:

    >>> from garoupa import Hosh
    >>> a = Hosh(b"lots of data")
    >>> b = Hosh(b"lots of data 2")
    >>> a.id
    '.-0byLo.CdKjKN6RFTYqBIy30OST3oLyjYPf.6p8'
    >>> b.id
    'SXBse5Ie-yUCa7h7gZiHXGkkKdispqxlc4FnCYit'
    >>> (a * b).id
    'ALiaB9XPu.MoIwwoTPYrxqkGfVpktOgUv0tDB3IB'
    >>> (b * a).id
    'gr9psTs5dYGrCCdgWMAPWM4dDDzktOgUv0tDB3IB'
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
    >>> from garoupa import ø
    >>> print(ø)  # Handy syntax using ø for identity.
    0000000000000000000000000000000000000000
    >>> print(ø * "7ysdf98ys34hg543hdf98ysdf98ysdfysdf98ysd")  # str, bytes or int are converted as id, blob or element rank.
    7ysdf98ys34hg543hdf98ysdf98ysdfysdf98ysd
    >>> print(ø * "7ysdf98ysdf98ysdf98ysdfysdf98ysdasddsa32" * "6gdsf76dfqwe123de8gaf87gaf87gaf87agdfa78")
    94UrdYKjCGQWdd5P.W4xvFJgc9hZpIHlhytqHkaa
    >>> h = ø.u * b"sdff"
    >>> print(h)
    f_9e1a267c8_____________________________
    >>> x.id, (+x).id  # Making an ordered x.
    ('ZN_60eec3e6c7b68087329e16b581401a6bb2b1f', '6BDj3b7Mmj7n-6B8XYaP3akO7400s9FlG4AtcHTp')
    >>> -x * y != y * -x
    True
    >>> --x == x
    True
    >>> x ** y == +(+x * +y)  # a ** b is a shortcut for +(+a * +b)
    True
    >>> x ** y != y ** x
    True
    >>> (x ** b"1") * (y ** b"2") != (x ** b"2") * (y ** b"1")
    True
    >>> (x ** b"1") * (y ** b"2") == (y ** b"2") * (x ** b"1")
    True
    >>> (x ** y) // y == x
    True
    >>> f + e - x == ø - x + e + f  # Alternative (always unordered, i.e., form an Abelian group) operation
    True

    Parameters
    ----------
    content
        Binary content to be hashed, or a list of six integers
    etype
        ordered, hybrid, unordered
        According to the subset of the desired element: Z, H\\Z or G\\H
    version
        Group namedtuple: changes the number of digits and robustness against collisions
        UT32_4 is enough for most usages. It accepts more than 4 billion repetitions of the same operation in a row.
        UT64_4 provides unspeakable limits for operations, please see scientific paper for details.
        UT40_4 is recommended and default, since it is the most compatible with other systems (git, SHA-1, etc)
    """

    shorter = False
    _repr = None
    _n, _id, _ansi, _sid, _sidc, _etype, _rgb = None, None, None, None, None, None, None
    _etype_inducer, _bits, _ø = None, None, None

    def __init__(self, content, etype="default:ordered", version=UT40_4):
        self.version = version
        self.p, self.p4, self.p6, self.digits, self.bytes, _, _, _, _, _, _ = version
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
    def ø(self):
        """Identity element compatible with this Hosh object

        Usage:

        >>> from garoupa import Hosh
        >>> (b := Hosh(b"23987rg23")).id
        'J5.uRTue8X4r1xu.JFkPbURVVGvTRPSFLncXdyzj'
        >>> b.etype
        'ordered'
        >>> b.ø.etype
        'unordered'
        >>> b.etype == b.ø.etype_inducer
        True
        >>> b.ø.id
        '0000000000000000000000000000000000000000'
        >>> (b.ø * b"qwer").etype
        'ordered'
        """
        if self._ø is None:
            from garoupa import Identity

            self._ø = Identity(version=self.version, etype_inducer=self.etype)
        return self._ø

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
        >>> Hosh(b"12124", etype="hybrid").etype_inducer
        'hybrid'

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
        1094566309952642687224764830259410933250743749332933330234
        >>> a.cells
        [748932665, 516513868, 468764361, 3316970622, 2727293743, 316029245]
        >>> a.etype
        'ordered'
        >>> bid = a.id[:2] + "_" + a.id[3:]
        >>> bid
        'ab_defabcdefabcdefabcdefabcdefab'
        >>> b = Hosh.fromid(bid)
        >>> b.id
        'ab_defabcdefabcdefabcdefabcdefab'
        >>> b.n
        59377482839139050825606534576063885287
        >>> b.cells
        [0, 0, 749449200, 1774140626, 3139018916, 292801225]
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

        if len(id) not in groups:
            raise WrongIdentifier(f"Wrong identifier length: {len(id)}   id:[{id}]")
        return Hosh(cells_fromid(id, p=groups[len(id)].p), version=groups[len(id)])

    @classmethod
    def fromn(cls, n: int, version=UT40_4):
        """
        Create a Hosh object representing the given int.

        Default 'p' is according to version UT64.4.

        Usage:

        >>> h = Hosh.fromn(7647544756746324134134)
        >>> h.id
        '00_e49c1c505dcd0039e91000000000000000000'

        Parameters
        ----------
        n
        version

        Returns
        -------
        A new Hosh object
        """
        p, order = version.p, version.p6
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
        'ȟɟìӧДɫŖāöơɟբƢŊþXÊϱՎҲģţՀɄЌ'

        Returns
        -------
        Short utf-8 textual representation
        """
        if self._sid is None:
            self._sid = b777enc(self.n, self.digits * 5 // 8)
        return self._sid

    @property
    def ansi(self):
        r"""
        Colored textual (ANSI) representation of this element

        >>> from garoupa import Hosh
        >>> Hosh.fromid("Iaz3L67a2BQv0GifoWOjWale6LYFTGmJJ1ZPfdoP").ansi
        '\x1b[38;5;229m\x1b[1m\x1b[48;5;0mI\x1b[0m\x1b[38;5;228m\x1b[1m\x1b[48;5;0ma\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0mz\x1b[0m\x1b[38;5;223m\x1b[1m\x1b[48;5;0m3\x1b[0m\x1b[38;5;228m\x1b[1m\x1b[48;5;0mL\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0m6\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0m7\x1b[0m\x1b[38;5;223m\x1b[1m\x1b[48;5;0ma\x1b[0m\x1b[38;5;228m\x1b[1m\x1b[48;5;0m2\x1b[0m\x1b[38;5;221m\x1b[1m\x1b[48;5;0mB\x1b[0m\x1b[38;5;216m\x1b[1m\x1b[48;5;0mQ\x1b[0m\x1b[38;5;186m\x1b[1m\x1b[48;5;0mv\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0m0\x1b[0m\x1b[38;5;221m\x1b[1m\x1b[48;5;0mG\x1b[0m\x1b[38;5;181m\x1b[1m\x1b[48;5;0mi\x1b[0m\x1b[38;5;194m\x1b[1m\x1b[48;5;0mf\x1b[0m\x1b[38;5;229m\x1b[1m\x1b[48;5;0mo\x1b[0m\x1b[38;5;228m\x1b[1m\x1b[48;5;0mW\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0mO\x1b[0m\x1b[38;5;223m\x1b[1m\x1b[48;5;0mj\x1b[0m\x1b[38;5;228m\x1b[1m\x1b[48;5;0mW\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0ma\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0ml\x1b[0m\x1b[38;5;223m\x1b[1m\x1b[48;5;0me\x1b[0m\x1b[38;5;228m\x1b[1m\x1b[48;5;0m6\x1b[0m\x1b[38;5;221m\x1b[1m\x1b[48;5;0mL\x1b[0m\x1b[38;5;216m\x1b[1m\x1b[48;5;0mY\x1b[0m\x1b[38;5;186m\x1b[1m\x1b[48;5;0mF\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0mT\x1b[0m\x1b[38;5;221m\x1b[1m\x1b[48;5;0mG\x1b[0m\x1b[38;5;181m\x1b[1m\x1b[48;5;0mm\x1b[0m\x1b[38;5;194m\x1b[1m\x1b[48;5;0mJ\x1b[0m\x1b[38;5;229m\x1b[1m\x1b[48;5;0mJ\x1b[0m\x1b[38;5;228m\x1b[1m\x1b[48;5;0m1\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0mZ\x1b[0m\x1b[38;5;223m\x1b[1m\x1b[48;5;0mP\x1b[0m\x1b[38;5;228m\x1b[1m\x1b[48;5;0mf\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0md\x1b[0m\x1b[38;5;222m\x1b[1m\x1b[48;5;0mo\x1b[0m\x1b[38;5;223m\x1b[1m\x1b[48;5;0mP\x1b[0m'

        Returns
        -------
        Textual representation
        """
        if self._ansi is None:
            self._ansi = id2ansi(self.id)
        return self._ansi

    @property
    def idc(self):
        return self.ansi

    @property
    def rgb(self):
        """
        Colored textual (RGB) representation of this element

        >>> from garoupa import Hosh
        >>> Hosh.fromid("Iaz3L67a2BQv0GifoWOjWale6LYFTGmJJ1ZPfdoP").rgb
        [[6, 28, 104], [255, 255, 184], [255, 255, 141], [255, 220, 155], [255, 233, 172], [255, 250, 139], [255, 218, 144], [254, 223, 150], [255, 229, 187], [255, 255, 127], [255, 206, 98], [242, 176, 123], [212, 201, 138], [237, 216, 120], [252, 198, 115], [234, 193, 174], [229, 253, 204], [255, 255, 184], [255, 255, 141], [255, 220, 155], [255, 233, 172], [255, 250, 139], [255, 218, 144], [254, 223, 150], [255, 229, 187], [255, 255, 127], [255, 206, 98], [242, 176, 123], [212, 201, 138], [237, 216, 120], [252, 198, 115], [234, 193, 174], [229, 253, 204], [255, 255, 184], [255, 255, 141], [255, 220, 155], [255, 233, 172], [255, 250, 139], [255, 218, 144], [254, 223, 150], [255, 229, 187]]
        """
        if self._rgb is None:
            self._rgb = id2rgb(self.id)
        return self._rgb

    @property
    def html(self):
        """
        HTML page containing a colored textual representation of this element

        Returns
        -------
        Textual representation
        """
        return ansi2html(self.ansi)

    @property
    def sidc(self):
        """
        Shorter colored id (base-922 using up to 2 bytes utf8 per char)

        Usage:

        >>> from garoupa import ø
        >>> print((ø * b'65e987978g').sidc)
        \x1b[38;5;156m\x1b[1m\x1b[48;5;0mȟ\x1b[0m\x1b[38;5;155m\x1b[1m\x1b[48;5;0mɟ\x1b[0m\x1b[38;5;185m\x1b[1m\x1b[48;5;0mì\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0mӧ\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0mД\x1b[0m\x1b[38;5;185m\x1b[1m\x1b[48;5;0mɫ\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0mŖ\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0mā\x1b[0m\x1b[38;5;149m\x1b[1m\x1b[48;5;0mö\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0mơ\x1b[0m\x1b[38;5;83m\x1b[1m\x1b[48;5;0mɟ\x1b[0m\x1b[38;5;155m\x1b[1m\x1b[48;5;0mբ\x1b[0m\x1b[38;5;149m\x1b[1m\x1b[48;5;0mƢ\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0mŊ\x1b[0m\x1b[38;5;185m\x1b[1m\x1b[48;5;0mþ\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0mX\x1b[0m\x1b[38;5;156m\x1b[1m\x1b[48;5;0mÊ\x1b[0m\x1b[38;5;155m\x1b[1m\x1b[48;5;0mϱ\x1b[0m\x1b[38;5;185m\x1b[1m\x1b[48;5;0mՎ\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0mҲ\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0mģ\x1b[0m\x1b[38;5;185m\x1b[1m\x1b[48;5;0mţ\x1b[0m\x1b[38;5;113m\x1b[1m\x1b[48;5;0mՀ\x1b[0m\x1b[38;5;119m\x1b[1m\x1b[48;5;0mɄ\x1b[0m\x1b[38;5;149m\x1b[1m\x1b[48;5;0mЌ\x1b[0m

        Returns
        -------
        Short utf-8 colored textual representation
        """
        if self._sidc is None:
            self._sidc = id2ansi(self.sid)
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

    def __rmul__(self, other: Union["Hosh", str, bytes, int]):
        """
        >>> from garoupa import ø
        >>> (ø * b"13dfv34y4" )* b"434vbfrdg" == b"13dfv34y4" * (ø * b"434vbfrdg")
        True

        Parameters
        ----------
        other

        Returns
        -------

        """
        return Hosh(cellsmul(self.convert(other).cells, self.cells, self.p), version=self.version)

    def __rpow__(self, other):
        """
        >>> from garoupa import ø
        >>> (ø * b"13dfv34y4") ** b"434vbfrdg" == b"13dfv34y4" ** (ø * b"434vbfrdg")
        True

        Parameters
        ----------
        other

        Returns
        -------

        """
        return +(+self.convert(other) * +self)

    def __pow__(self, power, modulo=None):
        return +(+self * +self.convert(power))

    def __rfloordiv__(self, other):
        """
        >>> from garoupa import ø
        >>> (ø * b"13dfv34y4") // b"434vbfrdg" == b"13dfv34y4" // (ø * b"434vbfrdg")
        True

        Parameters
        ----------
        other

        Returns
        -------

        """
        return +(+self.convert(other) / +self)

    def __floordiv__(self, other):
        """Lift"""
        return +(+self / +self.convert(other))

    def __neg__(self):
        """Change disposition of element-matrix cells in a way that even hybrid ids will not commute.
        ps. This differs from +hosh because it creates a lower element.

        Switch positions of cells a2 and a4. This operation is it own inverse.

        Cells are represented as a list in the format: [a5, a4, a3, a2, a1, a0]
        Cells are represented as a matrix in the format:
        1 a4 a1 a0
        0  1 a2 a3
        0  0  1 a5
        0  0  0  1

        """
        cells = self.cells.copy()
        cells[3] = cells[1]
        cells[1] = self.cells[3]
        return Hosh(cells, version=self.version)

    def __pos__(self):
        """Change disposition of element-matrix cells in a way that even hybrid ids will not commute.
        ps. This differs from -hosh because it creates a higher element.
        For this reason it is adopted in __floordiv__

        Switch positions of cells a2 and a5. This operation is it own inverse.

        Cells are represented as a list in the format: [a5, a4, a3, a2, a1, a0]
        Cells are represented as a matrix in the format:
        1 a4 a1 a0
        0  1 a2 a3
        0  0  1 a5
        0  0  0  1

        """
        cells = self.cells.copy()
        cells[3] = cells[0]
        cells[0] = self.cells[3]
        return Hosh(cells, version=self.version)

    def __invert__(self):
        return Hosh(cellsinv(self.cells, self.p), version=self.version)

    def __rtruediv__(self, other):
        """
        >>> from garoupa import ø
        >>> (ø * b"13dfv34y4") / b"434vbfrdg" == b"13dfv34y4" / (ø * b"434vbfrdg")
        True

        Parameters
        ----------
        other

        Returns
        -------

        """
        return Hosh(cellsmul(self.convert(other).cells, cellsinv(self.cells, self.p), self.p), version=self.version)

    def __truediv__(self, other):
        return Hosh(cellsmul(self.cells, cellsinv(self.convert(other).cells, self.p), self.p), version=self.version)

    def __add__(self, other):
        """Matrix addition modulo p, keeping unidiagonal"""
        cells = list(map(lambda x, y: (x + y) % self.p, self.cells, self.convert(other).cells))
        return Hosh(cells, version=self.version)

    def __sub__(self, other):
        """Matrix subtraction modulo p, keeping unidiagonal"""
        cells = list(map(lambda x, y: (x - y) % self.p, self.cells, self.convert(other).cells))
        return Hosh(cells, version=self.version)
        # REMINDER: the chosen implementation differs from the alternative bellow!
        # return Hosh.fromn((self.n + self.convert(other).n) % self.order, self.version)

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
        voh8t1KrYmzCqpyrUO9.5QbGdouoZsnExarMSa34
        """
        return print(self.idc if colored else self.id)

    def short(self, colored=True):
        """
        Usage:

        >>> Hosh(b"asdf86fasd").short(colored=False)
        lϊӑơӫǯÃϺŮϳȐŁЬĽҪƉǏԛȪƜfÞӠȕՇ
        """
        return print(self.sidc if colored else self.sid)

    def __hash__(self):
        return self.n % maxsize

    def convert(self, other):
        """
        Usage:

        >>> from garoupa import ø
        >>> ø.convert([0,0,0,0,0,0]).id
        '0000000000000000000000000000000000000000'

        >>> from garoupa import Hosh
        >>> ø.convert(0).id
        '0000000000000000000000000000000000000000'

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
