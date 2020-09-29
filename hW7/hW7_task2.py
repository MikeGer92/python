from abc import ABC, abstractmethod


class Closes(ABC):

    mater = 0
    par_cl = 0

    def __init__(self, par_cl):
        self.mater = float(self.mater)
        self.par_cl = par_cl

    def __add__(self, other):
        self.mater = self.mater + other.mater
        return self.mater


    @abstractmethod
    def mater_count(self, par_cl):
        return self.mater


class Coat(Closes):

    def mater_count(self, v):

        self.mater = float((float(v) / 3) + 0.5)
        return self.mater


class Suit(Closes):

    def mater_count(self, h):
        self.mater = (h * 2 + 0.3)
        return self.mater


c = Coat(42)
s = Suit(1.5)
print(c.mater_count(42))
print(s.mater_count(1.5))
print(c + s)










