# 1) Решить задачи, которые не успели решить на семинаре.

# перенести таблицу умножения с тетрадки

MIN_LIMIT = 2
MAX_LIMIT = 10
INPUT_CENTER = 61
COLUMN = 4
STEP = 1

TEXT = "таблица умножения \n"

print(TEXT.upper().center(INPUT_CENTER))

for i in range(MIN_LIMIT, MAX_LIMIT - STEP, COLUMN):
    for j in range(MIN_LIMIT, MAX_LIMIT + STEP):
        for k in range(i, i + COLUMN):
            print(f'{k:>3} X {j:>2} = {k * j:>2}', end="  ")
        print()
    print()
