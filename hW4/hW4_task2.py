from random import randrange, randint, random

my_list = [randrange(1, 100, randint(1, 5)) for i in range(20)]
new_list = []
final_list = []
for el in my_list:
    if my_list.count(el) == 1:
        new_list.append(el)
for i in range(1, len(my_list)):
    if my_list[i] > my_list[i - 1]:
        final_list.append(my_list[i])


gen_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1] and my_list.count(my_list[i]) == 1]







print(my_list)
print(new_list)
print(final_list)
print(gen_list)


