import art
print("          WELCOME TO CAESAR CIPHER DECODER/ENCODER")
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Part 2: Caesar Cipher Function
def caesar(original_text, shift_amount, direction_mode):
    result_text = ""
    
    # Reverse shift if decoding
    if direction_mode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % len(alphabet)
            result_text += alphabet[new_position]
        else:
            result_text += letter  # Keep symbols, spaces, and punctuation unchanged

    print(f"Here is the {direction_mode}d result: {result_text}")

should_cont=True
while should_cont:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Normalize shift in case it's larger than 26
    shift = shift % 26

# Call function
    caesar(original_text=text, shift_amount=shift, direction_mode=direction)
    restart=input("Type 'yes' if  you want to go again. otherwise type 'no'\n").lower()
    if restart=='no':
        should_cont=False
        print("Good Bye!")
