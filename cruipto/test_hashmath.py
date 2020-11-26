#  Copyright (c) 2020. Davi Pereira dos Santos
#  This file is part of the cruipto project.
#  Please respect the license - more about this in the section (*) below.
#
#  cruipto is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  cruipto is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with cruipto.  If not, see <http://www.gnu.org/licenses/>.
#
#  (*) Removing authorship by any means, e.g. by distribution of derived
#  works or verbatim, obfuscated, compiled or rewritten versions of any
#  part of this work is a crime and is unethical regarding the effort and
#  time spent here.
#  Relevant employers or funding agencies will be notified accordingly.
#

from unittest import TestCase

from cruipto.hashmath import bytes2cycledbm, bm2int


class Test(TestCase):
    def test_bytes2cycledbmat(self):
        # test with a bad matrix, after 8 rotations, it repeats itself; at the end of cycling, it becomes identity
        byts = int.to_bytes(170808403787765189503184116671632670848, byteorder="big", length=16)
        self.assertEqual(0, bm2int(bytes2cycledbm(byts)))
