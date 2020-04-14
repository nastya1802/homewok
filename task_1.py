import time

class TrafficLight:
    color = ['Red', 'Yellow', 'Green']

    def running (self):
        color = ['Red', ' Yellow', 'Green']
        i = 0
        while i < 3 :
            if i == 0:
                print(f'Сигнал светофора: {color[i]}')
                time.sleep (7)
                i += 1
            elif i == 1:
                print(f'Сигнал светофора: {color[i]}')
                time.sleep (5)
                i += 1
            elif i == 2:
                print(f'Сигнал светофора: {color[i]}')
                time.sleep (7)
                i -= 2

a = TrafficLight()
a.running()
