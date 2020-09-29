start_dist2 = input('Введите дистанцию начала тренировок: _')
a2 = float(start_dist)
wish_dist = input('Введите желаемую дистанцию для тренировок: _')
b2 = float(wish_dist)
days2 = 1
while b2 > a2:
    a2 = a2 + (a2 / 10)
    days2 = days2 + 1
print(f'Вам понадобится не менее {days2} дней тренировок!')
