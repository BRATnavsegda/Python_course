# Решить задачи, которые не успели решить на семинаре.

# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

def cashup():
    global cash
    cash_up = int(input("Укажите вносимую сумму, кратную 50\n"))
    if cash_up % 50 == 0:
        cash += cash_up
    else:
        cashup()


def cashout():
    global cash
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
        cashout()


cash = 0
count = 0

while True:

    x = int(input("Введите операцию: \n1 -пополнить \n2 -снять \n3 -выйти \n -->"))
    count += 1

    if x == 3:
        break
    elif x == 1:
        cashup()
    elif x == 2:
        cashout()

    if count % 3 == 0:
        cash = cash * 1.03

    if cash > 5_000_000:
        cash = cash * 0.9

    print(f'На счету {cash}')
