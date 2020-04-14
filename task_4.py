class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go (self):
        print (f'Машина поехала')
    def stop (self):
        print(f'Машина остановилась')
    def turn_right (self):
        print(f'Машина повернула направо')
    def show_speed (self):
        print (f'Машина движется со скоростью {self.speed} км/ч')

class TownCar (Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
    def show_speed (self):
        if self.speed > 60:
            print("пожалуйста снизьте скорость. Допустимое значение менее 60 км/ч")
        else:
            print('Скорость движения не нарушена')

class SportCar (Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class WorkCar (Car):
     def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
     def show_speed (self):
        if self.speed > 40:
            print("пожалуйста снизьте скорость. Допустимое значение менее 40 км/ч")
        else:
            print('Скорость движения не нарушена')

class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)


Town = TownCar ("Hyinday", 70, "green", False)
print (f'Автомобиль марки {Town.name}. Цвет {Town.color}. Скорость передвижения составлет {Town.speed} км/ч')
print(f'Is it police car? {Town.is_police}')
Town.show_speed()
Town.go()
Town.stop()
Town.turn_right()



Sport = SportCar ('Ferrari', 120, 'red', False)
print (f'Автомобиль марки {Sport.name}. Цвет {Sport.color}. Скорость передвижения составлет {Sport.speed} км/ч')
print(f'Is it police car? {Sport.is_police}')
Sport.go()
Sport.stop()
Sport.turn_right()



Work = WorkCar ('Gazel', 70, 'grey', False)
print (f'Автомобиль марки {Work.name}. Цвет {Work.color}. Скорость передвижения составлет {Work.speed} км/ч')
print(f'Is it police car? {Work.is_police}')
Work.show_speed()
Work.go()
Work.stop()
Work.turn_right()


Police = PoliceCar ('Ford', 60, 'blue', True)
print (f'Автомобиль марки {Police.name}. Цвет {Police.color}. Скорость передвижения составлет {Police.speed} км/ч')
print(f'Is it police car? {Police.is_police}')
Police.go()
Police.stop()
Police.turn_right()

