import random
from logo import art  # Make sure logo.py has variable: art = "Your ASCII art here"

# Returns a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Calculates the score from a list of cards
def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Compares scores and returns the result
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "YOU LOSE, opponent has a Blackjack"
    elif user_score == 0:
        return "YOU WIN with a Blackjack"
    elif user_score > 21:
        return "YOU LOSE, you went over 21"
    elif computer_score > 21:
        return "YOU WIN, opponent went over 21"
    elif user_score > computer_score:
        return "YOU WIN"
    else:
        return "YOU LOSE"

# Main game function
def play_game():
    print(art)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Loop to replay the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 10)
    play_game()