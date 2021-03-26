from abc import abstractmethod, ABC


class Element(ABC):
    i: int

    def __init__(self):
        self.sym = self.__class__.__name__.lower()

    @abstractmethod
    def __mul__(self, other):
        pass

    def __repr__(self):
        return f"{self.sym}{self.i}"

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(repr(self))
