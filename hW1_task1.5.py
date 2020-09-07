revenue = int(input('Введите показатель выручки компании за год: _'))
cost = int(input('Укажите совокупный объем затрат компании за год: _'))
result = revenue - cost
if result < 0:
    print(f'Убыток Вашей компании за год составляет: {result} рублей')
else:
    print(f'Прибыль Вашей компании за год составила: {result} рублей')

if result > 0:
    rent = revenue / cost
    print(f'Рентабельность компании составляет: {rent * 100} процентов')
    workers = int(input('Введите количество сотрудников в Вашей компании: _'))
    rent_work = result / workers
    print(f'На каждого сотрудника в Вашей компании приходится {rent_work} рублей прибыли!')
