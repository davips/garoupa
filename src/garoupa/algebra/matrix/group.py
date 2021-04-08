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
import sys
from dataclasses import dataclass
from time import time

from progress.bar import Bar
from itertools import repeat, islice
from math import inf
from multiprocessing import Value, Lock
from random import Random
from multiprocessing import Manager

import pathos.multiprocessing as mp

from garoupa.algebra.abs.element import Element


# @dataclass
# class Group:
#     identity: Element
#     sorted: callable
#     seed: int = None

class Group:
    _commuting_pairs, _comparisons = Value('i', 0), Value('i', 0)
    _mutex = Lock()

    def __init__(self, identity: Element, sorted: callable, seed: int = None):
        self.identity, self.sorted, self.seed = identity, sorted, seed
        self.bits = self.identity.bits
        self.order = self.identity.order
        self.name = self.__class__.__name__
        if self.seed is None:
            self.seed = int(time() * 1000000000)
        self.rnd = Random(self.seed)

    def sampled_commuting_freq(self, pairs=5_000, runs=1_000_000_000_000):
        """
        Usage:
        >>> from garoupa.algebra.matrix import M
        >>> G = M(5, seed=0)
        >>> max(sorted(G.sampled_commuting_freq(pairs=1000, runs=4)))
        (272, 4000)
        """

        def thread(idx):
            A, B = self.replace(seed=idx + self.seed), self.replace(seed=idx + 1 + self.seed)
            with Group._commuting_pairs.get_lock(), Group._comparisons.get_lock():
                comms = Group._commuting_pairs.value
                n = Group._comparisons.value
                for a, b in Bar('Processing', max=pairs).iter(islice(zip(A, B), 0, pairs)):
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

    def sampled_orders(self, sample=100, width=10, limit=100, logfreq=10):
        """Histogram of element orders. Detect identity after many repetitions

        Usage:
        >>> from garoupa.algebra.symmetric import S
        >>> tot = 0
        >>> list(S(6, seed=0).sampled_orders(sample=1, width=2))
        [{(6, 7): 1}]
        >>> for hist in S(6, seed=0).sampled_orders(width=2):
        ...     print(hist)  # doctest: +SKIP
        {(0, 1): 1, (2, 3): 16, (4, 5): 6}
        {(0, 1): 1, (2, 3): 23, (4, 5): 7}
        {(0, 1): 1, (2, 3): 27, (4, 5): 11}
        {(0, 1): 1, (2, 3): 33, (4, 5): 13}
        {(0, 1): 1, (2, 3): 40, (4, 5): 14}
        {(0, 1): 3, (2, 3): 56, (4, 5): 20}
        {(0, 1): 4, (2, 3): 66, (4, 5): 29}
        {(0, 1): 4, (2, 3): 67, (4, 5): 29}
        """
        hist = Manager().dict()

        def thread(a):
            r = a
            for i in range(1, limit + 1):
                if r == self.identity:
                    bin = (i // width) * width + width // 2
                    key = bin - width // 2, bin + width // 2 - 1
                    with self._mutex:
                        if key not in hist:
                            hist[key] = 0
                        hist[key] += 1
                    break
                r = r * a
            if r != self.identity:
                key = inf, inf
                with self._mutex:
                    if key not in hist:
                        hist[key] = 0
                    hist[key] += 1
            # REMINDER: Python multithreading is really full of unneeded pitfalls:
            #   local variable hist is copied to all threads;
            #   the local variable will be untouched,
            #   so we need to return it.
            return hist

        last_total, previous = -1, 0
        with Bar('Processing', max=sample, suffix='%(percent)f%%  %(index)d/%(max)d  ETA: %(eta)ds') as bar:
            for h in mp.ProcessingPool().imap(thread, islice(self, 0, sample)):
                with self._mutex:
                    t = sum(h.values())
                bar.next()
                now = bar.elapsed + 1
                if now > previous + logfreq:
                    previous = now
                    with self._mutex:
                        tot = sum(h.values())
                        if tot > last_total:
                            last_total = tot
                            sys.stdout.write("\x1b[1A")  # "\x1b[2K")
                            yield dict(sorted(list(h.items())))
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
