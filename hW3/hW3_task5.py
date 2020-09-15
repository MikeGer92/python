val_list = []
new_list = []


def get_num():
    while True:
        val = input('Введите любое количество чисел от 1 до 9 через пробел, для выхода нажмите q: _')
        if val == 'q' or val == 'Q':
            break
        else:
            new_result = 0
            num_list = ''.join(val.split(' '))
            lnl = len(num_list)
            if 'q' in num_list:
                for num in num_list[:num_list.index('q')]:
                    num = int(num)
                    new_list.append(num)
                new_result = sum(new_list)
                result = sum(val_list)+new_result
                print(f'({new_result})({result})')
                break
            else:
                for num in num_list:
                    num = int(num)
                    val_list.append(num)
                    new_result = sum(val_list[-lnl:])
                result = sum(val_list)
            print(f'({new_result})({result})')


get_num()
