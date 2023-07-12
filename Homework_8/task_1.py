# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестирования возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import pickle
from pathlib import Path


def pickle_to_csv(pickle_file):
    file_name = Path(pickle_file)

    with open(file_name, 'rb') as pickle_rf:
        data = pickle.load(pickle_rf)
    keys = []

    for key in data[0].keys():
        keys.append(key)

    with open(f'out/{file_name.stem}.csv', 'w', newline='', ) as csv_wf:
        writer = csv.DictWriter(csv_wf, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


if __name__ == '__main__':
    pickle_to_csv('out/task_5_sem.pickle')

