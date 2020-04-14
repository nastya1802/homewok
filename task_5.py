class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color

    def draw(self):
        print(f'Запуск отрисовки ручкой. Цвет {self.color}')

class Pensil(Stationery):
    def __init__(self, title, font):
        super().__init__(title)
        self.font = font
    def draw(self):
        print(f'Запуск отрисовки карандашом. Шрифт выбран {self.font}')

class Handle(Stationery):
    def __init__(self, title, color):
        super().__init__(title)
        self.color = color
    def draw(self):
        print(f'Запуск отрисовки маркером. Цвет {self.color}')


Pen = Pen('Ручка', 'Синий')
print(Pen.title)
Pen.draw()

Pensil = Pensil('Карандаш', 'Arial')
print(Pensil.title)
Pensil.draw()

Handle = Handle('Маркер', 'Красный')
print(Handle.title)
Handle.draw()
