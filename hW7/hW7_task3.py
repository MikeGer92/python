class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        pass

    def __add__(self, other):
        self.cell = self.cell + other.cell
        return self.cell

    def __sub__(self, other):
        if self.cell < other.cell:
            self.cell = other.cell - self.cell
        return self.cell

    def __mul__(self, other):
        self.cell = self.cell * other.cell
        return self.cell

    def __floordiv__(self, other):
        if other.cell <= 0:
            return f'Ошибка при вводе значения Клетки!'
        else:
            self.cell = self.cell // other.cell
            return self.cell

    def make_oder(self, rows):
        if 0 < self.cell >= rows:
                num_rows = self.cell // rows
                el_cell = self.cell % rows
                for i in range(1, num_rows):
                    result = (f'{rows * "*" }\n' * num_rows)
                    return f'{result}\r{el_cell * "*"}'
        else:
            return f'Ошибка при вводе значения Клетки!'


cell_1 = Cell(15)
cell_2 = Cell(4)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_1.make_oder(4))
