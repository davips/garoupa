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

from garoupa.algebra.abs.element import Element


class Nat(Element):
    """
    Usage:

    >>> a = Nat(1414343245,2**32)
    >>> b = Nat(77639,2**32)
    >>> b
    77639
    >>> ~b
    4294889657
    >>> a * b
    1414420884
    >>> a * b * ~b == a
    True

    """

    def __init__(self, i, n):
        super().__init__(i, n)
        self.n = n

    def __mul__(self, other):
        return Nat((self.i + other.i) % self.n, self.n)

    def __repr__(self):
        return f"{self.i}"

    def __invert__(self):
        return Nat(self.order - self.i, self.n)
