# Тема 7. Введение в ООП
Отчет по Теме #8 выполнил:
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
 Создаем объекты класса Person
person1 = Person("Андрей", 20, "студент")
person2 = Person("Иван", 25, "инженер")
 Вызываем метод introduce для объекта person1
person1.introduce()
 Вызываем метод greet для объекта person1, поздоровавшись с person2
person1.greet(person2)
class Student(Person):
    def __init__(self, name, age, occupation, student_id):
        super().__init__(name, age, occupation)  # Вызываем конструктор родительского класса
        self.student_id = student_id
    def study(self, subject):
        print(f"{self.name} с номером студента {self.student_id} учит {subject}.")
 Создаем объект класса Student
student1 = Student("Елена", 22, "студент", "12345")
 Вызываем метод introduce для объекта student1 (наследован от класса Person)
student1.introduce()
 Вызываем метод study для объекта student1
student1.study("математику")



## Самостоятельная работа №4
Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях.
Результатом выполнения задания будет листинг кода и получившийся вывод консоли

```python
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.__age = age  # Сделаем атрибут age приватным с использованием двойного подчеркивания
        self.occupation = occupation

    # Геттер для получения значения атрибута age
    def get_age(self):
        return self.__age

    # Сеттер для установки значения атрибута age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным.")

    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.get_age()} лет. Я работаю как {self.occupation}.")

# Создаем объект класса Person
person1 = Person("Анна", 30, "врач")

# Попробуем установить возраст через сеттер
person1.set_age(35)

# Вызываем метод introduce для объекта person1
person1.introduce()
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/cef08cb3-7f75-40a3-b808-5c7cd8d8b8a7)



## Выводы
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.__age = age   Сделаем атрибут age приватным с использованием двойного подчеркивания
        self.occupation = occupation
     Геттер для получения значения атрибута age
    def get_age(self):
        return self.__age
     Сеттер для установки значения атрибута age
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Возраст не может быть отрицательным.")
    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.get_age()} лет. Я работаю как {self.occupation}.")
 Создаем объект класса Person
person1 = Person("Анна", 30, "врач")
 Попробуем установить возраст через сеттер
person1.set_age(35)
 Вызываем метод introduce для объекта person1
person1.introduce()



## Самостоятельная работа №5
Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. 
Результатом выполнения задания будет листинг кода и получившийся вывод консоли
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Гав-гав!"


class Cat(Animal):
    def sound(self):
        return "Мяу!"


# Создаем список животных
animals = [Dog("Барон"), Cat("Мурзик")]

# Перебираем список животных и вызываем метод sound для каждого
for animal in animals:
    print(f"{animal.name}: {animal.sound()}")
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/4c7a1e6c-49f8-4c59-a306-fea2968e4fe0)

## Выводы
class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Гав-гав!"
class Cat(Animal):
    def sound(self):
        return "Мяу!"
 Создаем список животных
animals = [Dog("Барон"), Cat("Мурзик")]
 Перебираем список животных и вызываем метод sound для каждого
for animal in animals:
    print(f"{animal.name}: {animal.sound()}")




## Общие выводы по теме
ООП важный аспект программирования
