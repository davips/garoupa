#  Copyright (c) 2021. Gabriel Dalforno and Davi Pereira-Santos
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


def ncclasses(n, p):
    """Number of conjugacy classes

    Usage:

    >>> for n in range(3, 5):
    ...     print(ncclasses(n, 2**32-5))
    18446744035054845971
    158456324493573097642216390441
    """
    if n == 3:
        return p ** 2 + p - 1
    elif n == 4:
        return 2 * (p ** 3) + p ** 2 - 2 * p
    # elif n == 5:
    #     return 5 * (p ** 4) - 5 * (p ** 2) + 1
    # elif n == 6:
    #     return -1 + 4 * p + 5 * (p ** 2) - 15 * (p ** 3) - 5 * (p ** 4) + 12 * (p ** 5) + p ** 6
    # elif n == 7:
    #     return 7 * p + 7 * (p ** 2) + 35 * (p ** 3) - 35 * (p ** 4) - 35 * (p ** 5) \
    #            + 28 * (p ** 6) + 8 * (p ** 7)
    # elif n == 8:
    #     return 2 + 4 * p - 32 * (p ** 2) - 28 * (p ** 3) + 161 * (p ** 4) - 28 * (p ** 5) \
    #            - 168 * (p ** 6) + 48 * (p ** 7) + 38 * (p ** 8) + 4 * (p ** 9)
    # elif n == 9:
    #     q = p - 1
    #     return 1 + 36 * q + 462 * (q ** 2) + 2772 * (q ** 3) + 8715 * (q ** 4) \
    #            + 15372 * (q ** 5) + 15862 * (q ** 6) + 9720 * (q ** 7) + 3489 * (q ** 8) \
    #            + 701 * (q ** 9) + 72 * (q ** 10) + 3 * (q ** 11)
    # elif n == 10:
    #     q = p - 1
    #     return 1 + 45 * q + 750 * (q ** 2) + 6090 * (q ** 3) + 26985 * (q ** 4) \
    #            + 69825 * (q ** 5) + 110530 * (q ** 6) + 110280 * (q ** 7) + 70320 * (q ** 8) \
    #            + 28640 * (q ** 9) + 7362 * (q ** 10) + 1170 * (q ** 11) + 110 * (q ** 12) \
    #            + 5 * (q ** 13)
    # elif n == 11:
    #     q = p - 1
    #     return 1 + 55 * q + 1155 * (q ** 2) + 12210 * (q ** 3) + 72765 * (q ** 4) \
    #            + 261261 * (q ** 5) + 592207 * (q ** 6) + 877030 * (q ** 7) \
    #            + 868725 * (q ** 8) + 583550 * (q ** 9) + 267542 * (q ** 10) \
    #            + 83909 * (q ** 11) + 18007 * (q ** 12) + 2618 * (q ** 13) + 242 * (q ** 14) \
    #            + 11 * (q ** 15)
    # elif n == 12:
    #     q = p - 1
    #     return 1 + 66 * q + 1705 * (q ** 2) + 22770 * (q ** 3) + 176055 * (q ** 4) \
    #            + 841302 * (q ** 5) + 2600983 * (q ** 6) + 5387646 * (q ** 7) \
    #            + 7680310 * (q ** 8) + 7684820 * (q ** 9) + 5473050 * (q ** 10) \
    #            + 2803182 * (q ** 11) + 1042181 * (q ** 12) + 284109 * (q ** 13) \
    #            + 57256 * (q ** 14) + 8484 * (q ** 15) + 890 * (q ** 16) + 60 * (q ** 17) \
    #            + 2 * (q ** 18)
    # elif n == 13:
    #     q = p - 1
    #     return 1 + 78 * q + 2431 * (q ** 2) + 40040 * (q ** 3) + 390390 * (q ** 4) \
    #            + 2403258 * (q ** 5) + 9766471 * (q ** 6) + 27116232 * (q ** 7) \
    #            + 52873678 * (q ** 8) + 74012653 * (q ** 9) + 75670881 * (q ** 10) \
    #            + 57294120 * (q ** 11) + 32515314 * (q ** 12) + 14000495 * (q ** 13) \
    #            + 4635125 * (q ** 14) + 1195116 * (q ** 15) + 241436 * (q ** 16) \
    #            + 37778 * (q ** 17) + 4381 * (q ** 18) + 338 * (q ** 19) + 13 * (q ** 20)
    else:
        raise Exception("Only 3x3 ... 13x13 matrices have number of conjugacy classes implemented.")
