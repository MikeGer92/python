from random import randrange, randint, random

my_list = [randrange(1, 100, randint(1, 5)) for i in range(20)]


new_list = [el for el in my_list if my_list.count(el) == 1]

print(my_list)
print(new_list)