def add_two_and_number():
    try:
        user_input = input("Введите число: ")
        # Пробуем преобразовать введенные данные в число
        number = float(user_input)
        result = 2 + number
        print(f"Результат сложения 2 и введенного числа: {result}")

    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == "__main__":
    # Проведем несколько тестов
    add_two_and_number()
    add_two_and_number()
    add_two_and_number()
    add_two_and_number()
    add_two_and_number()


