colour1 = input()
colour2 = input()

if colour1 not in ("красный", "синий", "желтый") or colour2 not in ("красный", "синий", "желтый"):
    print("Выберите цвет из доступных: красный, синий, желтый")
elif (colour1 == "красный" and colour2 == "синий") or (colour1 == "синий" and colour2 == "красный"):
    print("фиолетовый")
elif (colour1 == "красный" and colour2 == "желтый") or (colour1 == "желтый" and colour2 == "красный"):
    print("оранжевый")
elif colour1 == colour2:
    print(colour1)
else:
    print("зеленый")
