# Создаем собственное исключение
class ValueTooSmallError(Exception):
    def __init__(self, value, threshold):
        self.value = value
        self.threshold = threshold
        super().__init__(f"Значение {value} меньше порога {threshold}")

# Используем исключение в функции
def check_value(value):
    threshold = 10
    try:
        if value < threshold:
            raise ValueTooSmallError(value, threshold)
        else:
            print(f"Значение {value} прошло проверку.")
    except ValueTooSmallError as vse:
        print(f"Ошибка: {vse}")

if __name__ == "__main__":
    # Вызываем функцию с использованием исключения
    check_value(5)  # Вывод: Ошибка: Значение 5 меньше порога 10
    check_value(15) # Вывод: Значение 15 прошло проверку.
