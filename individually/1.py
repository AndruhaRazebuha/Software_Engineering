import string
def count_words(filename):
    word_count = {}
    most_common_word = ""
    max_count = 0
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = text.split()
        for word in words:
            word = word.strip(string.punctuation)  # Удаляем знаки препинания из слова
            if word:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
                if word_count[word] > max_count:
                    max_count = word_count[word]
                    most_common_word = word
    total_words = sum(word_count.values())
    return total_words, most_common_word, max_count
if __name__ == "__main__":
    filename = "statia.txt"
    total_words, most_common_word, max_count = count_words(filename)

    print("Всего слов в файле:", total_words)
    print("Самое часто встречающееся слово:", most_common_word)
    print("Количество повторений:", max_count)