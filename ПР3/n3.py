#№1
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
print(num1, num2) #№2
print(num1 + num2) #№3
# Если ввести буквы, то выдаст ошибку ValueError, потому что int(input()) не поддерживает тип string    №5


# #№6
# try:
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print(num1, num2)  # №2
#     print(num1 + num2)  # №3
# except ValueError:
#     print("Произола ошибка, Вы ввели не число. Введите целое число")
