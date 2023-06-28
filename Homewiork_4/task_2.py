# Напишите функцию для транспонирования матрицы.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(f"\nInitial matrix: \n{matrix}")


def transposition_matrix(matx: list[list]) -> list[list]:
    new_matx = []

    for i in matx:
        for j in i:
            if len(new_matx) != len(matx[0]):
                new_matx.append([j])
            else:
                new_matx[i.index(j)].append(j)
    return new_matx


print(f"\nTransposed matrix: \n{transposition_matrix(matrix)}")
