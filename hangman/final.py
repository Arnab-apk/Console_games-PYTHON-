import random
import words
import pics

print(pics.art[0])


rand_word=random.choice(words.word_list)
#print(rand_word)
len=len(rand_word)
placeholder=""
print("THE WORD:")
for position in range(0,len):
    placeholder+="_"
print(placeholder)
correct_letters=[]
lives=6
game_over=False
while not game_over:
    print(f"*********************{lives}/6*********************")
    char=input("Guess a letter: ").lower()
    if char in correct_letters:
        print(f"You've already guessed {char}")
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
    print(pics.pictures[lives-1])   
    if "_" not in display:
        game_over=True
        print("*********************YOU WIN*********************")

    elif char not in rand_word:
        lives-=1
        print(f"You guessed {char}, that's not in the word. You lose a life!")
        if lives ==0:
            game_over==True
            print(f"*********************IT WAS {rand_word}.YOU LOST!*********************")
            
    