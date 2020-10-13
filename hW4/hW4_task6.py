from itertools import count, cycle

my_list = []


for num  in count(10, 10):
    if num <= 100:
        my_list.append(num)
    else:
        break
print(my_list)
i = 1
for num in cycle(my_list):
    if i < 15:
        print(num)
        i += 1
    else:
        break





