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
