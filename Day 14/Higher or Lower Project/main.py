import random
from game_data import data
from art import logo, vs

def get_random_data(data):
    random_contestent1=random.choice(data)
    random_contestent1_name = random_contestent1['name']
    random_contestent1_description = random_contestent1['description']
    random_contestent1_country = random_contestent1['country']

    random_contestent1_banner = f"Compare A: {random_contestent1_name} a {random_contestent1_description} from {random_contestent1_country}."


    random_contestent2=random.choice(data)
    random_contestent2_name = random_contestent2['name']
    random_contestent2_description = random_contestent2['description']
    random_contestent2_country = random_contestent2['country']

    random_contestent2_banner = f"Against B: {random_contestent2_name} a {random_contestent2_description} from {random_contestent2_country}."
    
    return {
        'random_contestent1':random_contestent1,
        'random_contestent1_banner':random_contestent1_banner,
        'random_contestent2':random_contestent2,
        'random_contestent2_banner':random_contestent2_banner,
    }


def find_winner(user_guess, a_followers_count, b_followers_count):
    if a_followers_count['follower_count'] > b_followers_count['follower_count']:
        return user_guess == 'a'
    else:
        return user_guess == 'b'

print(logo)
score = 0
game_should_continue = True


while game_should_continue:
    contestents = get_random_data(data)

    print(contestents['random_contestent1_banner'])
    print(vs)
    print(contestents['random_contestent2_banner'])

    a_followers_count = contestents['random_contestent1']
    b_followers_count = contestents['random_contestent2']
    
    user_guess = input('Who has more followers in Instagram? Type A or B.').lower()
    is_correct = find_winner(user_guess, a_followers_count, b_followers_count)
    
    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
    



