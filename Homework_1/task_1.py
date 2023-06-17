# 1) Решить задачи, которые не успели решить на семинаре.

# перенести таблицу умножения с тетрадки

MIN_LIMIT = 2
MAX_LIMIT = 10
INPUT_CENTER = 61
STEP = 1

TEXT = "таблица умножения \n"

print(TEXT.upper().center(INPUT_CENTER))

for i in range(MIN_LIMIT, MAX_LIMIT + STEP):
    for j in range(MIN_LIMIT, MAX_LIMIT // MIN_LIMIT + STEP):
        print(f'{j:>3} X {i:>2} = {i * j:>2}', end="  ")
    print()
print()

for i in range(MIN_LIMIT, MAX_LIMIT + STEP):
    for j in range(MAX_LIMIT // MIN_LIMIT + STEP, MAX_LIMIT):
        print(f'{j:>3} X {i:>2} = {i * j:>2}', end="  ")
    print()
print()
