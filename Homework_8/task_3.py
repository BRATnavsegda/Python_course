# Решить задачи, которые не успели решить на семинаре.
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import csv
import json
import os
import pickle
from pathlib import Path


def made_json_csv_pickle(directory, lst):
    with(
        open(f'out/{directory.name}_1.json', 'w', encoding='utf8') as json_wf,
        open(f'out/{directory.name}_2.csv', 'w', encoding='utf8') as csv_wf,
        open(f'out/{directory.name}_3.pickle', 'wb') as pickle_wf,
    ):
        pickle.dump(lst, pickle_wf)

        json.dump(lst, json_wf)

        dict_list = []
        for item in lst:
            for parent, (object_, type_, size_) in item.items():

                dict_list.append({
                    'object': object_["object"],
                    'type': type_['type'],
                    'size': size_['size'],
                    'Parent': parent,
                })
        writer = csv.DictWriter(csv_wf, fieldnames=['object', 'type', 'size', 'Parent'])
        writer.writeheader()
        writer.writerows(dict_list)


def directory_walker(directory=Path.cwd(), list_dicts=None):  # obj,parent,obj_type,size

    if list_dicts is None:
        list_dicts = []
    for item in directory.iterdir():
        # print(*os.walk(item))
        size = 0
        if item.is_dir():
            for elem in os.scandir(item):
                size += os.stat(elem).st_size
                directory_walker(item, list_dicts)
        else:
            size = item.stat().st_size
        dict_ = [
            {'object': item.name},
            {'type': 'folder' if item.is_dir() else 'file'},
            {'size': size},

        ]
        new_line = {f'Parent: {directory.name}': dict_}
        if new_line not in list_dicts:
            list_dicts.append(new_line)

    return list_dicts


if __name__ == '__main__':

    made_json_csv_pickle(Path('out'), directory_walker())

