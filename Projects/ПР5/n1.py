TAX_RATE = 0.13

income = float(input("Введите годовый доход в рублях: "))

tax = income * TAX_RATE
net_income = income - tax

print(f"Общая сумма дохода: {income:.2f} руб.")
print(f"Сумма налога: {tax:.2f} руб.")
print(f"Доход на руки: {net_income:.2f} руб.")
