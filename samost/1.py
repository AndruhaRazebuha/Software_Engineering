
user_input = input("Введите последовательность чисел, разделенных пробелом: ")
numbers_list = user_input.split() # Разделить введенную строку на список чисел
numbers_tuple = tuple(numbers_list) # Преобразовать список чисел в кортеж
print("Список чисел:", numbers_list) # Вывести полученный список и кортеж
print("Кортеж чисел:", numbers_tuple)
