def remove_element_from_tuple(input_tuple, element):
    if element in input_tuple:
        index = input_tuple.index(element)
        new_tuple = input_tuple[:index] + input_tuple[index+1:]
        return new_tuple
    else:
        # Если элемент не найден, возвращаем исходный кортеж
        return input_tuple

# Пример использования
original_tuple = (1, 2, 3, 4, 5, 6)
element_to_remove = 3
result_tuple = remove_element_from_tuple(original_tuple, element_to_remove)
print("Исходный кортеж:", original_tuple)
print("Кортеж без элемента:", result_tuple)
