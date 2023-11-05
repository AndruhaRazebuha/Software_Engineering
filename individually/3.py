with open('test.txt', 'r') as file:
    content = file.read()

letter_count = sum(1 for char in content if char.isalpha())
word_count = len(content.split())
line_count = content.count('\n') + 1

print(f'Файл содержит {letter_count} букв {word_count} слов {line_count} строк')