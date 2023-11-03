# Запрашиваем у пользователя ввод номера кабинета и сохраняем его в переменной request
request = int(input('Введите номер кабинета: '))

# Создаем словарь dictionary, в котором ключами являются номера кабинетов, а значениями являются словари с данными о доступе
dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False},
}

# Используем метод get для получения значения из словаря dictionary по ключу request и сохраняем его в переменной response
response = dictionary.get(request)

# Если response равно None (то есть введенный номер кабинета отсутствует в словаре), то
# используем словарь, соответствующий ключу None, как значение response
if not response:
    response = dictionary[None]

# Извлекаем ключ 'key' и значение 'access' из словаря response
key = response.get('key')
access = response.get('access')

# Выводим значение key и access
print(key, access)
