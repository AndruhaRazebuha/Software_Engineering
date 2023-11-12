# Тема 9. Концепции и принципы ООП
Отчет по Теме #9 выполнил:
- Постовалов Андрей Георгиевич
- ПИЭ-21-2

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | 
| Задание 4 | + | 
| Задание 5 | + | 
| Задание 6 | + | 
| Задание 7 | + | 
| Задание 8 | + | 
| Задание 9 | + | 
| Задание 10 | + | 

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная работа №1
Есть Помидор со следующими характеристиками: • Индекс • Стадия созревания (стадии: отсутствует, цветение, зеленый, красный) Помидор может: • Расти (переходить на следующую стадию созревания) • Предоставлять информацию о своей зрелости Есть Куст с помидорами, который: • Содержит список томатов, которые на нем растут А также может: • Расти вместе с томатами • Предоставлять информацию о зрелости всех

```python
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
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/1c5499ad-4b18-4c25-9d4e-f53c5cadfce6)


## Выводы
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
 Создание куста с пятью помидорами
bush = TomatoBush(5)
 Создание садовника
gardener = Gardener("Иван", bush)
 Уход за кустом с помидорами и сбор урожая
for day in range(7):
    gardener.take_care()
    if bush.all_are_ripe():
        harvest = gardener.harvest()  # Если все помидоры созрели, собираем урожай.
        print(f"Садовник {gardener.name} собрал {len(harvest)} спелых помидоров.")
print(f"Осталось {len(bush.tomatoes)} незрелых помидоров.")


## Самостоятельная работа №2
Класс Tomato: 1) Создайте класс Tomato 2) Создайте статическое свойство states, которое будет содержать все стадии созревания помидора 3) Создайте метод __init__(), внутри которого будут определены два динамических свойства: _index (передается параметром) и _state
(принимает первое значение из словаря states). После написания этого блока кода в комментарии к нему укажите какими являются эти два свойства 4) Создайте метод grow(), который будет переводить томат на следующую стадию созревания 5) Создайте метод is_ripe(), который будет проверять, что томат созрел
Класс TomatoBush: 1) Создайте класс TomatoBush 2) Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes 3) Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания 4) Создайте
Класс Gardener: 1) Создайте класс Gardener 2) Создайте метод __init__(), внутри которого будут определены два динамических свойства: name (передается параметром, является публичным) и _plant (принимает объект класса TomatoBush). После написания этого блока кода в комментарии к нему укажите какими являются эти два свойства 3) Создайте метод work(), который заставляет садовника работать, что позволяе
Тесты: 1) Вызовите справку по садоводству 2) Создайте объекты классов TomatoBush и Gardener 3) Используя объект класса Gardener, поухаживайте за кустом с помидорами 4) Попробуйте собрать урожай, когда томаты еще не дозрели. Продолжайте ухаживать за ними
5) Соберите урожай Результатом работы вашей программы будет листинг кода с подробными комментариями и скриншоты выполенния всех тестов.

```python
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
```

### Результат.
![image](https://github.com/AndruhaRazebuha/Software_Engineering/assets/133500965/867b8acd-e856-40d0-bd33-8f80e6ae2b20)


## Выводы
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







## Общие выводы по теме
Концепции и принципы ООП важны в программной инженерии

