import random
from art import logo

def change_difficulty():
    difficulty = input("Choose difficulty: Easy, Hard: ").lower()

    if difficulty == 'easy':
        attempts_remaining = 10
    elif difficulty == 'hard':
        attempts_remaining = 5
    else:
        print("Invalid choice.")
        return False
    return attempts_remaining

def start_game(attempts_remaining):
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    guessed_number = random.randint(1, 100)

    while attempts_remaining > 0:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")

        user_guess = int(input("Make a guess: "))

        if user_guess == guessed_number:
            print(f"You got it! The answer was {guessed_number}")
            return

        attempts_remaining -= 1

        if attempts_remaining == 0:
            print("You've run out of guesses.")
            return

        if user_guess > guessed_number:
            print("Too high.\nGuess again.")
        else:
            print("Too low.\nGuess again.")
while True:
    attempts = change_difficulty()
    if not attempts:
        print('Invalid Choice!')
        continue
    start_game(attempts)

    if input("Want to try again? Type 'Y' to continue and 'N' to pass: ").lower() != 'y':
        print("Goodbye 👋")
        break
    else:
        if input("Want to change difficulty? Type 'Y' to change & 'N' to continue").lower() == 'y':
            attempts = change_difficulty()
            if not attempts:
                print('Invalid Choice!')
                continue
            start_game(attempts)
        else:
            start_game(attempts)
