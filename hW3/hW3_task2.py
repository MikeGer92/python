def one_string(*args):
    print(args)
    print(f'{f_name} {s_name}, {age} г.р., живет в городе {city}, эл.почта: {email}, телефон: {phone}')


while True:
    f_name = input('Введите Ваше имя: _')
    s_name = input('Введите Вашу фамилию: _')
    age = input('Введите год Вашего рождения: _')
    city = input('Введите город, где Вы живете: _')
    email = input('Введите адрес Вашей электронной почты: _')
    phone = input('Введите Ваш номер телефона: _')
    try:
        age = int(age)
        phone = int(phone)
        if not'@' and '.' in email:
            print('Вы ошиблись при вводе адреса электронной почты. Попробуйте снова!')
        else:
            break
    except ValueError:
        print('Вы ошиблись при вводе, попробуйте снова!')


one_string(f_name, s_name, age, city, email, phone)


def one_string2(**kwargs):
    print(kwargs.values())
    print(f'{f_name} {s_name}, {age} г.р., живет в городе {city}, эл.почта: {email}, телефон: {phone}')


one_string2(name=f_name, fam=s_name, a=age, c=city, e=email, p=phone)
