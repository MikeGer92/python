from functools import reduce

my_list = []


def fact1(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i += 1
        yield f


for n in fact1(5):
    print(n)


def fact2(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
        yield f


for n in fact2(6):
    print(n)


def fact3(n):
    for num in range(1, n + 1):
        my_list.append(num)
    f = reduce(lambda a, b: a * b, my_list)
    yield f


for n in fact3(4):
    print(n)
