#  Copyright (c) 2021. Gabriel Dalforno
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

import matplotlib.pyplot as plt
from symmetricdescr import orderS, PS, order_histS, orderSD, PSD, order_histSD
from wreathdescr import orderG, PG, order_histG
from math import log

# Sn versus SD versus G

N = 65
ND = [2, 3, 5, 7, 11, 13, 15, 17, 19, 23]
P = [2, 3, 5, 7, 11, 13, 17, 19]


print("Number of bits:")
print(f"Sn : {log(orderS(N), 2):.2f}")
print(f"SD : {log(orderSD(ND), 2):.2f}")
print(f"G : {log(orderG(P), 2):.2f}")
print()
print("Degree of commutation:")
print(f"Sn: {PS(N)}")
print(f"SD : {PSD(ND):.2f}")
print(f"G: {PG(P)}")
print()


hS = order_histS(N)
hSD = order_histSD(ND)
hG = order_histG(P)

xS = sorted(hS.keys())
xSD = sorted(hSD.keys())
xG = sorted(hG.keys())

yS = [log(hS[key]) for key in xS]
ySD = [log(hSD[key]) for key in xSD]
yG = [log(hG[key]) for key in xG]

xS = list(map(log, xS))
xSD = list(map(log, xSD))
xG = list(map(log, xG))

plt.title("Symmetric Group x Direct Product of Symmetric group x Proposed Group")
plt.plot(xG, yG, label="G")
plt.plot(xSD, ySD, label="DSn")
plt.plot(xS, yS, label="Sn")
plt.xlabel("Log(Order)")
plt.ylabel("Log(#Elements)")
plt.legend()
plt.show()
