# 2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

side_a, side_b, side_c = int(input("Triangle side A:")), \
                         int(input("Triangle side B:")), \
                         int(input("Triangle side C:"))
message = None

if side_a > side_b + side_c \
        or side_b > side_a + side_c \
        or side_c > side_a + side_b \
        or side_a == side_b == side_c == 0:
    message = "\nthere is no such triangle"
else:
    if side_a != side_b != side_c:
        message = "\nthe versatile triangle"
    elif side_a == side_b == side_c:
        message = "\nequilateral triangle"
    else:
        message = "\nisosceles triangle"

print(message)
