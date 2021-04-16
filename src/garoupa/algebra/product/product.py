#  Copyright (c) 2021. Davi Pereira dos Santos
#
#  Function based on Gabriel Dalforno code:
#  order_hist_mul
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

import operator
from functools import reduce
from itertools import product, cycle

from garoupa.algebra.matrix.group import Group
from garoupa.algebra.product.tuple import Tuple


class Product(Group):
    def __init__(self, *groups, seed=None):
        self.groups = groups
        identity = Tuple(*(g.identity for g in self.groups))
        sorted = lambda: (Tuple(*es) for es in product(*(g.sorted() for g in self.groups)))
        super().__init__(identity, sorted, seed)

    @property
    def comm_degree(self):
        comms = [g.comm_degree for g in self.groups]
        if any(comm is None for comm in comms):
            return
        return reduce(operator.mul, comms)

    def __iter__(self):
        its = [cycle(iter(g)) for g in self.groups]
        while True:
            yield Tuple(*(next(it) for it in its))

    def __repr__(self):
        return "×".join([str(g) for g in self.groups])

    def __mul__(self, other):
        if isinstance(other, Product):
            return Product(*self.groups, *other.groups)
        return Product(*self.groups, other)

    def replace(self, *args, **kwargs):
        dic = {"seed": self.seed}
        dic.update(kwargs)
        groups = args or self.groups
        return self.__class__(*groups, **dic)

    @classmethod
    def order_hist_mul(cls, hista, histb):
        """Histogram of element orders for a product of 2 groups.

        Usage
        >>> from garoupa.algebra.dihedral import D
        >>> Product.order_hist_mul(D(5).order_hist, D(7).order_hist)
        {1: 1, 2: 47, 5: 4, 7: 6, 10: 28, 14: 30, 35: 24}

        Based on Gabriel Dalforno code."""
        hist = {}
        for k1 in hista.keys():
            for k2 in histb.keys():
                key = cls.lcm(k1, k2)
                if key not in hist.keys():
                    hist[key] = hista[k1] * histb[k2]
                else:
                    hist[key] += hista[k1] * histb[k2]
        return dict(sorted(hist.items()))

    @property
    def order_hist(self):
        """Sorted histogram of element orders.

        Usage
        >>> from garoupa.algebra.dihedral import D
        >>> (D(3) * D(5) * D(7)).order_hist
        {1: 1, 2: 191, 3: 2, 5: 4, 6: 94, 7: 6, 10: 124, 14: 138, 15: 8, 21: 12, 30: 56, 35: 24, 42: 60, 70: 72, 105: 48}
        """
        if self._order_hist is None:
            self._order_hist = dict(sorted(reduce(self.order_hist_mul, (G.order_hist for G in self.groups)).items()))
        return self._order_hist

    def compact_order_hist_lowmem(self, max_histsize, preserve_upto, initial_binsize=1):
        """Memory-friendly histogram of element orders in a direct product

        Compact largest intermediate histograms during calculation to avoid memory exhaustion.
        Nested products will also be processed through this method.
        Final and temporary hist may exceed max_histsize by a factor of 2 at most.

        Usage
        >>> from garoupa.algebra.dihedral import D
        >>> Product.order_hist_mul(D(7).order_hist, D(19).order_hist)
        {1: 1, 2: 159, 7: 6, 14: 114, 19: 18, 38: 126, 133: 108}
        >>> G = D(3) * D(5) * D(7) * D(9)
        >>> G.compact_order_hist(binsize=20)
        {9: 9136, 29: 1856, 42: 1968, 69: 1044, 90: 1080, 105: 480, 126: 1188, 210: 864, 315: 432, 630: 432}
        >>> G.compact_order_hist_lowmem(max_histsize=5, preserve_upto=0)
        Intermediate hist size for D3*D5 : 7
        Intermediate hist size for D3*D5*D7 : 8
        Intermediate hist size for D3*D5*D7*D9 : 8
        {6: 7616, 9: 2856, 12: 2560, 36: 960, 70: 2496, 210: 768, 315: 792, 630: 432}
        >>> G.compact_order_hist_lowmem(max_histsize=5, preserve_upto=10)
        Intermediate hist size for D3*D5 : 7
        Intermediate hist size for D3*D5*D7 : 15
        Intermediate hist size for D3*D5*D7*D9 : 20
        {1: 1, 2: 1919, 3: 20, 5: 4, 6: 2668, 7: 6, 9: 18, 10: 1276, 14: 54, 15: 24, 18: 1710, 21: 36, 24: 4768, 30: 744, 45: 24, 63: 36, 72: 1788, 84: 1920, 90: 744, 252: 720}
        """

        # if max_histsize <= preserve_upto:  errado
        #     raise Exception(f"Cannot preserve up to order {preserve_upto} limited by {max_histsize} at the same time.")

        def hists():
            for g in self.groups:
                if isinstance(g, Product):
                    yield str(g), g.compact_order_hist_lowmem(max_histsize, preserve_upto, initial_binsize)
                else:
                    yield str(g), g.order_hist

        binsize = [initial_binsize]

        def compact(hist):
            while True:
                hist = self.compact_order_hist(binsize=binsize[0], preserve_upto=preserve_upto, hist=hist)
                if len(hist) <= max_histsize or len(hist) <= preserve_upto:
                    break
                binsize[0] *= 2
            return hist

        def mul(tupa, tupb):
            ga, hista = tupa
            gb, histb = tupb
            hista = compact(hista)
            histb = compact(histb)
            hist = self.order_hist_mul(hista, histb)
            prod = f"{ga}*{gb}"
            print(f"Intermediate hist size for {prod} : {len(hist)}")
            return prod, hist

        return dict(sorted(reduce(mul, hists())[1].items()))
