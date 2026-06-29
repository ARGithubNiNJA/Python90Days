from random import randint
print("Welcome to the Number Guessing Game!")
print("I am guessing a number between 1 and 100")

difficulty={
    "easy":10,
    "medium":7,
    "hard":5,
}
difficulty_chosen = (input("Choose your difficulty level: ")).lower()

Number_of_attempts=difficulty[difficulty_chosen]


target_number=randint(1,100)

def check_guess(guess):
    if guess==target_number:
        print( "You guessed the number")
        return True
    elif guess>target_number:
        print("You guessed higher than the number")
        return False

    elif guess<target_number:
        print("You guessed lower than the number")
        return False
    else:
        print("Good luck with that")
        return False

should_continue=False
while Number_of_attempts > 0 and not should_continue:
    print(f"You have {Number_of_attempts} attempts ")
    input_guess=int(input("Choose your Number : "))
    should_continue=(check_guess(input_guess))
    Number_of_attempts=Number_of_attempts-1



