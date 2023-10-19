sentence = str(input('Введите ваше предложение на английском языке: '))
print(f'Ваше предложение на английском:  {sentence}')
len = len(sentence)
print("Длина предложения", len)
sentencelower = sentence.lower()
print("Предложение на нижнем регистре", sentencelower)
values = 'aeiouAEIOU'
count = 0
for vowel in sentence:
    if values in sentence:
        count +=1
print("Количество этих букв", count)
sentenceswitch = sentencelower.replace("ugly", "beaty")
print("Измененное предложение", sentenceswitch)
if sentence.startswith("The"):
    print("Предложение начинается с The")
elif sentence.endswith("end."):
    print("Предложение заканчивается с end.")
else:
    print("Предложение не начинается с The и не заканчивается на end.")