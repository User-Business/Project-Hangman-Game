import random
from collections import Counter

# Here we initialized the program with basic inputs
name = input("What is your name? ")
print(f"Welcome {name} to the Hangman Game!")
someWords = []

# Define valid responses
valid_responses = ['yes', 'no']

# Loop to ensure the user provides a valid input
while True:
    question = input("Would you like to choose the words for the Guess word game? Please type 'Yes' or 'No': ").lower()
    
    if question not in valid_responses:
        print("Please type only 'yes' or 'no'")  # Error message
        continue  # Go back to the start of the loop to request a new input

    if question == "yes":
        print("Type 'q' to exit")
        while True:
            guess = input("Please, type the word you would like: ").lower()
            if guess == "q":
                break
            if not guess.isalpha():  # Check if the input is a valid word
                print("Only letters are accepted for the word.")  # Error message
                continue  # Return to the start of the loop to request a new word
            someWords.append(guess)

    if len(someWords) < 1:
        someWords = '''apple banana mango strawberry 
                       orange grape pineapple apricot lemon coconut watermelon 
                       cherry papaya berry peach lychee muskmelon'''
        someWords = someWords.split()

    elif question == "no":
        someWords = '''apple banana mango strawberry 
                       orange grape pineapple apricot lemon coconut watermelon 
                       cherry papaya berry peach lychee muskmelon'''
        someWords = someWords.split()
    
    break  # Exit the loop after receiving a valid input

# Continue with the game logic...

word = random.choice(someWords)



#here the main structure of the code is initialized
if __name__ == "__main__":
    if question == "no":
        print("Guess the word! word is a name of a fruit")

    for i in word: #Here shows the number of letters in the selected word
        print('_', end=" ")
    print()

    letterGuessed = "" #Here is where your chosen letter will be stored
    chances = len(word) + 2
    correct = 0
    flag = 0
    print("You have {} turns left!".format(chances))
    #Here is the bloke of try-exception for the letter guessed
    try:   
        while (chances > 0) and flag == 0:
            
            guess = (input("Enter a letter to guess: ")).lower()
           
            #In this section, you have the conditions to check if the guess is accepted
            if not guess.isalpha(): #if the chosen letter is not a only a letter, will be transmitted a print and the code will return to input
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter only a SINGLE letter")
                continue
            elif guess in letterGuessed:
                print("You have already guessed that letter, please try again!")
                continue
            
            #If guess in word then guess will going to letterguessed
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess

            #If guess not in word, the chances less 1 attempt
            if guess not in word:
                print("You made a mistake, the letter is not in word, try again")
                chances -= 1
                print("You have {} turns left !".format(chances))



            for char in word:
                if char in letterGuessed and (Counter(letterGuessed)!= Counter(word)):
                    print(char, end= ' ')
                    correct += 1
                
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end='')
                    print(word)
                    flag = 1
                    print("Congratulations, you won!")
                    break 
                    break
                else:
                    print("_", end=" ")
        
    except ValueError as e:
            print(f"Error as {e}")
            
            if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
                print()
                print("You lost! Try again...")
                print("The word was {}".format(word))
        

    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()



