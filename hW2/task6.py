fin_dic = []
hW2_dic = [{}]
dic = {}
char_list = ['название', 'цена', 'количество', 'ед.изм']
lcl = len(char_list)
d_count = int(input('Введите количество товаров в списке: _'))
for num in range(1, d_count+1):
    name = input(f'Введите название товара {num}:_')
    dic[char_list[0]] = name
    price = int(input(f'Введите цену товара {num}:_'))
    dic[char_list[1]] = price
    unit_count = int(input(f'Введите остаток товара {num} на складе:_'))
    dic[char_list[2]] = unit_count
    unit = input(f'Введите единицу измерения товара {num}:_')
    dic[char_list[3]] = unit
    hW2_dic.append(dic)

fin_dic.append(dic)
print(fin_dic)
