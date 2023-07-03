# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os

path = "task_1.py"

file_path = os.path.abspath(path)


def file_func(file: str):

    *_, file_name = file.split('\\')
    file = file[0: -len(file_name)]
    file_name, file_extension = file_name.split('.')
    return file, file_name, file_extension


print(file_func(file_path))
