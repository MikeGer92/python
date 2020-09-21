lines = 0
words = 0
num_letters = 0
f = open('task2.txt', 'r')
for line in f:
    line = line.split(' ')
    words = len(line)
    lines += 1
    print(f'В строке {lines} {words} слов')
for i in range(1, lines):
    words = len(line)
print(f'В этом файле {lines} строк')
f.close()
