def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    # Вызываем функцию итератора для генерации чисел Фибоначчи
    n = 10  # Указываем количество чисел, которые хотим получить
    fibonacci_sequence = list(fib(n))

    # Выводим результаты, начиная с числа Фибоначчи под номером 200
    for i, value in enumerate(fib(200)):
        if i == 199:  # Выводим только значение под номером 200
            print(f"Число Фибоначчи под номером 200: {value}")
            break
