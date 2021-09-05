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
#  part of this work is illegal and unethical regarding the effort and
#  time spent here.
from collections import namedtuple

Group = namedtuple("Group", "p p4 p6 digits bytes last")
"""Group properties"""

groups = {
    16: Group(65521, 18429861372428076481, 79119421429263970001791209121, 16, 12, "Y._0d5c34bc54504"),
    32: Group(4294967291, 340282365336375215945099464469838299761,
              6277101691541631771514589274378639120656724268335671295241, 32, 24, ".._67200000b0efffff59000000cefff"),
    40: Group(1099511627689, 1461501636868331575725436266114840805196834679841,
              1766847063939562670646036165286872353986524172769430561878277294118845361, 40, 30,
              ".._87c2a630003eec7dffff561b0000004aeffff"),
    64: Group(18446744073709551557, 115792089237316193942174975457431254695161196299352022581048345476735855814001,
              39402006196394478456139629384141450683325994812909116356652328479007639701989040511471346632255226219324457074810249,
              64, 48, ".._ca5e8b00000000003f673fffffffffff591500000000000041fffffffffff")
}
UT16_4, UT32_4, UT40_4, UT64_4 = groups.values()
