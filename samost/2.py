import random

def dice():
    score = random.randint(1, 6)
    print(score)
    if score == 5 or score == 6:
        print("Вы победили!")
    elif score == 3 or score == 4:
        print("Переброс кубика...")
        dice()
    elif score == 1 or score == 2:
        print("Вы проиграли! :(")
if __name__ == '__main__':
    dice()