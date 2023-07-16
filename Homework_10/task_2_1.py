# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали.
# Превратите функции в методы класса. Задачи должны решаться через вызов методов экземпляра.

# ---------------------------------------------------------------------------------------------------------------

# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
from pathlib import Path

__all__ = ['rename_files']


def rename_files(old_ext, new_name, new_ext):
    p = Path(Path.cwd())
    count = 0
    for file in p.iterdir():
        if file.suffix[1:] == old_ext:
            count += 1
            old_name, _ = Path(file).name.split('.')
            Path(file).rename(f'{old_name}_{new_name}_{count}.{new_ext}')


class RenameFiles:

    def __init__(self, old_ext, new_name, new_ext):
        self.new_ext = new_ext
        self.new_name = new_name
        self.old_ext = old_ext

    def rename_files(self):

        p = Path(Path.cwd())
        count = 0
        for file in p.iterdir():
            if file.suffix[1:] == self.old_ext:
                count += 1
                old_name = Path(file).stem
                Path(file).rename(f'{old_name}_{self.new_name}_{count}.{self.new_ext}')


if __name__ == '__main__':

    new_instance = RenameFiles('txt', 'new_name', 'pdf')
    new_instance.rename_files()

