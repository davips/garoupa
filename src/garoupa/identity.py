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
#  Relevant employers or funding agencies will be notified accordingly.
from garoupa import Hosh


class Identity(Hosh):
    def __init__(self, version, etype="ordered"):
        super().__init__(None, etype, version)
        self._cells = [0, 0, 0, 0, 0, 0]

    @property
    def u(self):
        """Shortcut to induce etype=unordered in the next operand, when it is not a ready Hosh object.
        default=Ordered, h=Hybrid and u=Unordered

        Usage:

        >>> from garoupa import ø, Ø, Hosh
        >>> a = ø.u * b"654"
        >>> print(a)
        000000000000000000000000000kYNjp
        >>> b = Ø.u * b"654"
        >>> print(b)
        000000000000000000000000000000000000000000000000000007Oe9Pkyj58r
        >>> Hosh(b"654", "unordered", "UT32.4") == a and b == Hosh(b"654","unordered", "UT64.4")
        True
        """
        return Identity(self.version, "unordered")

    @property
    def h(self):
        """Shortcut to induce etype=hybrid in the next operand, when it is given as a bytes object.
        default=Ordered, h=Hybrid and u=Unordered

        Usage:

        >>> from garoupa import ø, Ø, Hosh
        >>> a = ø.h * b"654"
        >>> print(a)
        0000000000167KF1DMkyi2pJsjygdObZ
        >>> b = Ø.h * b"654"
        >>> print(b)
        0000000000000000000000eZ7EUaEx7AwXByek6Nl1dSRveP.VZeAE4-oWVLSrc8
        >>> Hosh(b"654", "hybrid", "UT32.4") == a and b == Hosh(b"654","hybrid", "UT64.4")
        True
        """
        return Identity(self.version, "hybrid")
