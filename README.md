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

## Самостоятельная работа №1
Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. 
Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")


person1 = Person("Андрей", 20) # Создаем объект класса Person
person1.introduce() # Вызываем метод introduce для объекта person1
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/31f89a9a-6a7b-4b22-88ab-9d58a3175318)



## Выводы
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")


person1 = Person("Андрей", 20) # Создаем объект класса Person
person1.introduce() # Вызываем метод introduce для объекта person1



## Самостоятельная работа №2
Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. 
Результатом выполнения задания будет листинг кода и получившийся вывод консоли

```python
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет. Я работаю как {self.occupation}.")
    def greet(self, other_person):
        print(f"Привет, {other_person.name}! Я {self.name}, рад видеть тебя.")
# Создаем объекты класса Person
person1 = Person("Андрей", 20, "студент")
person2 = Person("Иван", 25, "инженер")
# Вызываем метод introduce для объекта person1
person1.introduce()
# Вызываем метод greet для объекта person1, поздоровавшись с person2
person1.greet(person2)
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/73fc757e-d85f-4210-8c8a-9d8d7674e627)



## Выводы
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет. Я работаю как {self.occupation}.")
    def greet(self, other_person):
        print(f"Привет, {other_person.name}! Я {self.name}, рад видеть тебя.")
 Создаем объекты класса Person
person1 = Person("Андрей", 20, "студент")
person2 = Person("Иван", 25, "инженер")
 Вызываем метод introduce для объекта person1
person1.introduce()
 Вызываем метод greet для объекта person1, поздоровавшись с person2
person1.greet(person2)


## Самостоятельная работа №3
Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях.
Результатом выполнения задания будет листинг кода и получившийся вывод консоли

```python
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет. Я работаю как {self.occupation}.")

    def greet(self, other_person):
        print(f"Привет, {other_person.name}! Я {self.name}, рад видеть тебя.")
# Создаем объекты класса Person
person1 = Person("Андрей", 20, "студент")
person2 = Person("Иван", 25, "инженер")
# Вызываем метод introduce для объекта person1
person1.introduce()
# Вызываем метод greet для объекта person1, поздоровавшись с person2
person1.greet(person2)
class Student(Person):
    def __init__(self, name, age, occupation, student_id):
        super().__init__(name, age, occupation)  # Вызываем конструктор родительского класса
        self.student_id = student_id
    def study(self, subject):
        print(f"{self.name} с номером студента {self.student_id} учит {subject}.")
# Создаем объект класса Student
student1 = Student("Елена", 22, "студент", "12345")
# Вызываем метод introduce для объекта student1 (наследован от класса Person)
student1.introduce()
# Вызываем метод study для объекта student1
student1.study("математику")
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/829013e9-1d2f-4d5b-a7d3-535fcfd43bd9)


## Выводы
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет. Я работаю как {self.occupation}.")

    def greet(self, other_person):
        print(f"Привет, {other_person.name}! Я {self.name}, рад видеть тебя.")
# Создаем объекты класса Person
person1 = Person("Андрей", 20, "студент")
person2 = Person("Иван", 25, "инженер")
# Вызываем метод introduce для объекта person1
person1.introduce()
# Вызываем метод greet для объекта person1, поздоровавшись с person2
person1.greet(person2)
class Student(Person):
    def __init__(self, name, age, occupation, student_id):
        super().__init__(name, age, occupation)  # Вызываем конструктор родительского класса
        self.student_id = student_id
    def study(self, subject):
        print(f"{self.name} с номером студента {self.student_id} учит {subject}.")
# Создаем объект класса Student
student1 = Student("Елена", 22, "студент", "12345")
# Вызываем метод introduce для объекта student1 (наследован от класса Person)
student1.introduce()
# Вызываем метод study для объекта student1
student1.study("математику")





## Общие выводы по теме
Работа с файлами полезный аспект изучения Python
