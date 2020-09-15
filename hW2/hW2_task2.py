my_list = []
my_list_len = int(input('Введите количество элементов в списке(число больше 0): _ '))
while my_list_len <= 0:
    my_list_len = int(input('Введите количество элементов в списке(число больше 0): _ '))
for i in range(1, my_list_len + 1):
    el = input(f'Введите значение элемента {i} нового списка: _')
    my_list.append(el)
print(my_list)
pos = 0
for i in range(pos, len(my_list)):
    if i % 2 == 0:
        if pos < len(my_list) - 1:
            my_list.insert(i, my_list[pos + 1])
            pos = i + 2
            my_list.pop(pos)
print(my_list)
