# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import random
from itertools import combinations
COMBS = 10000
ONE = 1
hike_things = {
    "палатка": 6,
    "кружка": 0.3,
    "спички": 0.1,
    "тарелка": 0.2,
    "фонарик": 0.3,
    "горелка": 1,
    "нож": 0.2,
    "спальник": 3,
}
BACKPACK = 10

# for i in range(1, len(hike_things) + ONE):
#     for combination in combinations(hike_things.items(), i):
#         print(combination)


#  Попробовал реализовать сам, получился вариант с всегда наполненным рюкзаком, но самих вариантов немного.

full_backpack = {}
all_combinations = []
new_combination = ''
hash_collection = []
for i in range(COMBS):
    for j in range(1, len(hike_things) + ONE):
        random_key = random.choice(list(hike_things))
        random_value = hike_things[random_key]
        if sum(full_backpack.values()) < BACKPACK \
                and sum(full_backpack.values()) + random_value < BACKPACK:
            full_backpack[random_key] = random_value
    new_combination = str(full_backpack)
    if hash(new_combination) not in hash_collection:
        hash_collection.append(hash(new_combination))
        all_combinations.append(new_combination)

for i in range(len(all_combinations)):
    print(all_combinations[i])
