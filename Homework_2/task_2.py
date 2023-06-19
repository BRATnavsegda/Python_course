# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

SYS_NUMBERS = 16
HEX_DIGIT = 9
res = []
hex_letters = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}

user_number = int(input("Enter number: "))
print(f'hex:        {hex(user_number)}')
print('my_program: ', end='')

if user_number < 0:
    user_number = abs(user_number)
    print('-', end='')

while user_number > 0:
    user_number, digit = divmod(user_number, SYS_NUMBERS)
    if digit > HEX_DIGIT:
        digit = hex_letters.get(digit)
    res.append(str(digit))

print(f'0x{"".join(list(reversed(res)))}')


