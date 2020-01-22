from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, matrix):
        self.matrix = [row.copy() for row in matrix]

    def __str__(self):
        return '\n'.join(
            ['\t'.join([str(i) for i in row]) for row in self.matrix]
        )

    def size(self):
        """
        :return: (rows, cols)
        """
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        s_rows = self.size()[0]
        s_cols = self.size()[1]
        if not isinstance(other, Matrix) or \
                s_rows != other.size()[0] or \
                s_cols != other.size()[1]:
            raise MatrixError(self, other)

        res_sum = []
        for i in range(s_rows):
            res_sum.append(
                [x + y for x, y in zip(
                    self.matrix[i],
                    other.matrix[i]
                )]
            )
        return Matrix(res_sum)

    @staticmethod
    def mul_matrices(self, matrix1, matrix2):
        cols1 = matrix1.size()[1]
        rows1 = matrix1.size()[0]
        cols2 = matrix2.size()[1]

        new_matrix = []
        for row1 in range(rows1):
            new_row = []
            for col2 in range(cols2):
                acc_sum = 0
                for col1 in range(cols1):
                    # FYI: row2 == col1
                    acc_sum += \
                        matrix1.matrix[row1][col1] * \
                        matrix2.matrix[col1][col2]
                new_row.append(acc_sum)

            new_matrix.append(new_row)

        return Matrix(new_matrix)

    def __mul__(self, num):
        if isinstance(num, Matrix):
            matrix1 = self
            matrix2 = num
            m1_size = matrix1.size()
            m2_size = matrix2.size()
            if m1_size[1] == m2_size[0]:
                return self.mul_matrices(self, matrix1, matrix2)
            else:
                raise MatrixError(matrix1, matrix2)
        elif isinstance(num, int) or isinstance(num, float):
            res = []
            for i in range(self.size()[0]):
                res.append([x * num for x in self.matrix[i]])
            return Matrix(res)
        else:
            raise MatrixError(self, num)

    __rmul__ = __mul__

    def transpose(self):
        self.matrix = [list(line) for line in zip(*self.matrix)]
        return self

    @staticmethod
    def transposed(matrix):
        # return Matrix(matrix.matrix).transpose()
        return Matrix([list(line) for line in zip(*matrix.matrix)])


class SquareMatrix(Matrix):
    def __pow__(self, n):
        if n < 0:
            raise MatrixError(self, n)
        if n == 1 or n == 0:
            return self

        if n % 2 == 0:
            return (self * self) ** (n // 2)
        else:
            return self * (self ** (n - 1))

    # use __pow__ for __mul__ results
    def __mul__(self, x):
        return SquareMatrix(super().__mul__(x).matrix)


exec(stdin.read())
