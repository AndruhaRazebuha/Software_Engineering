def most_frequent_numbers(input_string):
    # Создаем пустой словарь для подсчета вхождений
    counts = {}

    # Подсчитываем количество вхождений каждой цифры в строке
    for char in input_string:
        if char.isdigit():
            digit = int(char)
            counts[digit] = counts.get(digit, 0) + 1

    # Находим три самых часто встречающихся числа
    most_common = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]

    # Возвращаем результат в порядке возрастания ключей
    result_dict = {k: v for k, v in sorted(most_common, key=lambda x: x[0])}

    return result_dict


# Пример использования
input_string = "127512345689042112"
result = most_frequent_numbers(input_string)
print(result)
