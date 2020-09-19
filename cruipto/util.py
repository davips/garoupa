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
