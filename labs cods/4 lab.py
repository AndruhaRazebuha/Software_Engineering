massive = [1, 2, 3, 4, 5]
value = int(input("Введите число: "))
if value in massive:
    if value % 2 == 0:
        print('Число в массиве и четное')
    else:
        print('Число в массиве и нечетное')
else:
    print(f"Числа нет в массиве и оно равно {value}")
