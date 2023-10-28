def process_grades(grades):
    # Создаем пустой список для обработанных оценок
    processed_grades = []

    # Проходим по каждой оценке в исходном списке
    for grade in grades:
        if grade != 2:
            if grade == 3:
                processed_grades.append(4)
            else:
                processed_grades.append(grade)

    return processed_grades

# Первый вариант списка оценок
grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
# Второй вариант списка оценок
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
# Третий вариант списка оценок
grades3 = [5, 4, 3, 3, 4]
# Обработка и вывод результатов
processed_grades1 = process_grades(grades1)
print("Первый вариант после обработки:", processed_grades1)
processed_grades2 = process_grades(grades2)
print("Второй вариант после обработки:", processed_grades2)
processed_grades3 = process_grades(grades3)
print("Третий вариант после обработки:", processed_grades3)
