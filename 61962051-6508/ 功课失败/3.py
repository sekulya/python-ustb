import turtle
import random
#players 1's shape and color
player_one = turtle.Turtle()
player_one.color("red")
player_one.shape("turtle")
player_one.penup()
#player 1's starting position
player_one.goto(-180,100)
#player 2's shape and colore
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
#player 2's starting position
player_two.goto(-180,-100)
#players' finishing point represented by dots that they draw themselves and get back to the starting point
player_one.goto(250,100)
player_one.pendown()
player_one.dot(35)
player_one.penup()
player_one.goto(-180,100)
player_two.goto(250,-100)
player_two.pendown()
player_two.dot(35)
player_two.penup()
player_two.goto(-180,-100)
#dice in ascending numbers
dice = [1,2,3,4,5,6]
for i in range(20):
    if player_one.pos() >= (250,100):
            print("玩家一获胜！")
            break
    elif player_two.pos() >= (250,-100):
            print("玩家两次获胜！")
            break
    else:
#to play the game palyer have to roll a die by clicking "Enter"
            player_one_turn = input("按“ Enter”来掷骰子")
            dice_outcome = random.choice(dice)
            #system to randomly select a number from it, the number that is selected will be considered as the output of the dice
            print("掷骰子的结果是：")
            print(dice_outcome)
            print("步骤数将是：")
            print(20*dice_outcome)
            player_one.fd(20*dice_outcome)
            player_two_turn = input("按“ Enter”来掷骰子")
            dice_outcome = random.choice(dice)
            print("掷骰子的结果是：")
            print(dice_outcome)
            print("步骤数将是：")
            print(20*dice_outcome)
            player_two.fd(20*dice_outcome)

