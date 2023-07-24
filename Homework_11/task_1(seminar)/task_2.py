# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Класс Архив, который хранит число и строку.
    При создании нового экземпляра класса, данные из ранее созданных экземпляров, сохраняются в список кортежей"""

    _instance = None

    def __new__(cls, number, string):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.lst_arc = []
        else:
            cls._instance.lst_arc.append((cls._instance.number, cls._instance.string))
        return cls._instance

    def __init__(self, number, string):
        self.string = string
        self.number = number

    def __str__(self):
        """Метод представления для пользователя"""
        return f"{self.number}, {self.string}, {self.lst_arc}"

    def __repr__(self):
        """Метод представления для программиста"""
        return f'Archive({self.number}, "{self.string}")'


ins_1 = Archive(5, 'One')
print(ins_1)
ins_2 = Archive(7, 'Two')
print(ins_2)
ins_3 = Archive(9, 'Three')
print(ins_3)
print(repr(ins_3))

