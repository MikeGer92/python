my_str = input('Введите несколько слов, разделяя их пробелом: _')
new_str = my_str.split(' ')
n = 1
for i in new_str:
    if len(i) > 10:
        i = i[:10]
    print(f'{n}. {i}')
    n += 1


# c enumerate

my_str2 = input('Введите несколько слов, разделяя их пробелом: _')
print(my_str2)
my_str2 = my_str2.split(' ')
new_str2 = []
for word in my_str2:
    if len(word) > 10:
        word = word[:10]
        new_str2.append(word)
    else:
        new_str2.append(word)
for word in enumerate(new_str2, 1):
    print(word)