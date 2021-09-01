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


class Tuple(Element):
    def __init__(self, *subelements):
        self.subelements = subelements
        order = 1
        i = 0
        for a in reversed(subelements):
            i += order * a.i
            order *= a.order
        super().__init__(i, order)

    def __mul__(self, other):
        return Tuple(*(a * b for a, b in zip(self.subelements, other.subelements)))

    def __repr__(self):
        return f"«{', '.join([str(a) for a in self.subelements])}»"

    def __invert__(self):
        return Tuple(*(~a for a in self.subelements))
