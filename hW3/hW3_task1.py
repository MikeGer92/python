def div(var1, var2):
    (quo) = var1 / var2
    print(quo)


while True:
    num1 = input('Введите первое любое число: _')
    num2 = input('Введите второе любое число, кроме 0: _')
    try:
        num1 = int(num1)
        num2 = int(num2)
        div(num1, num2)
        break
    except (ValueError, ZeroDivisionError):
        print('Вы ошиблись при вводе числа, попробуйте снова: _')
