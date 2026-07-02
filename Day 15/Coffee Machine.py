# TODO check th  resources are sufficient to make the order

from ingredient import *

print("Welcome to Coffee Machine")
profit=0
is_On = True

def is_Ingredient_Suffecient(order_ingredient):
    for item in order_ingredient:
        if resources[item]<order_ingredient[item]:
            print(f"Ingredient {item} Insufficient")
            return False
        return  True

def process_coins():
    print("Please Insert coins")
    total=float(input("The no. of quarters")) * 0.25
    total+=float(input("The no.Dimes")) * 0.10
    total+=float(input("The no.nicles")) * 0.05
    total+=float(input("The no.Pens")) * 0.01

    return total

def is_Transaction_successful(money_received,drink_price):
    if money_received>float(drink_price):
        return True
    else:
        print("You don't have enough money")
        return False


while is_On:
    choice =input("What would you like?").lower()
    if choice=="off":
        is_On = False
    elif choice=="report":
        for key,value in resources.items():
            print(f"{key}: {value}")
        print(f"Money : ${profit}")
    else:
        drink=MENU[choice]
        if is_Ingredient_Suffecient(drink["ingredients"]):
            payment=process_coins()
            if is_Transaction_successful(payment,drink["ingredients"]["cost"]):
                print("Your coffee is getting ready")
            print(f"cost {drink["ingredients"]["cost"]} your Payment{payment}")