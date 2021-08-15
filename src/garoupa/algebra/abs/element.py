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
import operator
from abc import abstractmethod, ABC
from dataclasses import dataclass
from functools import reduce
from math import log

from garoupa import Hash


@dataclass
class Element(ABC):
    i: int
    order: int
    _id = None
    _hash = None

    def __post_init__(self):
        """
        Usage:

        >>> from garoupa.algebra.dihedral import Ds
        >>> Ds(64**2, 64**32).bits - 1
        192.0
        """
        self.name = f"{self.__class__.__name__.lower()}_{self.i}"
        self.bits = log(self.order, 2)

    @abstractmethod
    def __mul__(self, other):
        pass

    def __xor__(self, other):
        """
        Usage:

        >>> from garoupa.algebra.dihedral import Ds
        >>> Ds(64**2,64**5) ^ 3
        ds4096
        """
        return reduce(operator.mul, [self] * other)

    __pow__ = __xor__

    def __repr__(self):
        """
        Usage:

        >>> from garoupa.algebra.dihedral import Ds
        >>> Ds(64**3, 64**5) ^ 3
        ds262144
        """
        return self.name

    def __eq__(self, other):
        """
        Usage:

        >>> from garoupa.algebra.dihedral import Ds
        >>> Ds(64**2, 64**5) ^ 3 == Ds(4096, 64**5)
        True
        """
        return self.name == other.name

    def __hash__(self):
        """
        Usage:

        >>> from garoupa.algebra.dihedral import Ds
        >>> isinstance(hash(Ds(64**2,64**5)), int)
        True
        """
        return hash(repr(self))

    @property
    def hash(self):
        """
        Usage:

        >>> from garoupa.algebra.dihedral import Ds
        >>> Ds(64**2,64**5).hash.id
        '0000000000000000000000000000000000000000000000000000000000000100'
        """
        if self._hash is None:
            self._hash = Hash.fromn(self.i)
        return self._hash

    @property
    def id(self):
        """
        Usage:

        >>> from garoupa.algebra.dihedral import Ds
        >>> Ds(64**2,64**5).id
        '0000000000000000000000000000000000000000000000000000000000000100'
        """
        if self._id is None:
            self._id = self.hash.id
        return self._id
