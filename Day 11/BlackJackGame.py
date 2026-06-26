import random
def deal_card():
    """return a random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    ##print(card)
    return card

user_card=[]
computer_card=[]
is_gameOver=False
def calculate_card(cards):
    """return a sum of the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        user_card.remove(11)
        user_card.append(1)

    return sum(cards)

for _ in range(2):
    ##new_card=deal_card()
    user_card.append(deal_card()) ##we are not using += to add the element because
    ## only an iterable can be done so, if you want to use += the wrap deal card within square brackets
    computer_card.append(deal_card())
while not is_gameOver:
    user_score=calculate_card(user_card)
    computer_score=calculate_card(computer_card)

    print(user_card)
    print(user_score)

    print(computer_card[0])
    print(computer_score)

    if user_score==0 or computer_score==0 or user_score>21:
        is_gameOver=True
    else:
        user_should_deal=input("Do you want another card?(y/n)")
        if user_should_deal=="y":
            user_card.append(deal_card())
        else:
            is_gameOver=True