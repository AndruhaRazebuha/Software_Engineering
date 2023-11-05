# Создаем файл с вариациями запрещенных слов
banned_words = ['hello', 'email', 'python', 'the', 'exam', 'wor', 'is']

variations = set()
for word in banned_words:
    variations.add(word)
    variations.add(word.lower())
    variations.add(word.upper())
    variations.add(word.capitalize())

with open('banned_words.txt', 'w') as file:
    for word in variations:
        file.write(word + '\n')

# Загружаем список запрещенных слов из файла
with open('banned_words.txt', 'r') as banned_file:
    banned_words = [line.strip() for line in banned_file]

# Получаем предложение от пользователя
sentence = input("Введите предложение: ")

# Функция для замены запрещенных слов на звездочки
def replace_banned(word):
    for banned_word in banned_words:
        word_lower = word.lower()
        banned_lower = banned_word.lower()
        word = word.replace(banned_word, '*' * len(banned_word))
        word = word.replace(banned_lower, '*' * len(banned_word))
    return word

# Заменяем слова в предложении
new_sentence = ' '.join(replace_banned(word) for word in sentence.split())

# Выводим предложение с заменой запрещенных слов
print(new_sentence)
