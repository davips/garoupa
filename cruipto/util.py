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

# noinspection PyPep8Naming
class _meta(type):
    def __getattr__(self, item):
        return lambda x: x.__getattribute__(item)


# noinspection PyPep8Naming
class _(metaclass=_meta):
    """Shortcut for functional handling of iterables.

    _.m = apply map and convert to list (useful for easy printing while debugging)
    _ = item inside iterable (to provide as a function to map)
    Example:
        map(_[4], tuples)
        map(_('My class name applied for all new instances'), classes)
        _.m(_.id, users)

    ps. Mostly for development.
    """

    def __new__(cls, *args, **kwargs):
        return lambda x: x(*args, **kwargs)

    def __class_getitem__(cls, item):
        return lambda x: x[item]

    m = lambda x, y: list(map(x, y))


def flatten(lst):
    return [item for sublist in lst for item in sublist]
