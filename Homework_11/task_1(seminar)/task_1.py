# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

from time import time, strftime, gmtime


class MyStr(str):
    """Класс, где доступны все возможности класса str. Также, дополнительно хранятся имя автора строки и время её
    создания """

    def __init__(self, value, name):
        super().__init__()
        self.name = name
        self.value = value

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.start_time = strftime('%H:%M:%S', gmtime(time()))
        return instance

    def __str__(self):
        return f"Value: {self.value}; Name: {self.name}; Time: {self.start_time}"


str1 = MyStr('Hello', 'Kuchin')

print(str1)
