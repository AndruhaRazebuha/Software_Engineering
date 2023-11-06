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
