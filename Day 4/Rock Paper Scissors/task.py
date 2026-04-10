import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]
# print(machine_list)
while True:
    user_input = int(input("Please choose 1 for Rock, 2 for Paper and 3 for Scissors and 0 for exit: "))
    if user_input == 0:
        exit()
    machine_input = random.randint(0, (len(game_image) - 1))

    if user_input<=2  and user_input >=0:
        print(game_image[user_input])

    print('Computer choose:')
    print(game_image[machine_input])

    if user_input >=4 or user_input < 0:
        print("Please select a valid option. You Loose")
    elif user_input == 0 and machine_input == 2:
        print('You Win')
    elif machine_input == 0 and user_input == 2:
        print('You loose')
    elif user_input > machine_input:
        print('You Win')
    elif machine_input > user_input:
        print('You Loose')
    elif machine_input == user_input:
        print('Game draw')


