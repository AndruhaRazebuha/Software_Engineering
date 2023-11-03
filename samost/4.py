def extract_employee_records(records, target_id):
    if target_id not in records:
        return ()  # Элемент отсутствует в кортеже, возвращаем пустой кортеж

    first_occurrence = records.index(target_id)
    last_occurrence = len(records) - records[::-1].index(target_id) - 1

    return records[first_occurrence:last_occurrence + 1]

# Пример использования
employee_records = (1, 2, 3, 4, 2, 5, 6, 2, 7, 8)
target_id = 2
result = extract_employee_records(employee_records, target_id)
print(result)
