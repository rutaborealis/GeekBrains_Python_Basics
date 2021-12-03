# Lesson 7
# Task 2
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __add__(self, other):
        if isinstance(self, Coat):
            result = ((self.v / 6.5) + 0.5) + ((other.h * 2) + 0.3)
            return result
        else:
            result = ((self.h * 2) + 0.3) + ((other.v / 6.5) + 0.5)
            return result

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def tissue_consumption(self):
        result = (self.v / 6.5) + 0.5
        return result


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def tissue_consumption(self):
        result = (self.h * 2) + 0.3
        return result


coat = Coat(float(input('Enter V for coat: ')))
suit = Suit(float(input('Enter H for suit: ')))

print(f'Tissue for coat {coat.v:.2f}: {coat.tissue_consumption:.2f} m.')
print(f'Tissue for suit {suit.h:.2f}: {suit.tissue_consumption:.2f} m.')
print(f'Total tissue consumption for coat and suit: {coat + suit:.2f} m.')
