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
from dataclasses import dataclass, replace
from itertools import repeat, islice
from multiprocessing import Value, Lock
from pprint import pprint
from random import Random
from timeit import timeit

import pathos.multiprocessing as mp
from lange import gp

from garoupa.algebra.abs.element import Element


@dataclass
class Group:
    identity: Element
    sorted: callable
    seed: int = 0
    _commuting_pairs, _comparisons, _last_printed = Value('i', 0), Value('i', 0), Value('i', -1)

    def __post_init__(self):
        self.bits = self.identity.bits
        self.order = self.identity.order
        self.name = self.__class__.__name__
        self.rnd = Random(self.seed)

    def sampled_comm_degree(self, chunksize=5_000, nchunks=1_000_000):
        """
        Usage:
        >>> import io
        >>> from contextlib import redirect_stdout
        >>> from garoupa.algebra.symmetric import S
        >>> G = S(4)
        >>> f = io.StringIO()
        >>> with redirect_stdout(f):
        ...     G.sampled_comm_degree(chunksize=10000, nchunks=1)
        >>> print(f"Expected: {G.comm_degree:.4}\t\tEstimated: {f.getvalue()}")  # doctest: +NORMALIZE_WHITESPACE
            Expected: 0.2542         Estimated:     2443/10000:	~24.43%
        """

        def thread(idx):
            A, B = self.replace(seed=idx), self.replace(seed=idx + 1)
            for a, b in islice(zip(A, B), 0, chunksize):
                if a * b == b * a:
                    with Group._commuting_pairs.get_lock():
                        Group._commuting_pairs.value += 1
                with Group._comparisons.get_lock():
                    Group._comparisons.value += 1
            with Group._last_printed.get_lock(), Group._commuting_pairs.get_lock(), Group._comparisons.get_lock():
                comms = Group._commuting_pairs.value
                n = Group._comparisons.value
                if n > Group._last_printed.value:
                    Group._last_printed.value = n
                    print(f"{comms}/{n}:".rjust(15, ' '), f"\t~{100 * comms / n}%", sep="", flush=True)
            return comms, n

        Group._commuting_pairs.value = 0
        Group._comparisons.value = 0
        Group._last_printed.value = 0
        if nchunks == 1:
            thread(0)
        else:
            lst = mp.ProcessingPool().map(thread, range(0, 2 * nchunks, 2))
            comms, n = sorted(lst)[-1]
            print(self, f"{comms}/{n}:".rjust(15, ' '), f"\t~{100 * comms / n}%", sep="", flush=True)

    @property
    def comm_degree(self):
        raise Exception(f"Not implemented for groups from class {self.name}."
                        "HINT: Use sampled_comm_degree()", self.name)

    def __iter__(self):
        raise Exception("Not implemented for groups of the class", self.name)

    def __invert__(self) -> Element:
        return next(iter(self))

    def samplei(self):
        return self.rnd.getrandbits(int(self.bits))

    def __mul__(self, other):
        from garoupa.algebra.product import Product
        return Product(self, other)

    def __xor__(self, other):
        from garoupa.algebra.product import Product
        return Product(*repeat(self, other))

    __pow__ = __xor__

    def replace(self, *args, **kwargs):
        raise Exception("Not implemented for groups of the class", self.name)
