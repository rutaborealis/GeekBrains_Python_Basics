# Lesson 7
# Task 1
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for row in self.matrix:
            result = result + ' '.join([str(i) for i in row]) + '\n'
        return result

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            for i in self.matrix:
                for j in other.matrix:
                    if len(i) != len(j):
                        print('\033[31mMatrices must be one-dimensional!\033[30m')
                        raise ValueError
            result = Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])
            return result
        else:
            print('\033[31mMatrices must be one-dimensional!\033[30m')
            raise ValueError


matrix1 = Matrix([[-121, 50, 108, -1000, 5], [300, -700, 950, -12321, 0], [1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]])
matrix2 = Matrix([[121, -50, -108, 1000, -5], [-300, 700, -950, 12321, 0], [-1, -2, -3, -4, -5], [1, 2, 3, 4, 5]])
matrix3 = Matrix([[121, -50, -108, 1000, 5], [-300, 700, -950, 12321, 0], [-1, -2, -3, -4, -5]])
matrix4 = Matrix([[121, -50, -108, 1000, -5], [-300, 700, -950, 12321, 0], [-1, -2, -3, -4, -5], [1, 2, 3, 4, 5, 6]])
print(matrix1)
print(f'{matrix1 + matrix2}')
# print(f'{matrix1 + matrix3}')
# print(f'{matrix1 + matrix4}')