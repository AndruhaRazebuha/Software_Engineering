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
