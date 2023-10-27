def average(*args):
    if len(args) == 0:
        return None
    total = sum(args)
    return total / len(args)

if __name__ == '__main__':
    values = []

    while True:
        user_input = input("Введите число (или 'Stop' для завершения): ")
        if user_input == 'stop' or user_input == "Stop":
            break
        try:
            value = float(user_input)
            values.append(value)
        except ValueError:
            print("Неверный формат числа. Попробуйте снова.")

    avg = average(*values)
    if avg is not None:
        print(f"Среднее арифметическое: {avg}")
    else:
        print("Нет чисел для вычисления среднего.")