pocket = int(input("Введите номер кармана: "))

if pocket < 0 or pocket > 36:
    print("Ошибка, введите число в диапазоне 0-36")
elif pocket == 0:
    print("зеленый")
elif 1 <= pocket <= 10 and pocket % 2 == 1:
    print("красный")
elif 1 <= pocket <= 10 and pocket % 2 == 0:
    print("черный")
elif 11 <= pocket <= 18 and pocket % 2 == 1:
    print("черный")
elif 11 <= pocket <= 18 and pocket % 2 == 0:
    print("красный")
elif 19 <= pocket <= 28 and pocket % 2 == 1:
    print("красный")
elif 19 <= pocket <= 28 and pocket % 2 == 0:
    print("черный")
elif 29 <= pocket <= 36 and pocket % 2 == 1:
    print("черный")
elif 29 <= pocket <= 36 and pocket % 2 == 0:
    print("красный")
