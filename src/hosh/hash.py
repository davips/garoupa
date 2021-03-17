from functools import reduce

from hosh.core import n_bin_id_fromblob, bin_id_fromn, n_bin_fromid, n_id_fromperm
from hosh.math import pmat_transpose, pmat_mult, pmat_inv


class Hash:
    def __init__(self, n=None, blob=None, id=None, bin=None):
        if blob:  # 1.54us
            self._n, self._bin, self._id = n_bin_id_fromblob(blob)
        else:
            self._n, self._id, self._bin = n, id, bin

    def calculate(self):
        if self._bin:  # 1.11us
            self._n, self._id = n_id_fromperm(self._bin)
        elif self._id:  # 1.17us
            self._n, self._bin = n_bin_fromid(self._id)
        elif self._n is not None:  # 1.49us vs 3.7us (rust vs python)
            self._bin, self._id = bin_id_fromn(self._n)
        else:
            raise Exception("Missing argument.")

    @property
    def bin(self):
        if self._bin is None:
            self.calculate()
        return self._bin

    @property
    def id(self):
        if self._id is None:
            self.calculate()
        return self._id

    @property
    def n(self):
        if self._n is None:
            self.calculate()
        return self._n

    def __mul__(self, other):  # 1.63 µs vs 1.43us
        return Hash(bin=pmat_mult(self.bin, other.bin))

    def __invert__(self):  # 3.22 µs vs 560ns
        return Hash(bin=pmat_inv(self.bin))

    def __truediv__(self, other):  # 4.44 µs vs 704ns
        return Hash(bin=pmat_mult(self.bin, pmat_inv(other.bin)))

    def __add__(self, other):  # 534ns
        return Hash(n=(self.n + other.n) % 295232799039604140847618609643520000000)  # 34!

    def __sub__(self, other):  # 530ns
        return Hash(n=(self.n - other.n) % 295232799039604140847618609643520000000)  # 34!

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id

    @classmethod
    def muls(cls, *perms):  # 23.6 µs
        return Hash(bin=reduce(pmat_mult, [p.bin for p in perms]))

    @classmethod
    def pairmuls(cls, *pairs):  # 5.34 µs
        results = map(lambda a, b: pmat_mult(a.bin, b.bin), pairs[::2], pairs[1::2])
        return [Hash(bin=res) for res in results]
