class OwnError(Exception):
    new_list = []

    def __init__(self):
        self.new_list = []

    def get_num(self):
        while True:
            val = input('Введите любое количество чисел, для выхода нажмите q: _')
            if val == 'q' or val == 'Q':
                break
            else:
                try:
                    val = int(val)
                except ValueError:
                    print('Вы ввели не число!')
                else:
                    self.new_list.append(val)
        return self.new_list


num_list = OwnError()
print(num_list.get_num())
