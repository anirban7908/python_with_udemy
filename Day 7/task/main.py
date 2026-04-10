<<<<<<< HEAD
<<<<<<< HEAD
word_list = ["aardvark", "baboon", "camel"]
=======
import random
import  hangman_words
import hangman_art
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list
lives = 6
>>>>>>> 8a2243621c15705a4f4beaebf7b410250fd1b2a5

stages = hangman_art.stages
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
logo = hangman_art.logo
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

<<<<<<< HEAD
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
=======
import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

=======
>>>>>>> 8a2243621c15705a4f4beaebf7b410250fd1b2a5
game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
<<<<<<< HEAD
    print("****************************<???>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

=======
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print('You have already chosen this letter')
        
>>>>>>> 8a2243621c15705a4f4beaebf7b410250fd1b2a5
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
<<<<<<< HEAD
=======
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
>>>>>>> 8a2243621c15705a4f4beaebf7b410250fd1b2a5
        lives -= 1

        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
<<<<<<< HEAD
            print(f"***********************YOU LOSE**********************")
=======
            print(f"***********************YOU LOSE. The correct word is {chosen_word}.**********************")
>>>>>>> 8a2243621c15705a4f4beaebf7b410250fd1b2a5

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])
<<<<<<< HEAD
>>>>>>> origin/master
=======
>>>>>>> 8a2243621c15705a4f4beaebf7b410250fd1b2a5
