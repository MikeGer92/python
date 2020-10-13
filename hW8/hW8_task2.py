class OwnError(Exception):

    @staticmethod
    def check_num():
        while True:
            num = input('Введите число, которое необходимо разделить: _')
            num_2 = input("Введите положительное число: ")

            try:
                num = int(num)
                num_2 = int(num_2)
                if num < 0 or num_2 < 0:
                    raise OwnError("Вы ввели отрицательное число!")
                elif num_2 == 0:
                    raise OwnError('Деление на ноль недопустимо!')
            except ValueError:
                print("Вы ввели не число")
            except OwnError as err:
                print(err)
            else:
                print(f"Все хорошо. Ваш результат: {num / num_2}")
                break


OwnError.check_num()
res = OwnError()
res.check_num()
