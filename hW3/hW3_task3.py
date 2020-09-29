num_list = []


def mul_max(*args):
    for num in num_list:
        while len(num_list) > 2:
            num_list.pop(num_list.index(min(num_list)))
    result = num_list[0] * num_list[1]
    print(f' Произведение двух максимальных чисел списка = {result}')


l_num_list = int(input('Введите желаемую длинну списка чисел: _'))
for i in range(1, l_num_list + 1):
    while True:
        num = input(f'Введите число под номером {i}: _')
        try:
            num = int(num)
            num_list.append(num)
            break
        except ValueError:
            print('Вы ошиблись при вводе числа, попробуйте снова: _')


mul_max(num_list)
