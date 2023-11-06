class Tomato:
    states = {0: "отсутствует", 1: "цветение", 2: "зеленый", 3: "красный"}

    def __init__(self, index):
        self._index = index
        self._state = 1  # Начальное состояние - цветение.

    def grow(self):
        if self._state < 3:
            self._state += 1  # Переход к следующей стадии созревания.

    def is_ripe(self):
        return self._state == 3  # Проверка, созрел ли помидор.

class TomatoBush:
    def __init__(self, num_of_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(1, num_of_tomatoes + 1)]  # Создаем список помидоров, используя класс Tomato.

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()  # Рост всех помидоров на кусте.

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)  # Проверяем, все ли помидоры на кусте созрели.

    def give_away_all(self):
        self.tomatoes = [tomato for tomato in self.tomatoes if not tomato.is_ripe()]  # Очищаем список помидоров после сбора урожая.

class Gardener:
    def __init__(self, name, plant):
        self.name = name  # Создаем динамическое свойство name и устанавливаем его в значение, переданное параметром (публичное).
        self._plant = plant  # Создаем динамическое свойство _plant и устанавливаем его в значение, переданное параметром (приватное).

    def work(self):
        self._plant.grow_all()  # Садовник ухаживает за растением, вызывая метод grow_all у растения.

    def harvest(self):
        if self._plant.all_are_ripe():  # Если все помидоры на растении созрели.
            harvested_tomatoes = self._plant.tomatoes  # Собираем урожай.
            self._plant.give_away_all()  # Очищаем список помидоров после сбора урожая.
            return harvested_tomatoes  # Возвращаем собранные помидоры.
        else:
            print("Не все помидоры созрели. Продолжайте ухаживать за ними.")  # Выводим предупреждение.

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: ...")  # Выводим справку по садоводству.

# Тесты
Gardener.knowledge_base()  # Вызываем справку по садоводству

bush = TomatoBush(5)  # Создаем куст с пятью помидорами
gardener = Gardener("Иван", bush)  # Создаем садовника

for _ in range(6):
    gardener.work()  # Садовник ухаживает за кустом

unripe_tomatoes = gardener.harvest()  # Попытка собрать урожай до созревания

for _ in range(2):
    gardener.work()  # Садовник продолжает ухаживать за кустом

ripe_tomatoes = gardener.harvest()  # Сбор урожая после созревания

print(f"Осталось {len(bush.tomatoes)} незрелых помидоров.")  # Выводим количество оставшихся незрелых помидоров.
