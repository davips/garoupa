#  Copyright (c) 2021. Davi Pereira dos Santos
#
#  Functions based on Gabriel Dalforno code:
#  gcd, lcm
#
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
from itertools import repeat, islice
from math import inf
from multiprocessing import Manager
from multiprocessing import Value, Lock
from random import Random
from time import time

from garoupa.algebra.abs.element import Element


class Group:
    _commuting_pairs, _comparisons, _interrupt = Value("i", 0), Value("i", 0), Value("i", 0)
    _mutex = Lock()
    _euler, _order_hist, _pi = None, None, None

    def __init__(self, identity: Element, sorted: callable, seed: int = None):
        self.identity, self.sorted, self.seed = identity, sorted, seed
        self.bits = self.identity.bits
        self.order = self.identity.order
        self.name = self.__class__.__name__
        if self.seed is None:
            self.seed = int(time() * 1000000000)
        self.rnd = Random(self.seed)

    def sampled_commuting_freq(self, pairs=5_000, runs=1_000_000_000_000, exitonhit=False):
        """
        Usage:

        >>> from garoupa.algebra.matrix import M
        >>> G = M(5, seed=0)
        >>> max(sorted(G.sampled_commuting_freq(pairs=1000, runs=4)))
        (272, 4000)
        """
        import pathos.multiprocessing as mp
        from progress.bar import Bar

        def thread(idx):
            A, B = self.replace(seed=idx + self.seed), self.replace(seed=idx + 1 + self.seed)
            with Group._commuting_pairs.get_lock(), Group._comparisons.get_lock():
                comms = Group._commuting_pairs.value
                n = Group._comparisons.value
                for a, b in Bar("Processing", max=pairs).iter(islice(zip(A, B), 0, pairs)):
                    if a * b == b * a:
                        if exitonhit:
                            with Group._interrupt.get_lock():
                                Group._interrupt.value = 1
                        with Group._commuting_pairs.get_lock():
                            Group._commuting_pairs.value += 1
                    with Group._commuting_pairs.get_lock(), Group._comparisons.get_lock():
                        Group._comparisons.value += 1
                        comms = Group._commuting_pairs.value
                        n = Group._comparisons.value
                    if Group._interrupt.value == 1:
                        break
                return comms, n

        Group._commuting_pairs.value = 0
        Group._comparisons.value = 0
        Group._interrupt.value = 0
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
        raise Exception(
            f"Not implemented for groups from class {self.name}." "HINT: Use sampled_comm_degree()", self.name
        )

    def __iter__(self):
        raise Exception("Not implemented for groups of the class", self.name)

    def sampled_orders(self, sample=100, width=10, limit=100, logfreq=10, exitonhit=False):
        """Histogram of element orders. Detect identity after many repetitions

        Usage:

        >>> from garoupa.algebra.symmetric import S
        >>> tot = 0
        >>> list(S(6, seed=0).sampled_orders(sample=1, width=2))
        [{(5, 8): 1}]
        >>> for hist in S(6, seed=0).sampled_orders(width=2):
        ...     print(hist)
        {(-1, 2): 1, (1, 4): 20, (3, 6): 45, (5, 8): 34}
        """
        hist = Manager().dict()

        def thread(a):
            r = a
            for i in range(1, limit + 1):
                if r == self.identity:
                    if exitonhit:
                        with Group._interrupt.get_lock():
                            Group._interrupt.value = 1
                    bin = (i // width) * width + width // 2
                    key = bin - width // 2 - 1, bin + width // 2
                    with self._mutex:
                        if key not in hist:
                            hist[key] = 0
                        hist[key] += 1
                    break
                if Group._interrupt.value == 1:
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

        Group._interrupt.value = 0
        last_total, previous = -1, 0
        import pathos.multiprocessing as mp
        from progress.bar import Bar

        with Bar("Processing", max=sample, suffix="%(percent)f%%  %(index)d/%(max)d  ETA: %(eta)ds") as bar:
            for h in mp.ProcessingPool().imap(thread, islice(self, 0, sample)):
                bar.next()
                now = bar.elapsed + 1
                if now > previous + logfreq:
                    with self._mutex:
                        tot = sum(h.values())
                        if tot > last_total:
                            previous = now
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

    @classmethod
    def lcm(cls, a, b):
        """Least common multiple

        Usage:

        >>> from garoupa.algebra.dihedral import D
        >>> D.lcm(32, 12)
        96

        Based on Gabriel Dalforno code."""
        return int((a * b) / cls.gcd(a, b))

    @classmethod
    def gcd(cls, a, b):
        """Greatest common divisor

        Usage:

        >>> from garoupa.algebra.dihedral import D
        >>> D.gcd(32, 12)
        4

        Based on Gabriel Dalforno code."""
        if a == 0:
            return b
        return cls.gcd(b % a, a)

    def compact_order_hist_lowmem(self, max_histsize, preserve_upto, initial_binsize=1):
        raise Exception(f"Method compact_order_hist_lowmem() not implemented for groups from class {self.name}.")

    def compact_order_hist(self, binsize, preserve_upto=0, max_histsize=inf, hist=None):
        """Compact histogram of element orders.

        Usage:

        >>> from garoupa.algebra.dihedral import D
        >>> (D(7) * D(19)).order_hist
        {1: 1, 2: 159, 7: 6, 14: 114, 19: 18, 38: 126, 133: 108}
        >>> (D(7) * D(19)).compact_order_hist(1)
        {1: 1, 2: 159, 7: 6, 14: 114, 19: 18, 38: 126, 133: 108}
        >>> (D(7) * D(19)).compact_order_hist(3)
        {1: 160, 7: 6, 14: 114, 19: 18, 38: 126, 133: 108}
        >>> (D(7) * D(19)).compact_order_hist(10)
        {2: 166, 14: 132, 38: 126, 133: 108}
        """
        hist = hist or self.order_hist
        result = {}
        it = iter(hist.items())
        c = 0
        while True:
            try:
                k, v = next(it)
                c += 1
            except StopIteration:
                result[0] = 0
                return result
            if k > preserve_upto or c >= max_histsize:
                break
            result[k] = v

        while True:
            binstart = k // binsize
            acc = 0
            binmiddle = 0
            try:
                while k // binsize == binstart:
                    acc += v
                    binmiddle += k * v
                    k, v = next(it)
            except StopIteration:
                break
            finally:
                result[binmiddle // acc] = acc
        return result

    @property
    def order_hist(self):
        raise Exception(f"Method order_hist() not implemented for groups from class {self.name}.")

    @staticmethod
    def _pi_core(hist):
        p = 0
        for order, freq in hist.items():
            p += freq / order
        return p / sum(hist.values())

    @property
    def pi(self):
        """Chance of stopping a repetition exactly at identity"""
        if self._pi is None:
            self._pi = self._pi_core(self.order_hist)
        return self._pi

    def pi_lowmem(self, max_histsize, preserve_upto=0, initial_binsize=1):
        """Approximmate Chance of stopping a repetition exactly at identity - memory-friendly"""
        hist = self.compact_order_hist_lowmem(max_histsize, preserve_upto, initial_binsize=initial_binsize)
        return self._pi_core(hist)
