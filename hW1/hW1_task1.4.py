num = int(input('Введите число больше 0: _'))
last_fig = num % 10
new_num = num // 10
while new_num > 0:
    if new_num % 10 > last_fig:
        last_fig = new_num % 10
    new_num = new_num // 10
print(last_fig)
