import random
from art import logo
def deal_card():
    """Return a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(card_list):
    """Take a list of cards and return the sum of the card score"""
    if sum(card_list) == 21 and len(card_list) == 2:
        return  0

    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return  sum(card_list)

def compare_score(p_score, c_score):
    """Compares the user score p_score against the computer score c_score."""
    if p_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif p_score == 0:
        return "Win with a Blackjack 😎"
    elif p_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif p_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    player_cards = []
    computer_cards = []
    computer_score = -1
    player_score = -1
    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards: {player_cards}, Your Score: {player_score}")
        print(f"Computer first card: {computer_cards[0]}")
        if player_score == 0 or computer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card and 'n' to pass: ")
            if user_should_deal == 'y':
                player_cards.append(deal_card())
            else:
                is_game_over = True



    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)



    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"computer final hand: {computer_cards}, final score: {computer_score}")

    print(compare_score(player_score, computer_score))

while input("Do you want to play Black Jack? Type 'y' for 'yes' and 'n' for no: " ) == 'y':
    play_game()

print("\n\nGoogBye!!!☹️ Come Back Soon!!!🥹")
