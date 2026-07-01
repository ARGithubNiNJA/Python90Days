import random
from art import logo,vs
from game_data import data


account_b = random.choice(data)

def check_Answer(account_a, account_b,guess):
    if account_a>account_b:
       return guess=="a"
    else:
       return guess=="b"

def format_Data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return  (f"{account_name},{account_description},{account_country}")

print(logo)
score=0
is_correct = True
while is_correct:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A {format_Data(account_a)}")
    print(vs)
    print(f"Against B {format_Data(account_b)}")

    guess  = input("who has  more number of followers Type 'A' or 'B': ").lower()
    a_followersCount=account_a["followers"]
    b_followersCount=account_b["followers"]

    is_correct = check_Answer(a_followersCount,b_followersCount,guess)
    print(f"A followers {a_followersCount},b_followersCount{b_followersCount} is {is_correct}")
    if is_correct:
        score+=1
        print(f"Correct! Your Current Score: {score} !")
    else:
        print(f"Wrong! your Current Score : {score} !")