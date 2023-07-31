# Доработаем задачи 3 и 4. Создайте класс Project, содержащий атрибуты – список пользователей проекта и админ проекта.
# Класс имеет следующие методы:
# Классовый метод загрузки данных из JSON файла (из второй задачи 8 семинара)
# Метод входа в систему – требует указать имя и id пользователя.
# Далее метод создает пользователя и проверяет есть ли он в списке пользователей проекта.
# Если в списке его нет, то вызывается исключение доступа.
# Если пользователь присутствует в списке пользователей проекта,
# то пользователь, который входит получает его уровень доступа и становится администратором.
# Метод добавление пользователя в список пользователей. Если уровень пользователя меньше, чем уровень админа,
# вызывайте исключение уровня доступа.
# * метод удаления пользователя из списка пользователей проекта
# * метод сохранения списка пользователей в JSON файл при выходе из контекстного менеджера
import json
from pathlib import Path

from sem_task_3 import *

from sem_task_4 import User


class Project:

    def __init__(self, users_lst=None):
        if users_lst is None:
            users_lst = []
        self.users_lst = users_lst
        self.admin = None

    @classmethod
    def get_users_lst(cls, file_name):
        if Path('users_lst.json').is_file():
            with open('users_lst.json', 'r', encoding='utf8') as f:
                file = json.load(f)
        else:
            file = {"4": {"002": "Kuzma"}}
        with open('users_lst.json', 'w', encoding='utf8') as f:
            json.dump(file, f)
        with open(file_name, 'r', encoding='utf-8') as json_r:
            my_dict = json.load(json_r)
        users_lst = []
        for level in my_dict:
            for user in my_dict[level]:

                users_lst.append(User(level, user, my_dict[level][user]))
        return cls(users_lst)

    def login(self, user_to_check=None):
        if user_to_check is None:
            user_to_check = User(input("Enter name: "), input("Enter ID"), input('Enter your level'))
        if user_to_check not in self.users_lst:
            raise AccessException("Access denied", user_to_check)
        self.admin = user_to_check

    def add_user(self, level, id_, name):
        if self.admin.level > level:
            raise LevelException('Low level')
        self.users_lst.append(User(level, id_, name))

    def del_user(self, level, id_, name):
        user = User(level, id_, name)
        if self.admin.level > user.level:
            raise LevelException
        if user not in self.users_lst:
            raise AccessException('Unknown user', user)
        for i, user_lst in enumerate(self.users_lst):
            if user == user_lst:
                self.users_lst.pop(i)
                break

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb,):

        file = {}

        for user in self.users_lst:
            try:
                file[str(user.level)].update({user.id_: user.name})
            except KeyError:
                file[str(user.level)] = {user.id_: user.name}

        with open('users_lst.json', 'w', encoding='utf8') as f:
            json.dump(file, f)

    def __str__(self):
        users = ''
        for user in self.users_lst:
            users += f'{user.name} '
        return users

        
with Project.get_users_lst('users_lst.json') as proj:

    proj.admin = User(1, '000123', 'Misha')

    # proj.add_user(5, '00122', 'Torri')
    # proj.del_user(4, '0012', 'Tor')
    print(proj)


