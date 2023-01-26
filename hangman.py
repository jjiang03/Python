# assignment: programming assignment 1
# author: Justin Jiang
# date: 1, 19, 2023
# file: hangman.py is a program that (allows the user to select their own word size and number of lives in the game hangman)
# input: (the input asks for the user's preferred word size (3-12), and preferred number of lives (out of 10). It then asks the user for a letter one at a time.)
# output: (If the user guesses the correct letter, the letter will be shown, but if the user guesses incorrectly, they will lose a life as shown by the "X")

from random import choice, random
import random
import os

dictionary_file = "dictionary.txt" 

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))  # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    dictionary_file = "dictionary.txt"
    dictionary = {}
    max_size = 12
    with open(os.path.join(__location__,dictionary_file), "r") as f:
        data = f.read().split()
        for i in data:
            i.strip()
    f.close()

    try :
        for n in range(max_size):
            hold = []
            for k in data:
                if len(k) == n:
                    hold.append(k)
            dictionary[n] = hold
        raise Exception
    except :
        holdMax = []
        for p in data:
            if len(p) >= max_size:
                holdMax.append(p)
        dictionary[12] = holdMax
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    print(dictionary)
    

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    try:
        size = int(input("Please choose a size of a word to be guessed [3 - 12, default any size]: \n"))
        if size >= 3 and size <= 12:
            print(f'The word size is set to {size}.')
        else:
            raise Exception
    except:
        size = random.randint(3,12)
        print("A dictionary word of any size will be chosen. ")

    try:
         lives = int(input("Please choose a number of lives [1 - 10, default 5]: \n"))
         if lives >= 1 and lives <= 10:
            print(f'You have {lives} lives.')
         else:
            raise Exception
    except :
        lives = 5
        print("You have 5 lives.")

    return (size, lives)


# MAIN

if __name__ == '__main__' :
    
    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)
    
 
    
   
    # print a game introduction

    print("Welcome to the Hangman Game!")
    running = True
    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while running:    
    # set up game options (the word size and number of lives)
        size_lives = get_game_options()
        lives = size_lives[1]
    # select a word from a dictionary (according to the game options)
        selectedSize = random.choice(dictionary[size_lives[0]])
        selectedWord = selectedSize.upper()
        
        
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)
    
        # START GAME LOOP   (INNER PROGRAM LOOP)
        livesRemaining = lives
        guessed = []
        hidden = []
        
        if "-" in selectedWord:
            hidden.append('-')
        
        while livesRemaining >= 0:
        
        # format and print the game interface:
              # Letters chosen: E, S, P      list of chosen letters
            print("Letters chosen: " + ", ".join(guessed))

            for i in range(len(selectedWord)):
                if selectedWord[i] in hidden:
                    print(selectedWord[i] + "  ", end = '')
                else:
                    print("__  ", end = '')
            print(" lives: " + str(livesRemaining) + " ", end = '')
              # __ P P __ E    lives: 4   XOOOO        hidden word and lives
            for n in range(lives,0,-1):
                if livesRemaining - n < 0:
                    print("X", end = '')
                else:
                    print("O", end = '')
            print("")

        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game

            if livesRemaining > 0 :
                if "".join(sorted(hidden)) == "".join(sorted(set(selectedWord))):
                    print(f'Congratulations!!! You won! The word is {selectedWord}!')
                    break    
                else:
                    while True:
                          # ask the user to guess a letter
                        userGuess = input("Please choose a new letter > ").upper()
                    
                        if len(userGuess) != 1 or userGuess.isdigit() or userGuess.isalpha() == False:
                            print("")
                            continue
                        
                    
                        else:
                            print(userGuess)
                             # update the list of chosen letters
                            if (userGuess in selectedWord) and (userGuess not in guessed):
                                # if the letter is correct update the hidden word,
                                hidden.append(userGuess)
                                guessed.append(userGuess)
                                print("You guessed right!")
                                break
                            elif userGuess in guessed:
                                print("You have already chosen this letter.")
                
                            else:
                                 # else update the number of lives
                                   # and print interactive messages      
                                livesRemaining -= 1
                                guessed.append(userGuess)
                                print("You guessed wrong, you lost one life. ")
                                break
        # END GAME LOOP   (INNER PROGRAM LOOP)
            else:
                
                print("You lost! The word is " + selectedWord + "!")
                livesRemaining -= 1
                            
              
        # END MAIN LOOP (OUTER PROGRAM LOOP)
        # ask if the user wants to continue playing, 
        # if yes start a new game, otherwise terminate the program
        menuScreen = input("Would you like to play again [Y/N]?\n").upper()
        if menuScreen == 'Y':
            pass
        else:
            print("Goodbye!")
            break
        
            
            


                
                


            
      

       
      

        

        

        
       
      

      