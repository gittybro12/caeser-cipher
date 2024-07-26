alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']
def caeser_cipher(text,shift,direction):
    word = ""
    if direction == 'decode':
        shift *= -1
    for x in text:
        if x in alphabets:
            position = alphabets.index(x)
            new_position = shift + position
            new_letter = alphabets[new_position]
            word += new_letter
        else:
            word += text  
    print(f"here is your {direction}d result: {word}")          
play= True
while play:
    direction = input("Enter 'encode' to encrypt and 'decode' to decrypt\n").lower()
    text = input("Enter the word here\n")
    shift = int(input("Enter the number of shift\n"))
    ceaser_cipher(text,shift,direction)
    play_again = input("Enter 'yes' to play again and 'no' to quit\n" ).lower()

    if play_again == 'no':
        play = False
        print("Thanks for playing goodbye")
