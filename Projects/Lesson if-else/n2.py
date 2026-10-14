a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Равносторонний")
elif a == b:
    print("Равнобедренный")
elif a == c:
    print("Равнобедренный")
elif b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")
