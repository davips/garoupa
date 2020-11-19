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

import numpy


def int2bmat(n):
    m = numpy.eye(17)
    b = 127
    for i in range(3):
        for j in range(i + 1, 4):
            m[i, j] = n >> b & 1
            b -= 1
    for i in range(12):
        for j in range(max(5, i + 1), 17):
            m[i, j] = n >> b & 1
            b -= 1
    for i in range(13, 17):
        for j in range(max(12, i + 1), 17):
            m[i, j] = n >> b & 1
            b -= 1
    return m


def bmat2int(m):
    n = 0
    b = 127
    for i in range(3):
        for j in range(i + 1, 4):
            n += int(m[i, j]) << b
            b -= 1
    for i in range(12):
        for j in range(max(5, i + 1), 17):
            n += int(m[i, j]) << b
            b -= 1
    for i in range(13, 17):
        for j in range(max(12, i + 1), 17):
            n += int(m[i, j]) << b
            b -= 1
    return n


def bmatinv(m):
    return numpy.linalg.inv(m) % 2


def bmatmul(a, b):
    return (a @ b) % 2
