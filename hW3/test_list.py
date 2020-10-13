test_list = []


def int_fun(var):
    l_w = len(word)
    for el in word:
        if 97 <= ord(el) <= 122:
            test_list.append(el)
    if len(test_list) == l_w:
        print(word.title())
    else:
        print('Вы ошиблись при вводе. Слово содержит не латинские буквы или цифры!')
a = input('Введите любое слово из латинских букв: _')
word_list = a.lower()
word_list = word_list.split(' ')
lwl = len(word_list)

i = 0
while i <= lwl:
    for i in range(0, lwl):
        word = word_list[i]
        int_fun(word)
        i += 1
    break




