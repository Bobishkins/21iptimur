USD_TO_RUB = 85.12

def convert_usd_to_rub(amount_usd):
    """Переводит доллары в рубли"""
    return amount_usd * USD_TO_RUB

usd = float(input("Введите сумму в долларах: "))
rub = convert_usd_to_rub(usd)

print(f"Сумма в рублях: {rub:.2f} руб.")
