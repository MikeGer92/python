import time




class TrafficLight:
    __color = 'red'

    def running(self):
        print('Красный свет! Дороги нет!', end='')
        time.sleep(7)
        print('\r', end='')
        print('Желтый. Приготовиться!', end='')
        time.sleep(2)
        print('\r', end='')
        print('Зеленый свет. Вперед!', end='')
        time.sleep(15)
        print('\r', end='')
        print('Красный свет! Дороги нет!', end='')

TrafficLight.running(TrafficLight)
