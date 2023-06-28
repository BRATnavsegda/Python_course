# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def my_func(*, a, b, c):
    locals_variables = locals().items()
    lst_variables = {}
    for key, value in locals_variables:
        if mutable_or_not(value):
            lst_variables[str(value)] = key
        else:
            lst_variables[value] = key
    return lst_variables


def mutable_or_not(value):

    return hasattr(value, '__delitem__') or hasattr(value, 'pop')


print(my_func(a="1", b={12}, c=[15]))



