test_list = []
a = input('Введите любое слово из латинских букв: _')


def int_fun(var):
    a_list = list(a.lower())
    l_a = len(a_list)
    for el in a_list:
        if 97 <= ord(el) <= 122:
            test_list.append(el)
    if len(test_list) == l_a:
        print(a.title())
    else:
        print('Вы ошиблись при вводе. Слово содержит не латинские буквы или цифры!')


int_fun(a)
