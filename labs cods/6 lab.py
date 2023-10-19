string = 'Привет всем изучающим Python!'
value = input()
for i in string:
    if value in string: # Косяк здесь, надо не i == value, а проверить же букву в массиве, значит value(вводимая нами буква) in string(в массиве если она)
        index = string.find(value)
        print(f"Буква '{value}' есть в строке под {index} индексом")
        break
    else:
        print(f"Буква '{value}' нет в строке")
        break