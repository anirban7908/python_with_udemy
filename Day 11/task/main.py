import random
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

player_cards = []
computer_cards = []
is_game_over = False
for _ in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())

player_score = calculate_score(player_cards)
computer_score = calculate_score(player_cards)

print(f"Your Cards: {player_cards}, Your Score: {player_score}")
print(f"Computer first card: {computer_cards[0]}")
if player_score == 0 or computer_score == 0 or player_score > 21:
    is_game_over = True