val_list = []


def get_num():
    while True:
        val = input('Введите любое количество чисел через пробел, для выхода нажмите q: _')
        if val == 'q' or val == 'Q':
            break
        else:
            new_result = 0
            num_list = ''.join(val.split(' '))
            lnl = len(num_list)
            for num in num_list:
                num = int(num)
                val_list.append(num)
                new_result = sum(val_list[-lnl:])
            result = sum(val_list)
            print(f'({new_result})({result})')


get_num()
