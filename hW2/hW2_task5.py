my_list = [7, 5, 3, 3, 2]
lml = len(my_list)
new_num = int(input('Введите любое число: _'))
print(my_list)
if new_num in my_list:
    f_pos = my_list.index(new_num)
    step = my_list.count(new_num)
    new_num_pos = f_pos + step
    my_list.insert(new_num_pos, float(new_num))
elif new_num > my_list[0]:
    my_list.insert(0, new_num)
elif new_num < my_list[lml - 1]:
    my_list.append(new_num)
elif my_list[0] > new_num > my_list[lml - 1]:
    for num in my_list:
        if new_num - num == 1:
            new_num_pos = my_list.index(num)
            my_list.insert(new_num_pos, new_num)
            break
print(my_list)
