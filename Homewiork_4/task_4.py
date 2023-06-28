# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег


wallet = 0
count = 0
log_file = []


def adding(cash: int, log_f: list):

    cash_up = int(input("Укажите вносимую сумму, кратную 50\n"))
    if cash_up % 50 == 0:
        cash += cash_up
        log_f.append(str(f'\nпополнение: {cash_up}'))
        return cash, log_file
    else:
        adding(cash)


def withdrawal(cash: int, log_f: list):

    cash_out = int(input("Укажите сумму снятия, кратную 50\n"))
    if cash_out % 50 == 0 and cash_out < cash:
        cash -= cash_out
        log_f.append(str(f'\nснятие: {cash_out}'))
        if 30 < (cash_out * 0.015) < 600:
            cash = cash - (cash_out * 0.015)
            log_f.append(str(f'\nпроцент за снятие: {-cash_out * 0.015}'))

        elif (cash_out * 0.015) < 30:
            cash = cash - 30
            log_f.append(str(f'\nпроцент за снятие: {-30}'))

        else:
            cash = cash - 600
            log_f.append(str(f'\nпроцент за снятие: {-600}'))

    else:
        withdrawal(cash, log_f)
    return cash, log_f


while True:

    x = int(input("\nВведите операцию: \n1 -пополнить \n2 -снять \n3 -выйти \n -->"))
    count += 1

    if x == 3:
        print(f'\nНа счету {wallet}')
        print("\nСписок операций, выполненных во время текущего сеанса:")
        print(*log_file)
        break
    elif x == 1:
        wallet, log_file = adding(wallet, log_file)
    elif x == 2:
        wallet, log_file = withdrawal(wallet, log_file)

    if count % 3 == 0:
        log_file.append(str(f'\nкэшбэк: {wallet * 0.03}'))
        wallet = wallet * 1.03

    if wallet > 5_000_000:
        log_file.append(str(f'\nналог на богатство: {-wallet * 0.1}'))
        wallet = wallet * 0.9

    print(f'\nНа счету {wallet}')
