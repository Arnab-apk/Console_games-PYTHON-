from random import randint

EASY_LEVEL=10
HARD_LEVEL=5

def check_answer(user_guess,actual_guess):
    if user_guess>actual_guess:
        print("Too High")
    elif user_guess<actual_guess:
        print("Too Low!")
    else:
        print("You got it!")
def game():
    print("Welcome to the number guessing game! ")
    print("I am thinking of a number between 1 and 100 ")
    answer=randint(1,100)


    def set_difficulty():
        level=input("Choose a difficuly, type 'easy' or 'hard': ")
        if level=="easy":
            return EASY_LEVEL
        elif level=="hard":
            return HARD_LEVEL
    guess=0
    turns=set_difficulty()
    while guess!=answer:
        print(f"You have {turns} turns remaining to guess the number")
        guess=int (input("Make a guess: "))
        turns-=1
        check_answer(guess,answer)
    
game() 


