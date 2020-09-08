a = 25
print(type(a))

name = input('Добрый день! Как Вас зовут? _')
print(type(name))
print(f'Очень приятно, {name}! А я питон Гоша!')
age = int(input(f'{name}, а сколько Вам лет?_'))
age_python = 29
if age > age_python:
    print('Круто! А мне всего 29.')
elif age < age_python:
    print('Круто! А мне уже 29.')
else:
    print('Обалдеть! Мы же с Вами ровестники!')

print(bool(age > age_python))

if age > age_python:
    compare_age = ("%.2f" % (age/age_python))
    print(f'{name}, Вы в {compare_age} раза старше меня.')
else:
    compare_age = ("%.2f" % (age_python/age))
    print(f'{name}, Вы в {compare_age} моложе меня.')

print(type(compare_age))
