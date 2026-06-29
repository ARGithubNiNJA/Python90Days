import random


def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def compare(U_Score, C_Score):
    if U_Score == C_Score:
        return "Draw"
    elif C_Score == 0:
        return "Loss. Opponent has a Blackjack."
    elif U_Score == 0:
        return "Win with a Blackjack!"
    elif C_Score > 21:
        return "Opponent went over. You win!"
    elif U_Score > 21:
        return "You went over. You lose."
    elif U_Score > C_Score:
        return "You win!"
    else:
        return "You lose."


def play_game():      # Fixed: added def
    user_card = []
    computer_card = []
    is_gameOver = False

    def calculate_card(cards):
        """Return the score of the cards."""
        if sum(cards) == 21 and len(cards) == 2:
            return 0

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)      # Fixed: use cards instead of user_card
            cards.append(1)

        return sum(cards)

    # Deal two cards each
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_gameOver:
        user_score = calculate_card(user_card)
        computer_score = calculate_card(computer_card)

        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_gameOver = True
        else:
            user_should_deal = input("Do you want another card? (y/n): ").lower()

            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_gameOver = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_card(computer_card)

    # Recalculate user's score in case Ace changed
    user_score = calculate_card(user_card)

    print(f"\nYour final hand: {user_card}, final score: {user_score}")
    print(f"Computer's final hand: {computer_card}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Main game loop
while input("Do you want to play Blackjack? (y/n): ").lower() == "y":
    play_game()