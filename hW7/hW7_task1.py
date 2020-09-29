class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join([str(num) for num in el]) for el in self.matrix])

    def __add__(self, other):
        result = []
        new_matrix = []
        for i in range(len(self.matrix)):
            for num in range(len(self.matrix[0])):
                summa = self.matrix[i][num] + other.matrix[i][num]
                new_matrix.append(summa)
                if len(new_matrix) == len(self.matrix):
                    result.append(new_matrix)
                    new_matrix = []
        return '\n'.join([' '.join([str(num) for num in el]) for el in result])


matrix_1 = Matrix([[3, 4], [5, 6]])
matrix_2 = Matrix([[9, 10], [11, 12]])
print(matrix_1 + matrix_2)
