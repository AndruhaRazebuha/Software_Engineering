# Три списка с длинами сторон треугольников
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
# Находим максимальный и минимальный элементы из каждого списка
max_one, min_one = max(one), min(one)
max_two, min_two = max(two), min(two)
max_three, min_three = max(three), min(three)
# Функция для вычисления площади треугольника по длинам его сторон
def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
# Находим площади треугольников, составленных из максимальных и минимальных элементов
area_max_min_one = triangle_area(max_one, max_two, max_three)
area_min_max_one = triangle_area(min_one, min_two, min_three)
# Вывод результатов
print("Площадь треугольника из максимальных элементов:", area_max_min_one)
print("Площадь треугольника из минимальных элементов:", area_min_max_one)
