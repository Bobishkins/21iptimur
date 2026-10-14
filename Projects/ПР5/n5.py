BANKNOTES = (5000, 2000, 1000, 500, 200, 100)

def calculate_banknotes(amount):
    """Рассчитывает количество купюр каждого номинала."""
    result = {}

    for banknote in BANKNOTES:
        count = amount // banknote
        result[banknote] = count
        amount = amount % banknote

    return result

amount = int(input("Введите сумму для снятия: "))

if amount <=0 or amount % 100 != 0:
    print("Сумма должна быть положительной и кратной 100")
else:
    banknotes = calculate_banknotes(amount)

    print('Отчет о выдаче наличных:')

    for banknote, count in banknotes.items():
        if count > 0:
            print(f"Купюр по {banknote} руб: {count}")

    print(f"Общая сумма: {amount} руб.")
