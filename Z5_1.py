# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
import random




def player ():
    candies = 45
    maxx = 28 
    ig = random.randint(1, 2)
    name1 = 'Первый игрок' 
    name2 = 'Второй игрок'
    
    if ig == 1:
        first = name1
        second = name2
    else:
        first = name2
        second = name1
    print (f'{first} первым берет конфеты')
       
    count = 0
    while candies > 0:
        if count == 0:
            move = int(input(f"{first} сколько вы возьмете конфет = "))
            if move > candies or move > maxx:
                move = int(input(f'{first} это слишком много, попробуй еще раз = '))
            candies = candies - move
        if candies > 0:
            print (f'Осталось {candies} конфет')
            count = 1
        else:
            print ('Конфеты кончились')

        if count == 1:
            move = int(input(f' {second} сколько вы возьмете конфет = '))
            if move > candies or move > maxx:
                move = int(input(f'{second} это слишком много, попробуй еще раз = '))
            candies = candies - move
        if candies > 0:
            print (f'Осталось {candies} конфет')
            count = 0
        else:
            print ('Конфеты кончились')
    if count == 0:
        print(f'{first} вы победили. Все конфеты ваши!')
    else:
        print(f'{second} вы победили. Все конфеты ваши!')

        

player  ()

t= 'dfjjjgj'
t.upper()