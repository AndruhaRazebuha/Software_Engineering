from geron import FormuleOfGerone

a = float(input('Введите значение первой стороны: '))
b = float(input('Введите значение второй стороны: '))
c = float(input('Введите значение третьей стороны: '))

Square = FormuleOfGerone(a, b, c)

print(f"Площадь равна: {Square}")