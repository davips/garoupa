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


class Dr(Element):
    def __init__(self, j, n):
        super().__init__(n + j, 2 * n)
        self.j = j
        self.n = n
        self.name = self.name.split("_")[0] + str(self.j)

    def __mul__(self, other):
        j = (self.j + other.j) % self.n
        if isinstance(other, Dr):
            return Dr(j, self.n)
        else:
            from garoupa.algebra.dihedral.ds import Ds

            return Ds(j, self.n)
