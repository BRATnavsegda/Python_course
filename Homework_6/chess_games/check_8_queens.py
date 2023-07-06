# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок


__all__ = ['chess_comb']


def add_queen(i, j):
    for x in range(8):
        chess_table[x][j] += 1
        chess_table[i][x] += 1
        # print(chess_table)
        if 0 <= i + j - x < 8:
            chess_table[i + j - x][x] += 1
        if 0 <= i - j + x < 8:
            chess_table[i - j + x][x] += 1
    chess_table[i][j] = -1


def del_queen(i, j):
    for x in range(8):
        chess_table[x][j] -= 1
        chess_table[i][x] -= 1
        # print(chess_table)
        if 0 <= i + j - x < 8:
            chess_table[i + j - x][x] -= 1
        if 0 <= i - j + x < 8:
            chess_table[i - j + x][x] -= 1
    chess_table[i][j] = 0


def chess_comb(i=0):
    global count
    for j in range(8):
        if chess_table[i][j] == 0:
            add_queen(i, j)
            if i == 7:
                count += 1
                show_wright_positions(count)
            else:
                chess_comb(i + 1)
            del_queen(i, j)


def show_wright_positions(cnt):
    chess_table_wins = [["\U00002610" for i in range(8)] for j in range(8)]
    for i in range(8):

        for j in range(8):
            if chess_table[i][j] == -1:
                chess_table_wins[i][j] = "\U00002655"
    print(f'\n{cnt}.   a     b    c    d     e    f     g    h')
    chess_table_wins = {i: j for i, j in enumerate(chess_table_wins, 1)}
    print(*chess_table_wins.items(), sep='\n')


count = 0
chess_table = [[0 for i in range(8)] for j in range(8)]

if __name__ == '__main__':
    chess_comb()

















# from random import randint
# from itertools import permutations, combinations


# def new_queen():
#     for i in range(1, 9):
#         for j in range(1, 9):
#             yield [i, j]
#
#
# def new_list():
#     my_list = [*new_queen()]
#     while True:
#         my_list = [my_list[-1]] + my_list[:-1]
#         yield my_list
#
#
#
# def generator_combs():
#     count = 0
#     my_list = [*new_queen()]
#     new_comb = []
#     while len(new_comb) < 8:
#         my_iter = new_list()
#         work_list = next(my_iter)
#
#         new_comb = [work_list.pop(count)]
#         rows = [new_comb[0][0]]
#         columns = [new_comb[0][1]]
#         while len(work_list) > 0:
#             new_chess = work_list.pop(count)
#
#             if new_chess[0] not in rows:
#                 if new_chess[1] not in columns:
#                     for item in new_comb:
#                         if not kill_or_not_two(item, new_chess):
#                             break
#                         elif item == new_comb[-1]:
#                             rows.append(new_chess[0])
#                             columns.append(new_chess[1])
#                             new_comb.append(new_chess)
#         count += 1
#         print(new_comb, rows, columns)
#         # break
#
#
# def kill_or_not_two(chess_1: list, chess_2: list):
#
#     """Если ферзь1 бьет ферзя2, возвращает False"""
#
#     if chess_1[0] == chess_2[0] or chess_1[1] == chess_2[1]:
#         return False
#     elif ((chess_1[0]*10 + chess_1[1]) - (chess_2[0]*10 + chess_2[1])) % 11 == 0:
#         return False
#     elif chess_1[0] + chess_1[1] == chess_2[0] + chess_2[1]:
#         return False
#     else:
#         return True
#
#
# def kill_or_not_list(chess: list):
#
#     for chess_1, chess_2 in permutations(chess, 2):
#         if chess_1[0] == chess_2[0] or chess_1[1] == chess_2[1]:
#             return False
#         elif ((chess_1[0]*10 + chess_1[1]) - (chess_2[0]*10 + chess_2[1])) % 11 == 0:
#             return False
#         elif chess_1[0] + chess_1[1] == chess_2[0] + chess_2[1]:
#             return False
#         else:
#             continue
#     return True
#
# def generator_combs2():
#     my_list = [*new_queen()]
#     count = 0
#     for combination in combinations(my_list, 8):
#         print(list(combination))
#         if len({x[0]: x[1] for x in combination}) == len(combination):
#             if len({x[1]: x[0] for x in combination}) == len(combination):
#                 print(list(combination))
#                 if kill_or_not_list(list(combination)):
#                     count += 1
#                     print(count, combination)
#
#
# generator_combs()
# lst = [[1, 1], [5, 2], [4, 3], [7, 4], [5, 5], [8, 6], [2, 7], [1, 8]]
# list_of_dicts = len({x[0]: x[1] for x in lst})
# print(list_of_dicts)



