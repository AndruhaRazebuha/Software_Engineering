import time

# Создаем класс декоратора
class TimingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {self.func.__name__}: {execution_time} секунд")
        return result

# Используем декоратор для двух функций
@TimingDecorator
def example_function_1():
    print("Выполняется функция 1")
    time.sleep(2)

@TimingDecorator
def example_function_2():
    print("Выполняется функция 2")
    time.sleep(1)

if __name__ == "__main__":
    # Вызываем обе функции, декоратор будет отслеживать время выполнения
    example_function_1()
    example_function_2()
