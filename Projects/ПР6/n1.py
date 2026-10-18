temp = float(input("Введите температуру: "))
pressure = int(input("Введите верхнее давление: "))
pulse = int(input("Введите пульс: "))

if (temp < -50 or temp > 60 or pressure <= 0 or pressure > 300 or pulse <= 0 or pulse > 300):
    print("Ошибка ввода")
elif (temp < 35 or temp > 38 or pressure < 105 or pressure > 140 or pulse < 55 or pulse > 110):
    print("Требуется врач")
elif (36 <= temp <= 37 and 110 <= pressure <= 130 and 60 <= pulse <= 100):
    print("Нормальное состояние")
else:
    print("Легкое недомогание")
