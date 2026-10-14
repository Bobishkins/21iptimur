import math

def calculate_distance(x1, y1, x2, y2):
    """Находит расстояние между двумя точками по их координатам"""
    dx = x2 - x1
    dy = y2 - y1
    return math.sqrt(dx ** 2 + dy ** 2)

def calculate_triangle_area(a, b, c):
    """Вычисляет площадь треугольника по формуле Герона"""
    half_perimeter = (a + b + c) / 2

    area = math.sqrt(half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c))
    return area

x1, y1, x2, y2, x3, y3 = map(float, input("Введите координаты трех вершин (x1 y1 x2 y2 x3 y3): ").split())

a = calculate_distance(x1, y1, x2, y2)
b = calculate_distance(x2, y2, x3, y3)
c = calculate_distance(x3, y3, x1, y1)

triangle_area = calculate_triangle_area(a, b, c)

print(f"Площадь треугольника: {triangle_area:.2f}")
