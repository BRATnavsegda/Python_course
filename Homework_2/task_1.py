# Решить задачи, которые не успели решить на семинаре.

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

def adding(cash):

    cash_up = int(input("Укажите вносимую сумму, кратную 50\n"))
    if cash_up % 50 == 0:
        cash += cash_up
        return cash
    else:
        adding(cash)


def withdrawal(cash):

    cash_out = int(input("Укажите сумму снятия, кратную 50\n"))
    if cash_out % 50 == 0 and cash_out < cash:
        cash -= cash_out
        if 30 < (cash_out * 0.015) < 600:
            cash = cash - (cash_out * 0.015)

        elif (cash_out * 0.015) < 30:
            cash = cash - 30

        else:
            cash = cash - 600

    else:
        withdrawal(cash)
    return cash


wallet = 0
count = 0

while True:

    x = int(input("Введите операцию: \n1 -пополнить \n2 -снять \n3 -выйти \n -->"))
    count += 1

    if x == 3:
        break
    elif x == 1:
        wallet = adding(wallet)
    elif x == 2:
        wallet = withdrawal(wallet)

    if count % 3 == 0:
        wallet = wallet * 1.03

    if wallet > 5_000_000:
        wallet = wallet * 0.9

    print(f'На счету {wallet}')
