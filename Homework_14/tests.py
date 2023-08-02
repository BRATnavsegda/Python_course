# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.


import pytest
import json

from User_class import User
from MyExeptions import *
from Project_class import Project


@pytest.fixture
def get_file(tmp_path):
    file_name = tmp_path / 'users_lst.json'

    with open(file_name, 'w+', encoding='utf-8') as f:
        file_data = {"4": {"002": "Kuzma"}, "5": {"00122": "Torri"}}
        json.dump(file_data, f)
        # yield file_name
    return file_name


@pytest.fixture
def set_project(get_file):
    with Project.get_users_lst(get_file) as proj:
        proj.admin = User(1, '000123', 'Misha')
    return proj


def test_add_user(get_file, set_project):
    proj = set_project
    proj.add_user(4, "0012", "Tor")
    assert proj.users_lst == [User(4, "002", "Kuzma"),
                              User(5, "00122", "Torri"),
                              User(4, "0012", "Tor")]


def test_del_user(get_file, set_project):
    proj = set_project
    proj.del_user(4, "002", "Kuzma")
    assert proj.users_lst == [User(5, "00122", "Torri")]


@pytest.mark.parametrize("self_user, other_user, expected",
                         [
                             (User(2, "123", "Igor"), User(2, "123", "Igor"), True),
                             (User(2, "123", "Igor"), User(2, "345", "Igor"), False),
                             pytest.param(User(2, "123", "Igor"), User(2, 345, "Igor"), False, marks=pytest.mark.xfail)
                         ])
def test_users(self_user, other_user, expected):
    assert (self_user == other_user) == expected
