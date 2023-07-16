
# ----------------------------------------------------------------------------------------------------------

# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции

from random import randint, uniform

__all__ = ['rand_nums_in_file']


def rand_nums_in_file(rows: int, file_name: str):
    with open(file_name, 'a', encoding="utf-8") as f:
        for _ in range(rows):
            f.write(f'{randint(START, END)}|{uniform(START, END)}\n')


START = -1000
END = 1000


class RandomNums:
    START = -1000
    END = 1000

    def __init__(self, rows: int, file_name: str):
        self.file_name = file_name
        self.rows = rows

    def rand_nums_in_file(self):
        with open(self.file_name, 'a', encoding="utf-8") as f:
            for _ in range(self.rows):
                f.write(f'{randint(START, END)}|{uniform(START, END)}\n')


if __name__ == "__main__":
    # rand_nums_in_file(8, 'out/task_1.txt')
    new_instance = RandomNums(2, 'task_2_2.txt')
    new_instance.rand_nums_in_file()
