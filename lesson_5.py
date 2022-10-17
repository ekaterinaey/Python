# Задание №1
# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. 
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?


from random import randint


player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')

value = 121
counter1 = 0 

counter2 = 0


draw = randint(0, 2)

if draw:
    print(f"Первый ходит игрок {player1}")
else:
    print(f"Первый ходит игрок {player2}")

def take_sweets(player):
    s = int(input(f"{player}, Введите количество конфет, которое хотите взять от 1 до 28 шт: "))
    return s

def summarize(player, sweets, counter, value):
    print(f"Ходил игрок {player}, взял {sweets} конфет. Его общее количество конфет {counter}, осталось всего {value} конфет")

while value > 28:
    if draw:
        sweets = take_sweets(player1)
        counter1 += sweets
        value -= sweets
        draw = False
        summarize(player1, sweets, counter1, value)
    else:
        sweets = take_sweets(player2)
        counter2 += sweets
        value -= sweets
        draw = True
        summarize(player2, sweets, counter2, value)

if draw:
    print(f"Выиграл {player1}, его общее количество конфет {counter1}")
else:
    print(f"Выиграл {player2}, его общее количество конфет {counter2}")


# a) Добавьте игру против бота


player3 = input('Введите  Ваше имя: ')
playerBot = 'Чарли-Бот'

print(f"Привет {player3}, меня зовут {playerBot}, сегодня мы будем играть")

value2 = 121
counter3 = 0 
counterBot = 0 

draw2 = randint(0, 2)

if draw2:
    print(f"Первый ходит игрок {player3}")
else:
    print(f"Первый ходит игрок {playerBot}")


def take_sweets2(player): 
     s = int(input(f"{player}, Введите количество конфет, которое хотите взять от 1 до 28 шт: "))
     return s

def take_sweets3(player):
    s = int(randint(1, 28))
    print(f"{player} берет {s} штук")
    return s


def summarize2(player, sweets, counter, value):
    print(f"Ходил игрок {player}, взял {sweets} конфет. Его общее количество конфет {counter}, осталось всего {value} конфет")


while value2 > 28:
    if draw2:
        sweets_2 = take_sweets2(player3)
        counter3 += sweets_2
        value2 -= sweets_2
        draw2 = False
        summarize2(player3, sweets_2, counter3, value2)
    else:
        sweets_2 = take_sweets3(playerBot)
        counterBot += sweets_2
        value2 -= sweets_2
        draw2 = True
        summarize2(playerBot, sweets_2, counterBot, value2)

if draw2:
    print(f"Выиграл {player3}, его общее количество конфет {counter3}")
else:
    print(f"Выиграл {playerBot}, его общее количество конфет {counterBot}")
    




