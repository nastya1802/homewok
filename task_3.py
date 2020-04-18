class Cell:
    def __init__(self):
        self.quantity = []

    def __add__(self, other):
        self.quantity.append(other)
    def __sub__(self, other):
        self.quantity.append(other)



cell = Cell ()
a = 5
b = 4

print (a+b)
print (a-b)
print (a*b)

