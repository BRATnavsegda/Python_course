# Создайте класс с базовым исключением и дочерние классы-исключения:
# ошибка уровня,
# ошибка доступа.
#

class MyBaseException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        pass


class LevelException(MyBaseException):
    def __init__(self, message='Level error', user='the current user'):
        self.user = user
        self.message = message

    def __str__(self):
        print(f'{self.message} to {self.user}')


class AccessException(MyBaseException):
    def __init__(self, message='Access error', user='the current user'):
        self.user = user
        self.message = message

    def __str__(self):
        print(f'{self.message} to {self.user}')

