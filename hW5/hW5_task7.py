new_list = []
fin_list = []
firm_dic = {}
av_dic = {}
profit_list = []
with open('text_7.txt', 'r+', encoding='utf-8') as task7:
    firm_list = task7.read().splitlines()
    for el in firm_list:
        new_list.append(el.split(' '))
    for i in range(0, len(new_list)):
        new_list[i][2] = int(new_list[i][2])
        new_list[i][3] = int(new_list[i][3])
    for i in range(0, len(new_list)):
        key = new_list[i][0]
        val = (new_list[i][2] - new_list[i][3])
        firm_dic[key] = val
        if val > 0:
            profit_list.append(val)
    fin_list.append(firm_dic)
    avange = sum(profit_list) / len(profit_list)
    av_dic['avarange_profit'] = avange
    fin_list.append(av_dic)

print(fin_list)

j


