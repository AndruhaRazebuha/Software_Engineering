def fib(n):
    a, b = 1, 1
    with open("fib.txt", "w") as file:
        for _ in range(n):
            file.write(f"{a}\n")  # Записываем число на отдельной строке
            yield a
            a, b = b, a + b

if __name__ == "__main__":
    n = 10
    fibonacci_sequence = list(fib(n))

    with open("fib.txt", "a") as file:
        for i, value in enumerate(fib(200)):
            if i == 199:
                file.write(f"{value}\n")

    # Проверим файл "fib.txt" после выполнения программы
    with open("fib.txt", "r") as file:
        content = file.read()
        print("Содержимое файла 'fib.txt':\n", content)
