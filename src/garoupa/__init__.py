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
"""GaROUPa solves the problem of determining the identity of multi-valued objects or sequences of events
(and provide extra modules for group theory)"""

from .config import setup
from .groups import *
from .hosh import Hosh as H
from .misc.helper import Helper
from .misc.identity import ø, Identity

__pdoc__ = {
    "hosh": False,
}

Hosh = H
"""All identifiers are instances of this class"""

ħ = Helper(UT40_4)
"""UTF-8 shortcut to create 40-digit Hosh objects (AltGr+H in most keyboards)

Other options are also available: ħ16, ħ32, ħ40, ħ64"""

identity = ø()
"""Shortcut to the 40-digit identity Hosh object"""

ø = identity
"""UTF-8 shortcut to the 40-digit identity Hosh object (AltGr+O in most keyboards)

Other options are also available: ø16, ø32, ø40, ø64"""

ħ16, ħ32, ħ40, ħ64 = [Helper(version) for version in groups.values()]
ø16, ø32, ø40, ø64 = [Identity(version) for version in groups.values()]


def rho_elem(index, asbin=False):
    """
    >>> rho_elem(1).id
    'L9.Vd4B6O6z0WdCgyk4mx1v118i91N.DkR7nS5Ua'
    >>> rho_elem(2).id
    'Od4uNccS.19C9PuEHnzB-VK0GKFajq5VJUJi1rCf'
    >>> rho_elem(2, asbin=True)
    b'<RESERVED ELEMENT: rho_2>'
    """
    r = f"<RESERVED ELEMENT: rho_{index}>".encode()
    return r if asbin else Hosh(r)


def removal_elem(field, asbin=False):
    """
    >>> removal_elem("_myfield").id
    'zZgRpxed-6aboKQ39.v5.HfBjr3j8WJlDwYVvUpi'
    >>> removal_elem("myfield").id
    'eE-IoUO1EiZkxKkRyrXJcgXHc0pTD2As7IODrxTc'
    >>> removal_elem("myfield", asbin=True)
    b'<RESERVED ELEMENT: DELETE VALUE AT FIELD myfield>'
    """
    r = f"<RESERVED ELEMENT: DELETE VALUE AT FIELD {field}>".encode()
    return r if asbin else Hosh(r)
