# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8, "asd", "qwe", "asd"]
ONE = 1
duplicate_elements_lst = []
print(f'\nThis list: \n{lst}')
for item in lst:
    if lst.count(item) > ONE:
        duplicate_elements_lst.append(item)

duplicate_elements_lst = list(set(duplicate_elements_lst))
print(f'\nThe resulting list: \n{duplicate_elements_lst}')
