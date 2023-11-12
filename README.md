# Тема 10. Декораторы и исключения
Отчет по Теме #10 выполнил:
- Постовалов Андрей Георгиевич
- ПИЭ-21-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | 
| Задание 7 | + | 
| Задание 8 | + | 
| Задание 9 | + | 
| Задание 10 | + | 

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
Вовочка решил заняться спортивным программированием на python, но для этого он должен знать за какое время выполняется его программа. Он решил, что для этого ему идеально подойдет декоратор для функции, который будет выяснять за какое время выполняется та или иная функция. Помогите Вовочке в его начинаниях и напишите такой декоратор. Подсказка: необходимо использовать модуль time Декоратор необходи
def fibonacci(): fib1 = fib2 = 1 for i in range(2, 200): fib1, fib2 = fib2, fib1 fib2 print(fib2, end=' ') if __name__ == '__main__': fibonacci() Результатом вашей работы будет листинг кода и скриншот консоли, в котором будет выполненная функция Фибоначчи и время выполнения программы. Также на этом примере можете посмотреть, что решение задач через рекурсию не всегда является хорошей идеей. Поско

```python
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time} секунд")
        return result
    return wrapper
@timing_decorator
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
if __name__ == '__main__':
    fibonacci()
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/9617e527-c0f4-4264-adc8-72624ba23ca7)


## Выводы
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции {func.__name__}: {execution_time} секунд")
        return result
    return wrapper
@timing_decorator
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
if __name__ == '__main__':
    fibonacci()



## Самостоятельная работа №2
Посмотрев на Вовочку, вы также загорелись идеей спортивного программирования, начав тренировки вы узнали, что для решения некоторых задач необходимо считывать данные из файлов. Но через некоторое время вы столкнулись с проблемой что файлы бывают пустыми, и вы не получаете вводные данные для решения задачи. После этого вы решили не просто считывать данные из файла, а всю конструкцию оборачивать в ис
проблемы. Создайте пустой файл и файл, в котором есть какая-то информация. Напишите код программы. Если файл пустой, то, нужно вызвать исключение (“бросить исключение”) и вывести в консоль “файл пустой”, а если он не пустой, то вывести информацию из файла.
```python
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
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/e998dbe5-bd9e-4973-9495-9a688955289e)
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/744138dc-f6b4-4bde-b4c9-7fc3a8d5209d)


## Выводы
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


## Самостоятельная работа №3
Напишите функцию, которая будет складывать 2 и введенное пользователем число, но если пользователь введет строку или другой неподходящий тип данных, то в консоль выведется ошибка “Неподходящий тип данных. Ожидалось число.”. Реализовать функционал программы необходимо через try/except и подобрать правильный тип исключения. Создавать собственное исключение нельзя. 
Проведите несколько тестов, в которы

```python
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
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/0dbc90a3-1749-40f9-8db5-c3439c9a22d3)


## Выводы
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




## Самостоятельная работа №4
Создайте собственный декоратор, который будет использоваться для двух любых вами придуманных функций. Декораторы, которые использовались ранее в работе нельзя воссоздавать. Результатом выполнения задачи будет: класс декоратора, две как-то связанными с ним функциями, скриншот консоли с выполненной программой и подробные комментарии, которые будут описывать работу вашего кода

```python
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
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/0effa111-ec4e-4628-9b06-08d5f03e358c)
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/3c5679a9-cd38-49d6-a9ce-40ee5ebce384)


## Выводы
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



## Самостоятельная работа №5
Создайте собственное исключение, которое будет использоваться в двух любых фрагментах кода. Исключения, которые использовались ранее в работе нельзя воссоздавать. Результатом выполнения задачи будет: класс исключения, код к котором в двух местах используется это исключение, скриншот консоли с выполненной программой и подробные комментарии, которые будут описывать работу вашего кода


```python
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
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/f7dbc3d5-7978-43ea-8428-87baf410b6f8)



## Выводы
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


## Общие выводы по теме
Декораторы и исключения важный аспект в программной инженерии

