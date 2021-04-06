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
from dataclasses import dataclass
from itertools import repeat, islice
from multiprocessing import Value, Lock
from random import Random

import pathos.multiprocessing as mp
from lange import GP

from garoupa.algebra.abs.element import Element


@dataclass
class Group:
    identity: Element
    sorted: callable
    seed: int = 0
    _commuting_pairs, _comparisons = Value('i', 0), Value('i', 0)
    _mutex = Lock()

    def __post_init__(self):
        self.bits = self.identity.bits
        self.order = self.identity.order
        self.name = self.__class__.__name__
        self.rnd = Random(self.seed)

    def sampled_commuting_freq(self, pairs=5_000, runs=1_000_000_000_000):
        """
        Usage:
        >>> from garoupa.algebra.matrix import M
        >>> G = M(5)
        >>> max(sorted(G.sampled_commuting_freq(pairs=1000, runs=4)))
        (272, 4000)
        """

        def thread(idx):
            A, B = self.replace(seed=idx), self.replace(seed=idx + 1)
            with Group._commuting_pairs.get_lock(), Group._comparisons.get_lock():
                comms = Group._commuting_pairs.value
                n = Group._comparisons.value
            for a, b in islice(zip(A, B), 0, pairs):
                if a * b == b * a:
                    with Group._commuting_pairs.get_lock():
                        Group._commuting_pairs.value += 1
                with Group._commuting_pairs.get_lock(), Group._comparisons.get_lock():
                    Group._comparisons.value += 1
                    comms = Group._commuting_pairs.value
                    n = Group._comparisons.value
            return comms, n

        Group._commuting_pairs.value = 0
        Group._comparisons.value = 0
        if runs == 1:
            thread(0)
        else:
            last_total = -1
            for comms, n in mp.ProcessingPool().imap(thread, range(0, 2 * runs, 2)):
                with self._mutex:
                    if n > last_total:
                        last_total = n
                        yield comms, n

    @property
    def comm_degree(self):
        raise Exception(f"Not implemented for groups from class {self.name}."
                        "HINT: Use sampled_comm_degree()", self.name)

    def __iter__(self):
        raise Exception("Not implemented for groups of the class", self.name)

    def sampled_orders(self, sample=100, width=10, limits=[100, 101, ..., 1_000_000_000_000_000_000]):
        """Histogram of element orders. Detect identity after many repetitions

        Usage:
        >>> from garoupa.algebra.symmetric import S
        >>> for hist in S(4).sampled_orders(width=1, limits=[1, 1.1, ..., 999_999]):
        ...     print(hist)
        {}
        {(1, 1): 9}
        {(1, 1): 13}
        {(1, 1): 11, (2, 2): 38}
        {(1, 1): 5, (2, 2): 37, (3, 3): 40}
        {(1, 1): 7, (2, 2): 39, (3, 3): 22, (4, 4): 32}
        """
        hist = {}

        def thread(limit):
            G = self.replace(seed=limit)
            for a in islice(G, 0, sample):
                r = a
                for i in range(1, int(limit)):
                    if r == G.identity:
                        with self._mutex:
                            bin = (i // width) * width + width // 2
                            key = bin - width // 2, bin + width // 2
                            if key not in hist:
                                hist[key] = 0
                            hist[key] += 1
                        break
                    r = r * a

            # REMINDER: Python multithreading is really full of unneeded pitfalls:
            #   local variable hist is copied to all threads;
            #   strangely, it is not one copy per thread, it is a copy for them all;
            #   the local variable will be untouched,
            #   so we need to return it.
            return hist

        if len(limits) == 1:
            yield thread(limits[0])
        else:
            last_total = -1
            for h in mp.ProcessingPool().imap(thread, GP(*limits)):
                with self._mutex:
                    tot = sum(h.values())
                    if tot > last_total:
                        last_total = tot
                        yield dict(sorted(list(h.items())))

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
