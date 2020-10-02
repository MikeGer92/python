class ComplNum:

    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'{self.num}'

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num


num_1 = ComplNum(1+2j)
num_2 = ComplNum(3+4j)
print(num_1)
print(num_2)
print(num_1 + num_2)
print(num_1 * num_2)
