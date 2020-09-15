

def sqr(x, y):
    result = x ** y
    print(f'{x} в степени {y} равно {result}')


while True:
    a = input('Для возведения числа в степень, введите число: _')
    b = input('Введите степень для числа: _')
    try:
        a = int(a)
        b = int(b)
        break
    except ValueError:
        print('Вы ошиблись при вводе, попробуйте снова:')


sqr(a, b)


def sqr2(var1, var2):
    i = 1
    num = var1
    while i < abs(var2):
        num = num * var1
        i += 1
    if var2 < 0:
        num = 1 / num
    print(num)


sqr2(a, b)
