num_list = []
new_list = []
result = 0
task5 = open('file_num.txt', 'a', encoding='utf-8')
input('Для выхода из программы нажмите "q" или Enter без ввода числа')
while True:
    num = input('Введите число: _ ')
    if num == "q" or num == '':
        break
    num_list.append(num)
    print(num_list)
print(num_list)
for num in num_list:
    new_list.append(int(float(num)))
    result = sum(new_list)
print(f'Списко введенных Вами чисел: {new_list}', file=task5)
print(f'Сумма введенных Вами чисел равна: {result}', file=task5)
print(f'Сумма введенных Вами чисел равна: {result}')
task5.close()
