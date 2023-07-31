# Вспомните задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя,
# личный идентификатор и уровень доступа (от 1 до 7).
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Реализуйте магический метод проверки на равенство пользователей
#

class User:

    def __init__(self, level, id_, name):
        self.level = level
        self.id_ = id_
        self.name = name

    def __eq__(self, other):
        return self.id_ == other.id_

    def __str__(self):
        return f'User {self.name}\nID {self.id_}\nLevel {self.level}'

    def __repr__(self):
        return f'User({self.level}, "{self.id_}", "{self.name}")'


if __name__ == "__main__":
    u = User(3, '000123', 'Misha')
    print(repr(u))
