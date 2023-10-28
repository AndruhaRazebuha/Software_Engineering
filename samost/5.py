# Функция для преобразования списка в множество с учетом правила
def transform_list_to_set(lst):
    result_set = set()

    for num in lst:
        count = lst.count(num)
        if count > 1:
            for i in range(1, count + 1):
                result_set.add(str(num) * i)
        else:
            result_set.add(num)

    return result_set

# Первый список
list_1 = [1, 1, 3, 3, 1]
set_1 = transform_list_to_set(list_1)
print(set_1)

# Второй список
list_2 = [5, 5, 5, 5, 5, 5, 5]
set_2 = transform_list_to_set(list_2)
print(set_2)

# Третий список
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
set_3 = transform_list_to_set(list_3)
print(set_3)
