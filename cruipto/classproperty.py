#  Copyright (c) 2020. Davi Pereira dos Santos
#      This file is part of the cruipto project.
#      Please respect the license. Removing authorship by any means
#      (by code make up or closing the sources) or ignoring property rights
#      is a crime and is unethical regarding the effort and time spent here.
#      Relevant employers or funding agencies will be notified accordingly.
#
#      cruipto is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      cruipto is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with cruipto.  If not, see <http://www.gnu.org/licenses/>.
#

class ClassProperty:
    def __init__(self, initializer):
        """
        Another way to create a class property, instead of the broken @classproperty decorator.

        Parameters
        ----------
        initializer
            A hidden function containing returning the desired value.
        """
        self.initializer = initializer

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if not hasattr(owner, "_" + self.name) or getattr(owner, "_" + self.name) is None:
            initializer = getattr(owner, self.initializer)
            initializer()

        return getattr(owner, "_" + self.name)
