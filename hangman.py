def display_room():
    if lives == 7:
        with open('rooms/ascii szoba (7).txt') as room:
            content = room.read()
            print(content)
    if lives == 6:
        with open('rooms/ascii szoba (6).txt') as room:
            content = room.read()
            print(content)
    if lives == 5:
        with open('rooms/ascii szoba (5).txt') as room:
            content = room.read()
            print(content)
    if lives == 4:
        with open('rooms/ascii szoba (4).txt') as room:
            content = room.read()
            print(content)
    if lives == 3:
        with open('rooms/ascii szoba (3).txt') as room:
            content = room.read()
            print(content)
    if lives == 2:
        with open('rooms/ascii szoba (2).txt') as room:
            content = room.read()
            print(content)
    if lives == 1:
        with open('rooms/ascii szoba (1).txt') as room:
            content = room.read()
            print(content)
            
# PART 1
# display a menu with at least 3 difficulty choices and ask the user
from fcntl import LOCK_WRITE


with open('menu.txt') as f:
  content = f.read()
  print(content)
difficulty = input("Choose difficulty:")
# to select the desired level
#difficulty = "1" # sample data, normally the user should choose the difficulty


# STEP 2
# based on the chosen difficulty level, set the values 
invalid_input = True
while invalid_input == True:
    if difficulty == "1":
        lives = 7
        print("Here is your starting room:")
        display_room()
        invalid_input = False
    elif difficulty == "2":
        lives = 5
        print("Here is your starting room:")
        display_room()
        invalid_input = False
    elif difficulty == "3":
        lives = 3
        print("Here is your starting room:")
        display_room()
        invalid_input = False
    else:
        difficulty = input("Please type the number of difficulty:")
        continue
# for the player's lives
word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
lives = 5 # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"
print ("_ " * len(word_to_guess))

# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions
letter = input("Type a letter:").lower()
while True:
    if letter == "quit":
        print("Quit működik") 
        #ide kell majd a quit kódja még 
    elif len(letter) != 1:
        letter = input("Please type only one letter:")
        continue
    break        

# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
already_tried_letters = [] # this list will contain all the tried letters
if letter in already_tried_letters:
    print("You've already guessed this letter. Heres your previous geusses:")
    print(already_tried_letters)
else:
    already_tried_letters.append(letter)
    
# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".
if letter in word_to_guess:
    modified_word = word_to_guess.lower()
    for i in range(len(word_to_guess)):
        if word_to_guess[i] != letter:
            modified_word = modified_word.replace(word_to_guess[i], "_")
        else:
            continue
    print(" ".join((modified_word))

# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.

else:
    lives = lives - 1
    display_room()
    
    
# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4