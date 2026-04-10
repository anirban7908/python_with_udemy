from hangman_words import word_list
from hangman_art import stages, logo
import random

lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
print(f"Welcome To {logo}")

word_length = len(chosen_word)
placeholder = "_" * word_length
print("Word to guess: " + placeholder)
game_over = False
corrected_words = []

while not game_over:
    print(
        f"**************************************************************{lives}/6 Lives left**************************************************************************"
    )
    display = ""
    guess = input("Choose you letter: ").lower()
    if guess in corrected_words:
        print(f"You have already choose the letter: {guess}")
    else:
        for letter in chosen_word:
            placeholder += "_"
            if letter == guess:
                display += guess
                corrected_words.append(guess)
            elif letter in corrected_words:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        if not "_" in display:
            game_over = True
            print(
                f"**************************************************************Congrats!!! You have won. The correct word is {chosen_word}, and your word is {display}************************************************************************"
            )

        if guess not in chosen_word:
            lives -= 1
            print(f"Chosen letter is not exists in the Word!! You loose a life: Lives = {lives}")
            if lives == 0:
                game_over = True
                print(
                    f"***********************YOU LOSE. The correct word is {chosen_word}.**********************"
                )

    print(stages[lives])
