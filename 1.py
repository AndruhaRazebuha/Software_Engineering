class Tomato:
    def __init__(self, index):
        self.index = index
        self.ripeness = 0  # Инициализация помидора с индексом и стадией созревания (отсутствует).

    def grow(self):
        if self.ripeness < 3:
            self.ripeness += 1  # Переход к следующей стадии созревания.

    def is_ripe(self):
        return self.ripeness == 3  # Проверка, созрел ли помидор.

class TomatoBush:
    def __init__(self, num_of_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_of_tomatoes + 1)]  # Создание куста с заданным количеством помидоров.

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()  # Рост всех помидоров на кусте.

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)  # Проверка, все ли помидоры на кусте созрели.

    def harvest(self):
        ripe_tomatoes = [tomato for tomato in self.tomatoes if tomato.is_ripe()]  # Поиск спелых помидоров.
        for tomato in ripe_tomatoes:
            self.tomatoes.remove(tomato)  # Уборка спелых помидоров.
        return ripe_tomatoes  # Возврат собранного урожая.

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.plant = plant  # Инициализация садовника с именем и растением, за которым он ухаживает.

    def take_care(self):
        self.plant.grow_all()  # Уход за растением (рост всех помидоров).

    def harvest(self):
        return self.plant.harvest()  # Сбор урожая с растения.

# Создание куста с пятью помидорами
bush = TomatoBush(5)

# Создание садовника
gardener = Gardener("Иван", bush)

# Уход за кустом с помидорами и сбор урожая
for day in range(7):
    gardener.take_care()
    if bush.all_are_ripe():
        harvest = gardener.harvest()  # Если все помидоры созрели, собираем урожай.
        print(f"Садовник {gardener.name} собрал {len(harvest)} спелых помидоров.")

print(f"Осталось {len(bush.tomatoes)} незрелых помидоров.")
