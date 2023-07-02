# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.


hike = {
    "Иван": ("спички", "палатка", "фонарик", "нож", "топор", "кружка", "тарелка"),
    "Егор": ("спички", "спальник", "фонарик", "нож", "пила", "кружка", "тарелка"),
    "Денис": ("мангал", "спальник", "фонарик", "ложка", "пила", "кастрюля", "тарелка"),
    "Роман": ("спички", "кукуруза", "фонарик", "нож", "пила", "кружка", "тарелка")
}
keys = list(hike)
FRIENDS = len(hike)
ONE = 1
ZERO = 0

# 1) Какие вещи взяли все три друга (не совсем понял, что имелось ввиду поэтому сделал 2 варианта)

# №1 вариант - одинаковые вещи у всех друзей
common_items = set(hike[keys[0]])
for item in hike:
    common_items = common_items.intersection(set(hike[item]))
print(f'\ncommon items: ', end='')
print(*common_items)

# №2 вариант - все вещи у всех друзей
all_items = set()
for i in range(FRIENDS):
    all_items = set(hike[keys[i]]).union(all_items)
print(f'all items: ', end='')
print(*all_items)


# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
items = {}
for friend, things in hike.items():
    for thing in things:
        if thing not in items:
            items[thing] = [friend]
        else:
            items[thing].append(friend)

items_dict = {thing: friends for thing, friends in items.items() if len(friends) == ONE}

print('\nThe unique items have:')
for thing, friend in items_dict.items():
    print(f"'{thing}' - {friend[ZERO]}")


# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
missing_items = {}
for friend, items in hike.items():
    for item in all_items:
        if item not in items:
            missing_items.setdefault(item, []).append(friend)

missing_items = {item: friends_list for item, friends_list in missing_items.items() if len(friends_list) == ONE}
print("\nMissing items:")
for thing, friend in missing_items.items():
    print(f"'{thing}' - {friend[ZERO]}")

