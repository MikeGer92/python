new_dic = {}
sub_list = []
new_list = []
fin_dic = {}
bad_list = ['(', ')', 'л', 'п', 'р', 'а', 'б', '-']
task6 = open('text_6.txt', 'r+', encoding='utf-8')
sub_string = task6.read()
sub_string = ''.join(i for i in sub_string if not i in bad_list)
sub_list = list(sub_string.splitlines())
for i in range(0, len(sub_list)):
    new_list.append(sub_list[i].split(':'))
for i in range(0, len(new_list)):
    new_list[i][1] = new_list[i][1].split()
for i in range(0, len(new_list)):
    key = new_list[i][0]
    val = new_list[i][1]
    new_dic[key] = val

print(new_dic)










# gen_sub_list = [sub_list[i].split(' ') for i in range(0, l_sl)]







