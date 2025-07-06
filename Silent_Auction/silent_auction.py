import art
print(art.logo)
#asking inputs

def highest_bidder(bidding_dictionary):
    winner=""
    highest_bid=0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")

bids={}
cont=True

while(cont):
    
    name=input("What is your name?: ")
    price=int(input("what is your bid?:"))
    
#save data into dictionary
    bids[name]=price 

    should_cont=input("Are there any other bidders? type yes or no.\n").lower()
    if should_cont=="no":
        cont=False
        highest_bidder(bids)
    elif should_cont=="yes":
        print("\n"*50)
     



    

        

