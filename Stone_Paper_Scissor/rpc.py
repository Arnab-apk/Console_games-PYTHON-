import random
input=int(input('''What do you want to choose?
         Enter 0 for ROCK
         Enter 1 for PAPER
         Enter 2 for SCISSORS
         '''))
print("You choose: ")
if(input<=2):

    if(input==0):
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

    
    elif(input==1):
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

    
    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

    

    random=random.randint(0,2)
    print("The computer choose: ")
    if(random==0): 
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    elif(random==1):
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    else:
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    if(input==random):
        print("Opps its a DRAW!")
    elif(input==0 and random==2):
        print("Hurray you  WON!")
    elif(input==1 and random==0):
        print("Hurray you  WON!")
    elif(input==2 and random==1):
        print("Hurray you  WON!")
    else:
        print("You LOST! Try again :)")

else:
    print("Pls enter a valid input!")










