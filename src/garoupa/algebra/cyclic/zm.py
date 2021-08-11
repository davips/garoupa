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
from garoupa.algebra.cyclic.natm import Natm
from garoupa.algebra.matrix.group import Group


class Zm(Group):
    def __init__(self, n, seed=None):
        """
        Usage:
        >>> G = Zm(1414343245, seed=0)
        >>> G.comm_degree
        1
        >>> G, ~G
        (Zm1414343245, 906691059)
        """
        sorted = lambda: (Natm(i, n) for i in range(n))
        super().__init__(Natm(1, n), sorted, seed)
        self.n = n

    @property
    def comm_degree(self):
        """Exact commutativity degree"""
        return 1

    def __iter__(self):
        while True:
            yield Natm(self.samplei(), self.n)

    def __repr__(self):
        return f"Zm{self.n}"

    def replace(self, *args, **kwargs):
        """
        Usage:
        >>> G = Zm(1414343245, seed=0)
        >>> ~G.replace(seed=1)
        144272509
        """
        dic = {"n": self.n, "seed": self.seed}
        dic.update(kwargs)
        return self.__class__(**dic)
