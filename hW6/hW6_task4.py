import time
from random import randint


class Car:

    name = ''
    color = ''
    speed = 0
    is_police = True

    def __init__(self, name, color,  is_police):
        self.name = name
        self.color = color
        self.is_police = False

    def go(self):
        print(f'\033[30m\033[42m {self.color} {self.name} speed {self.speed}')
        print('Go-go-go-go!!!!!!')

    def stop(self):
        print('STOP!!!')

    def turn(self):
        direction = ['left', 'right', 'back']
        d = (randint(0, len(direction)-1))
        print(direction[d])

    def show_speed(self):
        print(self)


class TownCar(Car):

    def go(self):
        print(f'\033[30m\033[42m {self.color} {self.name} speed {self.speed} Km/h')
        print('Go-go-go-go!!!!!!')
        TownCar('name', 'color', False).run_speed()

    def show_speed(self):
        print(self.speed)

    def run_speed(self):
        s = 0
        max_speed = 60
        while s < max_speed:
            print('Yes,Yes!Go!Go!')
            s += 5
            TownCar('name', 'color', False).show_speed()
            print(f' {s} Km/h')
            time.sleep(0.5)
            TownCar('name', 'color', False).turn()
        else:
            TownCar('name', 'color', False).stop()
            print(f'\033[30m\033[41m OVERSPEED')
            time.sleep(5)


class WorkCar(Car):

    def go(self):
        print(f'\033[30m\033[46m {self.color} {self.name} speed {self.speed} Km/h')
        print('Go-go-go-go!!!!!!')
        WorkCar('name', 'color', False).run_speed()

    def show_speed(self):
        print(WorkCar.speed)

    def run_speed(self):
        speed = 2
        max_speed = 40
        while speed < max_speed:
            print(f'\033[30m\033[43m Go!Go!')
            speed = int(speed * 1.5)
            print(f' {speed} Km/h')
            time.sleep(0.5)
            WorkCar('name', 'color', False).turn()
        else:
            WorkCar('name', 'color', False).stop()
            print(f'\033[30m\033[41m OVERSPEED')
            time.sleep(5)


auto_1 = TownCar
auto_1('HONDA', 'RED', False).go()
auto_2 = WorkCar
auto_2('Traktor', 'YELLOW', False).go()
