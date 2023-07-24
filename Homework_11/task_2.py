# Создайте класс Матрица.
# Добавьте методы для: вывода на печать, проверку на равенство, сложения, *умножения матриц
import numpy as np


class Matrix:
    """Класс Матрица, для работы с матрицами"""

    def __init__(self, value: [[]]):
        """Добавляем параметр значение"""
        self.value = value

    def __str__(self):
        """Строковое представление матрицы"""
        result = "The matrix is:\n"
        for row in self.value:
            result = result + str(row) + '\n'
        return result

    def __eq__(self, other):
        """Сравнение двух матриц"""
        for row_1, row_2 in zip(self.value, other.value):
            if row_1 != row_2:
                return False
        return True

    def __add__(self, other):
        """Сложение двух матриц"""
        if len(self.value) == len(other.value):
            result = []
            for row_1, row_2 in zip(self.value, other.value):
                if len(row_1) == len(row_2):
                    row = []
                    for i, j in zip(row_1, row_2):
                        row.append(i + j)
                    result.append(row)
                else:
                    return None
            return Matrix(result)
        else:
            return None

    def __mul__(self, other):
        """Произведение двух матриц"""
        if len(self.value[0]) == len(other.value):
            #  в одну строку
            # return Matrix([[sum(self.value[i][k] * other.value[k][j] for k in range(len(self.value[0])))
            #                 for j in range(len(other.value[0]))] for i in range(len(self.value))])

            result = [[0 for row in range(len(other.value[0]))] for col in
                      range(len(self.value))]

            for i in range(len(self.value)):
                for j in range(len(other.value[0])):
                    for k in range(len(self.value[0])):

                        result[i][j] += self.value[i][k] * other.value[k][j]

            return Matrix(result)

        else:
            return None


if __name__ == "__main__":
    m1 = Matrix([[1, 2], [4, 5], [7, 8]])
    m2 = Matrix([[9, 8, 7], [6, 5, 4]])
    print(m1 * m2)

    mat1 = np.array([[1, 2], [4, 5], [7, 8]])
    mat2 = np.array([[9, 8, 7], [6, 5, 4]])
    mat3 = mat1.dot(mat2)
    print(mat3)
    help(Matrix)



