even_array = [2,4,5,6,9]
flag = False
for value in even_array:
    if value % 2 == 1:
        flag = True
if flag is True:
    print('Есть нечетное число')
else:
    print('Все числа четные')