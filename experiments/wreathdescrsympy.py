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

from sympy.combinatorics import SymmetricGroup


def unrank(number, sylowsg):
    # Como obter o rank lexicográfico do elemento, dados os generators?
    # Só vai no intratavelmente exaustivo?
    return list(sylowsg.elements)[number].list()


def int_to_subelement(number, p):
    res, rem = divmod(number, p)
    sylowsg = SymmetricGroup(p ** 2).sylow_subgroup(p)
    return unrank(res, sylowsg)


def int_to_elem(x):
    res = x
    e = [None] * 7
    for i, p in enumerate([2, 3, 5, 7, 11, 13, 17]):
        radix = p ** (p + 1)
        res, rem = divmod(res, radix)
        e[6 - i] = 0 if rem == 0 else int_to_subelement(rem, p)
    return e


e = int_to_elem(3428723)
print(e)
# [0, 0, 0, 0, [2, 3, 4, 0, 1, 5, 6, 7, 8, 9, 14, 10, 11, 12, 13, 18, 19, 15, 16, 17, 22, 23, 24, 20, 21], [8, 6, 7, 0, 1, 2, 4, 5, 3], [1, 0, 2, 3]]

