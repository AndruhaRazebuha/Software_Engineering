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



## Самостоятельная работа #1
Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.
```python
import string
def count_words(filename):
    word_count = {}
    most_common_word = ""
    max_count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = text.split()
        for word in words:
            word = word.strip(string.punctuation)  # Удаляем знаки препинания из слова
            if word:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                if word_count[word] > max_count:
                    max_count = word_count[word]
                    most_common_word = word
    total_words = sum(word_count.values())
    return total_words, most_common_word, max_count
if __name__ == "__main__":
    filename = "statia.txt"
    total_words, most_common_word, max_count = count_words(filename)

    print("Всего слов в файле:", total_words)
    print("Самое часто встречающееся слово:", most_common_word)
    print("Количество повторений:", max_count)
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/78422323-ab99-4ad7-b8a3-fc8422895ed2)


## Выводы
import string  # Импортируем модуль string для работы со строками и знаками препинания.

def count_words(filename):
    word_count = {}  # Создаем пустой словарь для подсчета слов и их количества.
    most_common_word = ""  # Переменная для хранения самого часто встречающегося слова.
    max_count = 0  # Переменная для хранения количества повторений самого частого слова.

    with open(filename, 'r', encoding='utf-8') as file:  # Открываем файл для чтения в указанной кодировке.
        text = file.read().lower()  # Читаем содержимое файла и преобразуем его в нижний регистр.
        words = text.split()  # Разбиваем текст на слова, используя пробелы как разделители.

        for word in words:
            word = word.strip(string.punctuation)  # Удаляем знаки препинания из слова, используя string.punctuation.
            if word:  # Проверяем, что слово не пустое после удаления знаков препинания.
                if word in word_count:
                    word_count[word] += 1  # Увеличиваем счетчик для уже встреченных слов.
                else:
                    word_count[word] = 1  # Добавляем новое слово в словарь с начальным счетчиком 1.

                if word_count[word] > max_count:
                    max_count = word_count[word]  # Обновляем максимальное количество повторений и самое частое слово.

    total_words = sum(word_count.values())  # Считаем общее количество слов в тексте.
    return total_words, most_common_word, max_count  # Возвращаем результаты анализа.

if __name__ == "__main__":
    filename = "statia.txt"  # Указываем имя файла для анализа.
    total_words, most_common_word, max_count = count_words(filename)  # Вызываем функцию count_words.

    # Выводим результаты анализа на экран.
    print("Всего слов в файле:", total_words)
    print("Самое часто встречающееся слово:", most_common_word)
    print("Количество повторений:", max_count)


## Самостоятельная работа #2
У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет
```python
import os

def enter_expense():  # Функция для ввода информации о расходах
    expense_date = input("Введите дату расхода (например, 2023-10-21): ")
    expense_description = input("Введите описание расхода: ")
    expense_amount = float(input("Введите сумму расхода: "))
    return {
        "Дата": expense_date,
        "Описание": expense_description,
        "Сумма": expense_amount
    }
def save_expense(expense, filename):  # Функция для сохранения информации о расходах в файл
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{expense['Дата']} - {expense['Описание']} - {expense['Сумма']} руб.\n")
def display_expenses(filename): # Функция для вывода всех расходов из файла
    if not os.path.exists(filename):
        print("Файл с расходами пуст.")
        return

    with open(filename, "r", encoding="utf-8") as file:
        expenses = file.readlines()
        if not expenses:
            print("Файл с расходами пуст.")
        else:
            print("Список расходов:")
            for expense in expenses:
                print(expense, end="")

if __name__ == "__main__":
    expense_file = "zadanie2.txt"  # Имя файла для хранения расходов

    while True:
        print("\nВыберите действие:")
        print("1. Ввести новый расход")
        print("2. Вывести список всех расходов")
        print("3. Выход")
        choice = input("Введите номер действия: ")
        if choice == "1":
            expense = enter_expense()
            save_expense(expense, expense_file)
            print("Расход успешно добавлен.")
        elif choice == "2":
            display_expenses(expense_file)
        elif choice == "3":
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/923573ff-681e-4e1c-93e1-3187afeeabc5)
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/87c771f8-0558-477b-9d18-48cdd6b3b00c)
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/23ca488d-7840-4a73-87cb-c35102fb0288)
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/8fed4e7b-659a-4f92-83f5-d0691e75a8f2)



## Выводы
import os  # Импортируем модуль os для работы с файлами и операционной системой.

def enter_expense():  # Объявляем функцию enter_expense для ввода информации о расходах.
    expense_date = input("Введите дату расхода (например, 2023-10-21): ")  # Запрашиваем у пользователя ввод даты расхода.
    expense_description = input("Введите описание расхода: ")  # Запрашиваем у пользователя ввод описания расхода.
    expense_amount = float(input("Введите сумму расхода: "))  # Запрашиваем у пользователя ввод суммы расхода и преобразуем её в число.
    return {  # Возвращаем словарь, содержащий введенные пользователем данные.
        "Дата": expense_date,
        "Описание": expense_description,
        "Сумма": expense_amount
    }

def save_expense(expense, filename):  # Объявляем функцию save_expense для сохранения информации о расходах в файл.
    with open(filename, "a", encoding="utf-8") as file:  # Открываем файл для записи (режим "a") с указанной кодировкой.
        file.write(f"{expense['Дата']} - {expense['Описание']} - {expense['Сумма']} руб.\n")  # Записываем информацию о расходе в файл.

def display_expenses(filename):  # Объявляем функцию display_expenses для вывода всех расходов из файла.
    if not os.path.exists(filename):  # Проверяем, существует ли файл с указанным именем.
        print("Файл с расходами пуст.")  # Если файл не существует, выводим сообщение об отсутствии данных и завершаем функцию.
        return

    with open(filename, "r", encoding="utf-8") as file:  # Открываем файл для чтения с указанной кодировкой.
        expenses = file.readlines()  # Читаем все строки из файла и сохраняем их в список expenses.

        if not expenses:  # Проверяем, пуст ли список расходов.
            print("Файл с расходами пуст.")  # Если список пуст, выводим сообщение об отсутствии данных.
        else:
            print("Список расходов:")  # Если есть данные, выводим заголовок "Список расходов".
            for expense in expenses:  # Перебираем каждый элемент списка expenses (каждую строку) и выводим его на экран.
                print(expense, end="")  # Выводим расход и не переходим на новую строку.

if __name__ == "__main__":
    expense_file = "zadanie2.txt"  # Указываем имя файла, в котором будут храниться данные о расходах.

    while True:
        print("\nВыберите действие:")
        print("1. Ввести новый расход")
        print("2. Вывести список всех расходов")
        print("3. Выход")
        choice = input("Введите номер действия: ")  # Запрашиваем у пользователя выбор действия.

        if choice == "1":  # Если пользователь выбрал действие 1.
            expense = enter_expense()  # Запускаем функцию для ввода информации о расходе.
            save_expense(expense, expense_file)  # Сохраняем введенный расход в файл.
            print("Расход успешно добавлен.")  # Выводим сообщение об успешном добавлении расхода.
        elif choice == "2":  # Если пользователь выбрал действие 2.
            display_expenses(expense_file)  # Запускаем функцию для вывода всех расходов из файла.
        elif choice == "3":  # Если пользователь выбрал действие 3.
            break  # Выходим из цикла и завершаем программу.
        else:
            print("Неверный выбор. Попробуйте снова.")  # Если выбор пользователя не соответствует допустимым вариантам, выводим сообщение об ошибке.


## Самостоятельная работа #3
Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. • Текст в файле: Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. • Ожидаемый результат: Input file contains: 108 letters 20 words 4 lines
```python
with open('test.txt', 'r') as file:
    content = file.read()

letter_count = sum(1 for char in content if char.isalpha())
word_count = len(content.split())
line_count = content.count('\n') + 1

print(f'Файл содержит {letter_count} букв {word_count} слов {line_count} строк')
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/fa4ae863-cb9a-44b6-9278-68cc7a42d69f)
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/712306bc-71c9-4353-a2e5-1232602b4544)



## Выводы
Открываем файл 'test.txt' в режиме чтения ('r') с использованием контекстного менеджера with. Это обеспечивает автоматическое закрытие файла после его использования, что уменьшает вероятность ошибок.
Читаем содержимое файла и сохраняем его в переменной content.
Вычисляем количество букв в тексте, используя генераторное выражение. Мы проходим по каждому символу char в content и проверяем, является ли символ буквой с помощью метода char.isalpha(). Каждый раз, когда условие выполняется, мы увеличиваем счетчик на 1.
Вычисляем количество слов в тексте, разбивая content на слова с помощью метода split() и затем подсчитывая количество полученных слов с помощью len()
Вычисляем количество строк в тексте, считая количество символов новой строки ('\n') и добавляя 1, так как первая строка не имеет символа новой строки.

## Самостоятельная работа #4
Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в сере
```python
# Создаем файл с вариациями запрещенных слов
banned_words = ['hello', 'email', 'python', 'the', 'exam', 'wor', 'is']

variations = set()
for word in banned_words:
    variations.add(word)
    variations.add(word.lower())
    variations.add(word.upper())
    variations.add(word.capitalize())

with open('banned_words.txt', 'w') as file:
    for word in variations:
        file.write(word + '\n')

# Загружаем список запрещенных слов из файла
with open('banned_words.txt', 'r') as banned_file:
    banned_words = [line.strip() for line in banned_file]

# Получаем предложение от пользователя
sentence = input("Введите предложение: ")

# Функция для замены запрещенных слов на звездочки
def replace_banned(word):
    for banned_word in banned_words:
        word_lower = word.lower()
        banned_lower = banned_word.lower()
        word = word.replace(banned_word, '*' * len(banned_word))
        word = word.replace(banned_lower, '*' * len(banned_word))
    return word

# Заменяем слова в предложении
new_sentence = ' '.join(replace_banned(word) for word in sentence.split())

# Выводим предложение с заменой запрещенных слов
print(new_sentence)
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/3a449b3e-55b2-43bd-9bb4-05add8b417fd)


## Выводы
# Создаем файл с вариациями запрещенных слов
banned_words = ['hello', 'email', 'python', 'the', 'exam', 'wor', 'is']

variations = set()
for word in banned_words:
    variations.add(word)
    variations.add(word.lower())
    variations.add(word.upper())
    variations.add(word.capitalize())

with open('banned_words.txt', 'w') as file:
    for word in variations:
        file.write(word + '\n')

# Загружаем список запрещенных слов из файла
with open('banned_words.txt', 'r') as banned_file:
    banned_words = [line.strip() for line in banned_file]

# Получаем предложение от пользователя
sentence = input("Введите предложение: ")

# Функция для замены запрещенных слов на звездочки
def replace_banned(word):
    for banned_word in banned_words:
        word_lower = word.lower()
        banned_lower = banned_word.lower()
        word = word.replace(banned_word, '*' * len(banned_word))
        word = word.replace(banned_lower, '*' * len(banned_word))
    return word

# Заменяем слова в предложении
new_sentence = ' '.join(replace_banned(word) for word in sentence.split())

# Выводим предложение с заменой запрещенных слов
print(new_sentence)

## Общие выводы по теме
Работа с файлами полезный аспект изучения Python
