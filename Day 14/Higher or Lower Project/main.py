import random
from art import logo, vs
from game_data import data

def ger_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(data):
    return f"{data['name']} a {data['description']} from {data['country']}."

def check_answer(user_choice, a_followers, b_followers):
    if a_followers > b_followers:
        return user_choice == 'a'
    else:
        return user_choice == 'b'

print(logo)
is_continue = True
score = 0
account_b = ger_random_account()

while is_continue:
    account_a = account_b
    account_b = ger_random_account()

    if account_a == account_b:
        account_b = ger_random_account()

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who have more followers? Select A or B! ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    a_followers = account_a['follower_count']
    b_followers = account_b['follower_count']

    is_correct = check_answer(guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        is_continue = False


    



