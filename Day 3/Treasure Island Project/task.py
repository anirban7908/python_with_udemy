print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
player_name = input("Enter your name: ")

direction = input("Which direction will you go? Left(L) or Right(R)?")

if direction.upper() == 'L':
    activity = input("Which activity will you want to do? Swim(S), Run(R), Wait(W)?")
    if activity.upper() == 'W':
        door_selected = input("Choose your door. Red(R), Yellow(Y), Blue(B)")
        if door_selected.upper() == "R":
            print("Burned by fire. Game Over.")
        elif door_selected.upper() == "B":
            print("Eaten by beasts. Game Over.")
        elif door_selected.upper() == "Y":
            print(f"Congratulations {player_name} You Win!")
    else:
        print("Attacked by trout. Game Over.")
elif direction.upper() == "R":
    print('Fall into a hole. Game Over.')
else:
    print('Invalid input. Choose either L or R')