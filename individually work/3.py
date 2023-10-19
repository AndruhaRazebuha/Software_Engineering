number = int(input('Введите число от 0 до 10: '))
if number in range(11):
    if number <= 3:
        print("Число в диапозоне от 0 до 3")
    elif 3 < number <= 6:
        print("Число от 3 до 6 включительно")
    else:
        print("Число от 6 до 10 включительно")
else:
    print('Число не от 0 до 10')