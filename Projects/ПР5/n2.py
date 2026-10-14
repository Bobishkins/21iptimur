weight, height = map(float, input("Введите вес в кг и рост в метрах через пробел: ").split())

bmi = weight / (height * height)

print(f"Ваш индекс массы тела: {bmi:.1f}")
