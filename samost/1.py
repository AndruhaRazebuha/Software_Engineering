class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")


person1 = Person("Андрей", 20) # Создаем объект класса Person
person1.introduce() # Вызываем метод introduce для объекта person1
