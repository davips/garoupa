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
