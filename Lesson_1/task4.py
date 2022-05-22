def bank_deposit_calc(deposit, term):
    percent = 0
    if 1000 <= deposit < 10000:
        if 6 <= term < 12:
            percent = 5
        elif 12 <= term < 24:
            percent = 6
        elif term >= 24:
            percent = 5
    elif 10000 <= deposit < 100000:
        if 6 <= term < 12:
            percent = 6
        elif 12 <= term < 24:
            percent = 7
        elif term >= 24:
            percent = 6.5

    elif 100000 <= deposit < 1000000:
        if 6 <= term < 12:
            percent = 7
        elif 12 <= term < 24:
            percent = 8
        elif term >= 24:
            percent = 7.5
    else:
        raise Exception('Ошибка в вводных данных')

    result = deposit
    for _ in range(term):
        res = result * percent / 1200
        result += res

    return f'Сумма вклада на конец месяца: {result}'


dep = int(input('Введите сумму депозита (от 1000 до 1000000): '))
term = int(input('Введите срок депозита в месяцах (от 6 месяцев): '))

print(bank_deposit_calc(dep, term))