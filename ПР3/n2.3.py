#№3
my_string = "cat"
my_string[0] = 'b'
print(my_string) # При выводе кода выдаст ошибку: TypeError: 'str' object does not support item assignment
# Строка является неизменяемой, это значит, что после создания ее нельзя будет изменить
