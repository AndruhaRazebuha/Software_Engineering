# Тема 7. Работа с файлами
Отчет по Теме #7 выполнил:
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

## Лабораторная работа №1
Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк


### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/566be0ed-f797-4ac2-8a3b-888fa47620c7)


## Выводы
Вау, создали текстовый файл


## Лабораторная работа №2
Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().
```python
f = open("test.txt", "r")
print(f.readline()) # readline - читает только одну строчку
f.close()
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/c68406f4-f1a0-44b9-a838-9cb337339717)


## Выводы
Вывели первую строчку из текстового документа используя конструкцию open()/close() и readline(), которая выводит только одну строчку.




## Лабораторная работа №3
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().
```python
f = open("test.txt", "r")
print(f.readlines())  # readlines = выводит все строки
f.close()
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/d0ede42a-4516-4d09-84c7-00e8e0c45bb1)


## Выводы
Выводим все строки из файла в массив, используя конструкцию open()/close() и readlineS(), что выводит все строчки.


## Лабораторная работа №4
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open(
```python
with open("test.txt") as f:
    for line in f:
        print(line)
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/35eb1a38-6b1f-4f07-b35a-44bcb615de19)


## Выводы
Выводим все строки из файла в массив, используя with open(), которая сама закрывает файл потом.



## Лабораторная работа №5
Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().
```python
with open("test.txt") as f:
    for line in f:
        print(line)
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/ade65830-dd6d-42b5-9721-3e7ffda24bfa)


## Выводы
Выводим каждую строчку из файла отдлельно, используя конструкцию with open() и цикл для строк.


## Лабораторная работа №6
Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. 
Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.
```python
with open('test.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('test.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/8b273a72-d152-4221-a2b0-da7070aef56e)


## Выводы
Тоже самое, но добавляем f.write(), что записывает новую строчку в файл.


## Лабораторная работа №7
Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Т
акже не забудьте проверить что измененная вами информация сохранилась в файле.
```python
lines = ['one', 'two', 'three']
with open('test.txt', "w") as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/337fe3cc-5719-4283-98a1-8f89a6ffcfa1)
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/32dc81e2-cf56-4d70-9c83-2f495f2a9b63)


## Выводы
Создаем список, затем открываем файл, далее для line в списке lines мы добавляем соответственно с каждой новой записью Cycle run + элемент из списка по очереди.



## Лабораторная работа №8
Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит: ')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])} ')
    print('-' * 40)
print_docs('C:\SoftwareEngineering')
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/a8e984c8-2e0a-46c5-8c3c-49347551a838)



## Выводы
import os  # Импортируем модуль os для работы с файловой системой

def print_docs(directory):  # Объявляем функцию print_docs, которая принимает директорию в качестве аргумента
    all_files = os.walk(directory)  # Получаем список всех файлов и папок в указанной директории и её поддиректориях

    for catalog in all_files:  # Проходимся по каждому элементу в списке all_files (каждый элемент - кортеж)
        print(f'Папка {catalog[0]} содержит: ')  # Выводим название текущей папки (первый элемент кортежа)

    # В следующих трех строках выводим информацию о директориях и файлах в последней обработанной папке (последний catalog в цикле)
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])} ')
    print('-' * 40)  # Выводим разделитель, состоящий из 40 символов "-"

# Вызываем функцию print_docs и передаем ей путь к директории 'C:\SoftwareEngineering'
print_docs('C:\SoftwareEngineering')


## Лабораторная работа №9
Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных
```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_lenght = len(max(words, key = len))
        for word in words:
            if len(word) == max_lenght:
                sought_words=word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words
print(longest_words('input.txt'))
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/afd11e86-8bee-4a8d-b884-765cdf402e4b)



## Выводы
def longest_words(file):
    # Открываем файл для чтения с использованием кодировки UTF-8
    with open(file, encoding='utf-8') as f:
        # Читаем содержимое файла и разбиваем его на слова
        words = f.read().split()
        # Находим длину самого длинного слова в списке
        max_length = len(max(words, key=len))
        # Инициализируем список для хранения всех самых длинных слов
        sought_words = []

        # Перебираем слова в списке
        for word in words:
            # Если длина текущего слова равна максимальной длине, добавляем его в список
            if len(word) == max_length:
                sought_words.append(word)

        # Если в списке только одно самое длинное слово, возвращаем его
        if len(sought_words) == 1:
            return sought_words[0]
        # В противном случае возвращаем список всех самых длинных слов
        return sought_words


## Лабораторная работа №10
ребуется создать csv-файл «rows_300.csv» со следующими столбцами: • № - номер по порядку (от 1 до 300);
```python
import csv
import datetime
import time
with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1,301):
        writer.writerow([line,datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/ef923a63-d7ea-4cbe-bad2-0cc8766b85ae)



## Выводы
import csv  # Импортируем модуль csv для работы с CSV-файлами
import datetime  # Импортируем модуль datetime для работы с датой и временем
import time  # Импортируем модуль time для работы с временными задержками

# Открываем файл 'rows_300.csv' для записи с использованием кодировки UTF-8 и настроек для CSV-файлов
with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)  # Создаем объект writer для записи в CSV-файл

    # Записываем заголовок CSV-файла, состоящий из трех колонок
    writer.writerow(['№', 'Секунда', 'Микросекунда'])

    # Запускаем цикл, который будет записывать данные в CSV-файл
    for line in range(1, 301):
        # Записываем строку в CSV-файл. В этой строке номер строки, текущая секунда и текущая микросекунда
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])

        # Делаем паузу в 0.01 секунды (10 миллисекунд) между записями
        time.sleep(0.01)




## Общие выводы по теме
