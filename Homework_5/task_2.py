# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

names = ['Ben', 'Danila', 'Brother']
salaries = [40000, 15000, 50000]
prizes = ['12.45%', '10.40%', '15.50%']
ONE = 1
HUNDRED = 100


# сначала сделал без функции:
dict_prizes = {name: (salary * float(prize[:-ONE]) / HUNDRED) for name, salary, prize in zip(names, salaries, prizes)}
print(dict_prizes)
#
# потом подумал, что в условии "возможно" имелось ввиду именно сделать генератор-функцию...
# получилось как то так:


def generator_prizes(names_lst: list, salaries_lst: list, prizes_lst: list):
    yield {name: (salary * float(prize[:-ONE]) / HUNDRED) for name, salary, prize
           in zip(names_lst, salaries_lst, prizes_lst)}


print(type(generator_prizes(names, salaries, prizes)))

