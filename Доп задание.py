import random
import os

def count_runs():
    filename = "counter.txt"
    
    try:
        with open(filename, 'r') as f:
            count = int(f.read())
    except (FileNotFoundError, ValueError):
        count = 0
    
    count += 1
    
    with open(filename, 'w') as f:
        f.write(str(count))
    
    return count

print(f"Программа запущена {count_runs()} раз")



phrases = [
    "Начни — и состояние потока само тебя захватит",
    "30 минут могут стать самым крутым временем за день",
    "Ты создаёшь то, чем потом будешь гордиться",
    "Каждый маленький шаг уже является победой",
    "Сегодня отличный день, чтобы сделать что-то классное",
    "Включи любимую музыку и позволь идеям течь",
    "Представь, какой огонь ты зажжёшь в коде сегодня"
]
def get_advice():
    "Возвращает мотивирующую и вдохновляющую фразу"
    return random.choice(phrases)

def main():
    print("Мотивационный помощник")
    user = input("Как ты себя чувствуешь? (устал(а)/норм/плохо/выгорел(а)/прекрасно/нейтрально): ").lower().strip()
    if "устал" in user:
        print("Совет:", get_advice())
    elif user == "плохо":
        print("Можно сделать короткий перерыв и вернуться со свежим взглядом")
    elif "выгорел" in user:
        print("Сегодня достаточно поработать около часа")
    elif 'прекрасно' in user:
        print('Отлично, значит ты все делешь правильно')
    elif 'нейтрально' in user:
        print('наверное тебе нужен маленький перерыв')
    else:
        print("Супер! Продолжаем в своём ритме")
if __name__ == "__main__":
    main()






