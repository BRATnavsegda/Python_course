# Напишите следующие функции:
# * Нахождение корней квадратного уравнения
# * Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import json
from pathlib import Path
from random import randint


def decorator_csv_nums(func):
    def wrapper(*args):
        with open('new_csv.csv', 'r', newline='') as csv_rf:
            csv_file = csv.reader(csv_rf)
            for line in csv_file:
                a, b, c = line
                result = func(float(a), float(b), float(c))

        return result
    return wrapper


def decorator_function_log_cash(func):

    file_name = Path("new_json.json")

    if file_name not in Path().iterdir():
        dict_ = {}
    else:
        with open(file_name, 'r', encoding='utf-8') as json_rf:
            dict_ = json.load(json_rf)

    def wrapper(*args):
        params = f'Params a,b,c: {args}'
        if params not in dict_:
            dict_[params] = func(*args)
        else:
            print(f'{params} {dict_[params]}')
        with open(file_name, 'w', encoding='utf-8') as json_wf:
            json.dump(dict_, json_wf)
        return dict_[params]
    return wrapper


def csv_random_nums():
    rows = randint(100, 1000)
    lst_nums = []
    for _ in range(rows):
        lst_nums.append([randint(1, 9), randint(1, 9), randint(1, 9)])
    with open('new_csv.csv', 'w', newline='', encoding='utf-8') as csv_wf:
        writer = csv.writer(csv_wf)
        writer.writerows(lst_nums)


@decorator_csv_nums
@decorator_function_log_cash
def roots_quadratic_equation(*args):

    result = []
    if not args:
        a = float(input('Enter a value a: '))
        b = float(input('Enter a value b: '))
        c = float(input('Enter a value c: '))
    else:
        a, b, c, *_ = args

    print(f'Lets solve a quadratic equation of the form:\n{int(a)}•x²+{int(b)}•x+{int(c)}=0')

    discriminant = b ** 2 - 4 * a * c
    print(f'Discriminant = {discriminant}')
    if discriminant < 0:
        print('There are no roots')
        result.append('There are no roots')
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f'{x =}')
        result.append(f'{x =}')
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f'x₁ = {x1}\nx₂ = {x2}')
        result.append(f'x₁ = {x1} x₂ = {x2}')
    return result


if __name__ == "__main__":
    csv_random_nums()
    roots_quadratic_equation(5, 3, 2)
