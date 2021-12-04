# Lesson 7
# Task 3
class Cell:
    def __init__(self, cells_count=0, name=None):
        self.cells_count = cells_count
        self.name = name

    def __add__(self, other):
        if isinstance(other, Cell) and (self.cells_count > 0 and other.cells_count > 0):
            cell_add = Cell(self.cells_count + other.cells_count, 'cell_add')
            return f'Sum of {self.name} and {other.name}: {cell_add.cells_count}'
        else:
            print('\033[31mCells count cannot be negative!\033[30m')
            raise ValueError

    def __sub__(self, other):
        if isinstance(other, Cell) and (self.cells_count > 0 and other.cells_count > 0):
            if self.cells_count - other.cells_count > 0:
                cell_dif = Cell(self.cells_count - other.cells_count, 'cell_dif')
                return f'Dif of {self.name} and {other.name}: {cell_dif.cells_count}'
            else:
                cell_dif = Cell(other.cells_count - self.cells_count, 'cell_dif')
                return f'Dif of {other.name} and {self.name}: {cell_dif.cells_count}'
        else:
            print('\033[31mCells count cannot be negative!\033[30m')
            raise ValueError

    def __mul__(self, other):
        if isinstance(other, Cell) and (self.cells_count > 0 and other.cells_count > 0):
            cell_mul = Cell(self.cells_count * other.cells_count, 'cell_mul')
            return f'Mul of {self.name} and {other.name}: {cell_mul.cells_count}'
        else:
            print('\033[31mCells count cannot be negative!\033[30m')
            raise ValueError

    def __truediv__(self, other):
        if isinstance(other, Cell) and (self.cells_count > 0 and other.cells_count > 0):
            if self.cells_count > other.cells_count:
                cell_div = Cell(self.cells_count // other.cells_count, 'cell_div')
                return f'Div of {self.name} and {other.name}: {cell_div.cells_count}'
            else:
                cell_div = Cell(other.cells_count // self.cells_count, 'cell_div')
                return f'Div of {other.name} and {self.name}: {cell_div.cells_count}'
        else:
            print('\033[31mCells count cannot be negative!\033[30m')
            raise ValueError

    def make_order(self, cells_in_row):
        if self.cells_count > 0:
            rows = self.cells_count // cells_in_row
            rest = self.cells_count - (rows * cells_in_row)
            for _ in range(rows):
                print('\U0001F9EC' * cells_in_row)
            print('\U0001F9EC' * rest)
        else:
            print('\033[31mCells count cannot be negative!\033[30m')
            raise ValueError


cell1 = Cell(int(input('Enter cells count (natural number): ')), 'cell1')
cell2 = Cell(int(input('Enter cells count (natural number): ')), 'cell2')
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
cell1.make_order(int(input('Enter cells in row for print: ')))
