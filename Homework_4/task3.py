# '''
# Задача о банкомате
# Разбейте её на отдельные операции - функции. Дополнительно сохраняйте все операции поступления и снятия средств в
# список. Начальная сумма равна нулю.
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
# '''
from decimal import Decimal


def commission(amount: Decimal, percent: Decimal):
    total = amount * percent
    return total


def is_rich():
    global balance
    answer = False
    if balance > 5_000_000:
        answer = True
    return answer


def replenish():
    global balance, operation_count, replenish_percent, history_list
    print('ВНИМАНИЕ!!! Сумма пополнения должна быть кратна 50 у.е.')
    while True:
        if is_rich():
            balance -= commission(balance, tax)
            history_list.append(str(f'Удержан налог на богатство. Текущий баланс: {balance:.2f}'))
            print(history_list[len(history_list) - 1])
        amount = input(f'Текущий баланс: {balance:.2f} у.е. Введите сумму пополнения: ')
        if amount.isdigit() and int(amount) % 50 == 0:
            operation_count += 1
            balance += int(amount)
            if operation_count % 3 == 0:
                add_charge = commission(balance, replenish_percent)
                balance += add_charge
                history_list.append(str(f'Транзакция № {operation_count}. Внесение: {amount} у.е.,'
                                        f'Текущий баланс: {balance:.2f} у.е.'
                                        f'Начислены проценты за пользование услугами банка: {add_charge:.2f} у.е.'))
                print(history_list[len(history_list) - 1])
            else:
                history_list.append(str(f'Транзакция № {operation_count}. Внесение: {amount} у.е.,'
                                        f'текущий баланс: {balance:.2f}'))
                print(history_list[len(history_list) - 1])
            break
        else:
            print('Некорректный ввод, повторите поппытку')
    return


def withdraw_cash():
    global balance, operation_count, withdraw_percent
    print(f'ВНИМАНИЕ!!! Сумма снятия должна быть кратна 50 у.е.')
    while True:
        if is_rich():
            balance -= commission(balance, tax)
            history_list.append(str(f'Удержан налог на богатство. Текущий баланс: {balance:.2f}'))
            print(history_list[len(history_list) - 1])
        amount = input(f'Текущий баланс: {balance:.2f} у.е. Введите необходимую сумму: ')
        if not amount.isdigit() and int(amount) % 50 != 0:
            print('Некорректный ввод, повторите поппытку')
            continue
        operation_comm = commission(Decimal(amount), withdraw_percent)
        if operation_comm < 30:
            operation_comm = 30
        elif operation_comm > 600:
            operation_comm = 600
        total_amount = Decimal(amount) + operation_comm
        if balance >= total_amount:
            operation_count += 1
            balance -= total_amount
            if operation_count % 3 == 0:
                add_charge = commission(balance, replenish_percent)
                balance += add_charge
                history_list.append(str(f'Транзакция № {operation_count}. Снятие наличных: {amount} у.е.,'
                                        f'текущий баланс: {balance:.2f}. Комиссия по операции: {operation_comm:.2f}'))
                print(history_list[len(history_list) - 1])
                history_list.append(str(f'Начислены проценты за пользование услугами банка: {add_charge:.2f} у.е.'))
                print(history_list[len(history_list) - 1])
            else:
                history_list.append(str(f'Транзакция № {operation_count}. Снятие наличных: {amount:} у.е.,'
                                        f'текущий баланс: {balance:.2f} у.е.'
                                        f'Комиссия по операции: {operation_comm:.2f} у.е.'))
                print(history_list[len(history_list) - 1])
            break
        else:
            print('Недостаточно средств на счете!!!')
            break
    return


def exit_atm():
    quit()
    return


def print_menu():
    text = ['Пополнить счет', 'Снять наличные', 'Выйти']
    for i, elem in enumerate(text, start=1):
        print(i, elem)


def menu():
    print_menu()
    while True:
        a = input('Ваш выбор: ')
        if a.isdigit() and int(a) == 1:
            replenish()
        elif a.isdigit() and int(a) == 2:
            withdraw_cash()
        elif a.isdigit() and int(a) == 3:
            exit_atm()
        else:
            print('Некорректный ввод, повторите попытку...')
            continue
        print_menu()


balance = Decimal('0.00')
replenish_percent = Decimal('0.03')
withdraw_percent = Decimal('0.015')
operation_count = 0
tax = Decimal('0.10')
history_list = []

menu()
