import time
from turtle import *


class TrafficLight:
    color = ''


    def __init__(self):
        __color = ''

    def running(self):

        self.color = '   '
        print(f'\033[30m\033[41m{self.color}', end='')
        time.sleep(7)
        print('\r', end='')
        self.color = '   '
        print(f'\033[30m\033[43m{self.color}', end='')
        time.sleep(2)
        print('\r', end='')
        self.color = '   '
        print(f'\033[30m\033[42m{self.color}', end='')
        time.sleep(10)
        print('\r', end='')
        self.color = '   '
        print(f'\033[30m\033[43m{self.color}', end='')
        time.sleep(2)
        print('\r', end='')
        self.color = '   '
        print(f'\033[30m\033[41m{self.color}', end='')


t_l_1 = TrafficLight()
t_l_1.running()