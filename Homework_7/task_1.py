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


if __name__ == '__main__':
    rename_files('txt', 'new_name', 'pdf')
