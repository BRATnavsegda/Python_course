# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None. Значения не удаляются,
# а помещаются в одноимённые переменные без s на конце.

cats = ['c', 'a', 't']
dogs = ['d', 'o', 'g']
s = 's'
tiger = ['t', 'i', 'g', 'e', 'r']
dir_dict = globals()


def change_var(variables_dict):

    keys_to_change = []
    for key in variables_dict:
        if key[-1] == 's' and len(key) > 1:
            keys_to_change.append(key)

    for key in keys_to_change:
        variables_dict[key[:-1]] = variables_dict[key]
        variables_dict[key] = None


print(dir_dict)

change_var(dir_dict)

print(dir_dict)

