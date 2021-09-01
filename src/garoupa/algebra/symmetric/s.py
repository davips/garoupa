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

from math import pi, sqrt, exp, factorial

from garoupa.algebra.matrix.group import Group
from garoupa.algebra.symmetric.perm import Perm


class S(Group):
    def __init__(self, n, seed=None):
        identity = Perm(0, n)
        sorted = lambda: (Perm(i, self.n) for i in range(identity.order))
        super().__init__(identity, sorted, seed)
        self.n = n

    @property
    def comm_degree(self):
        """Asymptotic commutativity degree (value is between Sn and An)"""
        num = exp(2 * pi * sqrt(self.n / 6))
        den = 4 * self.n * sqrt(3) * factorial(self.n)
        return num / den

    # def P442(self, p):
    #     """4-Property p-group"""
    #     num = p**(p-1) + p**2 - 1
    #     den = p**(p+1)
    #     return num / den

    def __iter__(self):
        while True:
            yield Perm(self.samplei(), self.n)

    def __repr__(self):
        return f"S{self.n}"

    def replace(self, *args, **kwargs):
        dic = {"n": self.n, "seed": self.seed}
        dic.update(kwargs)
        return self.__class__(**dic)
