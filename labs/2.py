# Импортируем функцию pprint из модуля pprint
from pprint import pprint

# Создаем начальный словарь my_dict с одним элементом
my_dict = {'first': 'so easy'}

# Определяем функцию dict_maker, которая принимает и обновляет словарь my_dict с новыми данными
def dict_maker(**kwargs):
    # Используем **kwargs для передачи именованных аргументов в виде словаря
    my_dict.update(**kwargs)

# Вызываем функцию dict_maker и обновляем my_dict с новыми данными, передавая их в виде именованных аргументов
dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name='Михаил', age=31, weight=70, eyes_color='blue')

# Используем pprint для красивой печати словаря my_dict
pprint(my_dict)
