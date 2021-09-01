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

from garoupa.algebra.matrix.group import Group
from garoupa.algebra.matrix.mat8bit import Mat8bit


class M8bit(Group):
    def __init__(self, seed=None):
        """
        Usage:

        >>> G = M8bit(seed=0)
        >>> G, ~G
        (M8bit, [[1. 0. 1. 1. 0.]
         [0. 1. 1. 1. 0.]
         [0. 0. 1. 0. 0.]
         [0. 0. 0. 1. 0.]
         [0. 0. 0. 0. 1.]])
        """

        super().__init__(Mat8bit(0), lambda: (Mat8bit(i) for i in range(self.order)), seed)

    def __iter__(self):
        while True:
            yield Mat8bit(self.samplei())

    def __repr__(self):
        return self.__class__.__name__

    def replace(self, *args, **kwargs):
        """
        Usage:

        >>> G = M8bit(seed=0)
        >>> ~G.replace(seed=1)
        [[1. 0. 0. 0. 1.]
         [0. 1. 0. 0. 0.]
         [0. 0. 1. 1. 0.]
         [0. 0. 0. 1. 0.]
         [0. 0. 0. 0. 1.]]
        """
        dic = {"seed": self.seed}
        dic.update(kwargs)
        return self.__class__(**dic)
