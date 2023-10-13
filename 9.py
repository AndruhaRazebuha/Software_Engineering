"""
Создайте переменную message со значением "Hello, World!".
Далее, преобразуйте это сообщение в нижний регистр и вставьте слово "amazing" между словами "Hello" и "World".
Выведите результат.
"""
message = "Hello, World!"
new_message = message.lower().replace("hello", "hello amazing")
print(new_message)