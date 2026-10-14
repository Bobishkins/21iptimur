weight = int(input("Введите вес (целое число): "))

if weight < 60:
    print("Легкий вес")
elif weight < 64:
    print("Первый полусредний вес")
elif weight < 69:
    print("Полусредний вес")
else:
    print("Вес слишком большой")
