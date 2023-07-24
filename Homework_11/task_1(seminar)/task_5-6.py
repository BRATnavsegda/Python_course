# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длину и ширину.
# При вычитании не допускайте отрицательных значений.

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    """Класс прямоугольник, принимающий длину и ширину при создании экземпляра"""

    def __init__(self, length, width=None):
        """Добавляем параметры длина и ширина"""
        self.length = length
        self.width = width
        if width is None:
            self.width = length

    def perimeter(self):
        """Метод вычисляющий периметр"""
        return 2 * (self.width + self.length)

    def area(self):
        """Метод вычисляющий площадь"""
        return self.width * self.length

    def __str__(self):
        """Метод представления для пользователя"""
        return f"{self.length = } \n {self.width = }"

    def __add__(self, other):
        """Метод сложения двух экземпляров класса"""
        new_length = self.length + other.length
        return Rectangle(new_length, (self.perimeter() + other.perimeter()) / 2 - new_length)

    def __sub__(self, other):
        """Метод вычитания двух экземпляров класса"""
        new_length = self.length - other.length
        if new_length < 0:
            return "Отрицательное значение"
        return Rectangle(new_length, (self.perimeter() - other.perimeter()) / 2 - new_length)

    def __eq__(self, other):
        """Сравнение == двух экземпляров класса по площади"""
        return self.area() == other.area()

    def __lt__(self, other):
        """Сравнение < двух экземпляров класса по площади"""
        return self.area() < other.area()

    def __le__(self, other):
        """Сравнение >= двух экземпляров класса по площади"""
        return self.area() >= other.area()


r1 = Rectangle(8, 10)
print(r1)
r2 = Rectangle(10, 8)
print(r2)
r3 = r1 - r2
print(r1 == r2)
