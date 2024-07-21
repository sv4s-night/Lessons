"""9. Библиотека random """
import random

"""======================================= Задача ================================================
Напишите программу, которая симулирует игру в кости между двумя игроками

Программа должна:
1. Бросить кости для каждого игрока (2 шестигранных кубика для каждого игрока)
2. Сложить выпавшие значения для каждого игрока
3. Объявить победителя, основываясь на сумме выпавших значений.
Если сумма равна, объявить ничью
================================================================================================="""


def throw_dice():
    return random.randint(1,6), random.randint(1, 6)



def play_game():
    player_1_dice_1, player_1_dice_2 = throw_dice()
    sum_player_1 = player_1_dice_1 + player_1_dice_2
    print(f"Игрок 1 выбросил кости ({player_1_dice_1}, {player_1_dice_2}) на сумму {sum_player_1}")

    player_2_dice_1, player_2_dice_2 = throw_dice()
    sum_player_2 = player_2_dice_1 + player_2_dice_2
    print(f"Игрок 2 выбросил кости ({player_2_dice_1}, {player_2_dice_2}) на сумму {sum_player_2}")

    if sum_player_1 > sum_player_2:
        print("Победил игрок 1")
    elif sum_player_2 > sum_player_1:
        print("Победил игрок 2")
    else:
        print("Ничья")




play_game()