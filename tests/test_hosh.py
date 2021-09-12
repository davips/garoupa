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
import sys
from unittest import TestCase

import pytest

from garoupa import ø
from garoupa.groups import UT64_4, UT40_4
from garoupa.hosh import (
    DanglingEtype,
    CellValueTooHigh,
    Hosh,
    WrongContent,
    WrongVersion,
    WrongOperands,
    ElementTooHigh,
    WrongIdentifier,
)
from garoupa.misc.identity import Identity


class TestLdict(TestCase):
    def test_exceps(self):
        p = UT40_4.p
        i64 = Identity(UT64_4)
        with pytest.raises(CellValueTooHigh):
            Hosh([0, 0, p + 1, 0, 0, 0])
        with pytest.raises(DanglingEtype):
            Hosh([0, 0, p + 1, 0, 0, 0], "dang")
        with pytest.raises(WrongContent):
            Hosh(124124)
        with pytest.raises(ElementTooHigh):
            Hosh.fromn(2 ** 241)
        with pytest.raises(WrongVersion):
            ø.convert(i64)
        with pytest.raises(WrongVersion):
            Hosh(b"1234").convert(i64)
        with pytest.raises(WrongOperands):
            Hosh(b"1234").convert({})
        with pytest.raises(WrongIdentifier):
            Hosh.fromid("a")

    def test_magic(self):
        h = Hosh(b"123")
        self.assertEqual(hash(h), h.n % sys.maxsize)

        a = ø * [6, 5, 4, 3, 2, 1]
        b = ø * [9, 8, 7, 6, 5, 4]
        self.assertEqual([15, 13, 11, 9, 7, 5], (a + b).cells)
        self.assertEqual(repr(a * b / b), repr(a))

        self.assertEqual([6, 8, 7, 9, 5, 4], (+b).cells)
        self.assertEqual([9, 6, 7, 8, 5, 4], (-b).cells)
        c = ø * [0, 0, 7, 6, 5, 4]
        d = ø * [0, 0, 3, 2, 5, 8]
        e = ø * [0, 0, 8, 3, 4, 7]
        self.assertEqual(-+c, +c)
        self.assertEqual(+-c, -c)

        self.assertEqual(c * d, d * c)
        self.assertEqual([0, 0, 10, 8, 10, 42], d ** c)
        self.assertNotEqual(c ** d, d ** c)
        self.assertEqual(c, c ** d // d)

