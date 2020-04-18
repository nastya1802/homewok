class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def consumption1 (self):
        return (self.size/6.5 + 0.5)

    def consumption2 (self):
        return (2*self.height +0.3)

    @ property
    def total (self):
        print (f'Общий расход ткани составляет: {(2*self.height +0.3) + (2*self.height +0.3)}')

class Coat (Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.consumption1 = self.size/6.5 + 0.5
    def __str__(self):
        return f'Расход ткани на пальто составляет: {self.consumption1}'

class Suit (Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.consumption2 = 2*self.height +0.3
    def __str__(self):
        return f'Расход ткани на костюм составляет: {self.consumption2}'


coat = Coat (1, 2)
suit = Suit (2, 3)
print (coat)
print (suit)
print (coat.total)
print (suit.total)