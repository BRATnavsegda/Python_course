# Прежде всего хотелось бы выразить Вам огромную благодарность за вашу работу.
# Присоединяюсь ко всему сказанному ребятами на семинаре.
# Вы лучший преподаватель из всех встреченных мной на данный момент.
# Желаю Вам удачи и успехов во всех начинаниях, и пусть ваша работа приносит Вам только положительные эмоции!!!
# Большое человеческое Вам СПАСИБО!!!
# --------------------------------------------------------------------------------


# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.
from collections import namedtuple
import os
from pathlib import Path
import logging
from datetime import datetime
import argparse

parser = argparse.ArgumentParser(description='My parser')
parser.add_argument('directory', type=str, nargs='?')
dir_name = parser.parse_args()


logging.basicConfig(filename='task_1.log',
                    level=logging.INFO,
                    encoding='utf-8',
                    )
logger = logging.getLogger(__name__)


def directory_walker(directory=None, list_named_tuples=None):
    if directory is None:
        directory = Path.cwd()
    else:
        directory = Path(directory)

    if list_named_tuples is None:
        list_named_tuples = []
    File_or_dir = namedtuple('File_or_dir', ['file_name', 'ext_or_dir', 'size', 'parent_dir', 'time'])
    for item in directory.iterdir():
        size = 0
        if item.is_dir():
            for elem in os.scandir(item):
                size += os.stat(elem).st_size
                directory_walker(item, list_named_tuples)
        else:
            size = item.stat().st_size

        file_name, ext = item.name.split('.') if not item.is_dir() else (item.name, 'directory')
        new_line = File_or_dir(file_name, ext, size, directory.name, datetime.now().strftime('Дата %d %B %Y. Время '
                                                                                             '%H:%M:%S.'))
        if new_line not in list_named_tuples:
            list_named_tuples.append(new_line)
            logger.info(new_line)

    return list_named_tuples


if __name__ == "__main__":
    directory_walker()

# python task_1.py 'C:\Users\TESO\Desktop\Lessions\Python_course\Homeworks\Python_course\Homework_15'
# вроде всё нормально, но что-то упустил, этой командой запустить не получается
