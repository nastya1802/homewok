class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position (Worker):
    def __init__data (self, name, surname, position, wage, bonus):
        super().__init__(self, name, surname, position, wage, bonus)

    def  get_full_name(self):
        return f'Полное имя сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        return f'Доход с учетом премии составляет {sum(self._income.values())} евро'

a = Position('Ivan', 'Goremikin', 'Director', 25000, 15000)
print (a.get_full_name())
print (a.position)
print (a.get_total_income())
