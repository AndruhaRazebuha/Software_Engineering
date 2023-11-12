try:
    # Попробуем открыть файл с информацией
    with open('test.txt', 'r', encoding='utf-8') as file:
        content = file.read()

        # Проверим, пустой ли файл
        if not content:
            raise Exception("файл пустой")

        # Если файл не пустой, выведем информацию
        print("Информация из файла:")
        print(content)

except FileNotFoundError:
    print("Файл не найден")

except Exception as e:
    print(f"Ошибка: {e}")
