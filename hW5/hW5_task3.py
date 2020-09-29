name_list = open('text_3.txt', 'r', encoding='utf-8')
new_name_list = name_list.read().splitlines()
min_salary = 20000.0
l_nnl = len(new_name_list)
gen_list = [(new_name_list[i]).split(' ') for i in range(0, l_nnl)]
fin_gen_list = [gen_list[i] for i in range(0, len(gen_list)) if float(gen_list[i][-1]) < min_salary]
print()
for i in range(0, len(fin_gen_list)):
    print(fin_gen_list[i][0])
print(f'Эти сотрудники получают менее {min_salary} рублей')

salary_gen = [float(gen_list[i][-1]) for i in range(0, len(gen_list))]
print(f'Средняя зарплата сотрудника составляет {sum(salary_gen)/ len(gen_list)} рублей')

