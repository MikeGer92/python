my_dic = [
 (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
 (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
 (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

n = len(my_dic)

list_char = list(my_dic[1][1])
llc = len(list_char)
list_mame = []
list_price = []
list_count = []
list_unit = []

# for i in range(0, llc-1):
for a in range(0, n):
    list_mame.append(my_dic[a][1].get(list_char[0]))
for p in range(0, n):
    list_price.append(my_dic[p][1].get(list_char[1]))
for c in range(0, n):
    list_count.append(my_dic[c][1].get(list_char[2]))
for u in range(0, n):
    list_unit.append(my_dic[u][1].get(list_char[3]))

full_list = [list_mame, list_price, list_count, list_unit]
new_dic = {}
for w in list_char:
    i = 0
    key = w
    val = full_list[list_char.index(w)]
    new_dic.update({key: val})

print(new_dic['название'])
