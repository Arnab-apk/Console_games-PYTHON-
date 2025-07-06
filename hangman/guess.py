import random
word=["aardvark","baboon","camel"]
rand_word=random.choice(word)
print(rand_word)
len=len(rand_word)
placeholder=""
for position in range(0,len):
    placeholder+="_"
print(placeholder)
correct_letters=[]
game_over=False
while not game_over:
    
    char=input("Guess a letter: ").lower()
    display=""
    for letter in rand_word:
        if(char==letter):
            display+=char
            correct_letters.append(char)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)
        
    if "_" not in display:
        game_over=True
        print("You Win")
