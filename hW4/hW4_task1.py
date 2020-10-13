from sys import argv


script_name, work_time, tariff, result = argv


def gross(w, t):
    result = int(w) * int(t)
    return result


print('Имя скрипта: ', script_name)
print('Рабочее время: ', work_time)
print('Оплата в час: ', tariff)
gross(work_time, tariff)
print('Вознаграждение: ', gross(work_time, tariff))

