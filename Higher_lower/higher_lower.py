from art import logo,vs
from data import famous_people
import random
score=0
#ascii art to show
print(logo)
game_should_continue = True
account_b=random.choice(famous_people)  #initially set account_b to a random account
#generate a random account from the game
#format the account data into printable format
def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"
    
def check_answer(user_guess, a_follower_count, b_follower_count):
    """Check if the user's guess is correct."""
    if user_guess == 'A':
        return a_follower_count > b_follower_count
    else:
        return b_follower_count > a_follower_count
 
while game_should_continue:
    #generate a random account from the game
    account_a = account_b  #set account_a to the previous account_b
    account_b = random.choice(famous_people)
    
    #ensure account_a and account_b are not the same
    while account_a == account_b:
        account_b = random.choice(famous_people)
    
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #ask the user for a guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
     
     #clear the screen for better visibility
    #get follower count of accounts
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    #check if user is correct
    user_is_correct = check_answer(user_guess, a_follower_count, b_follower_count)
    
    if user_is_correct:
        score += 1
        print("\n" * 100)
        print(logo)
        print(f"You are correct! Current score: {score}")
        #make account_b the next account at position a
        account_a = account_b
        

    else:
        print(f"Sorry, that's wrong. B has more followers. Final score: {score}")
        game_should_continue = False







#format the account data into printable format
#ask the user for a guess


#give the feeback on their guess
#score keeping
#make the game repeatable
#making the accounts at pos b be the next account at position a


