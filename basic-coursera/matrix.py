from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)
        self.lines = len(self.matrix)
        self.rows = len(self.matrix[0])

    def __str__(self):
        return '\n'.join(
            ['\t'.join([str(i) for i in row]) for row in self.matrix]
        )

    def size(self):
        return self.lines, self.rows

    def __add__(self, other):
        if not isinstance(other, Matrix) or\
                self.lines != other.size()[0] or\
                self.rows != other.size()[1]:
            raise MatrixError(self, other)

        res_sum = []
        for i in range(self.lines):
            res_sum.append(
                [x + y for x, y in zip(self.matrix[i], other.matrix[i])]
            )
        return Matrix(res_sum)

    def __mul__(self, num):
        res = []
        if isinstance(num, int) or isinstance(num, float):
            for i in range(self.lines):
                res.append([x * num for x in self.matrix[i]])
        else:
            raise MatrixError(self, num)
        return Matrix(res)

    __rmul__ = __mul__

    def transpose(self):
        self.matrix = [list(line) for line in zip(*self.matrix)]
        return self

    @staticmethod
    def transposed(m):
        return Matrix([list(line) for line in zip(*m.matrix)])


exec(stdin.read())
