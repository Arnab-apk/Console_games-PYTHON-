print('''                         WELCOME TO LOVE CALCULATOR
,d88b.d88b,     ,d88b.d88b,     ,d88b.d88b,     ,d88b.d88b,     ,d88b.d88b,
88888888888     88888888888     88888888888     88888888888     88888888888
`Y8888888Y'     `Y8888888Y'     `Y8888888Y'     `Y8888888Y'     `Y8888888Y'
  `Y888Y'         `Y888Y'         `Y888Y'         `Y888Y'         `Y888Y'
    `Y'             `Y'             `Y'             `Y'             `Y   ''')

def calculate_love_score(name1, name2):
    name = name1 + name2
    name = name.upper()
    
    word1 = "TRUE"
    word2 = "LOVE"
    
    s1 = 0
    s2 = 0

    for char in word1:
        count = name.count(char)
        print(f"{char} occurs {count} times in the combined name.")
        s1 += count

    for char in word2:
        count = name.count(char)
        print(f"{char} occurs {count} times in the combined name.")
        s2 += count

    love_score = int(str(s1) + str(s2))
    print(f"\nYour love score is: {love_score}")

    # Optional: add fun message
    if love_score > 80:
        print("You are a perfect match!")
    elif love_score > 40:
        print("You are quite compatible.")
    else:
        print("You might need to work on your relationship.")

# Get input and convert to uppercase once
name1 = input("Enter your name: ")
name2 = input("Enter your partner's name: ")

calculate_love_score(name1.upper(), name2.upper())

    

