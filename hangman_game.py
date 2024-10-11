import random
from collections import Counter
name = input("What is your name? ")
print(f"Welcome {name} to the Hangman Game!")
question = input("Would do you like to choose the words for Guess word game? Please type 'Yes' or 'No' ").lower()
someWords = []
if question == "yes":
    print("Type q for exit")
    while True:
        guess = input("Please, type the word do would like: ").lower()
        if guess == "q":
            break
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


word = random.choice(someWords)

print(word)

if __name__ == "__main__":
    print("Guess the word! word is a name of a fruit")

    for i in word:
        print('_', end=" ")
    print()

    playing = True
    letterGuessed = ""
    chances = len(word) + 2
    correct = 0
    flag = 0
    print("You have {} turns left!".format(chances))
    try:   
        while(chances > 0) and flag == 0:
            
            try:
                guess = str(input("Enter a letter to guess: "))
            except:
                print("Enter only a letter!")
                continue
            
            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter only a SINGLE letter")
                continue
            elif guess in letterGuessed:
                print("You have already guessed that letter, please try again!")
                continue
            
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess


            if guess not in word:
                print("You made a mistake, the letter is not in word, try again")
                chances -= 1
                print("You have {} turns left !".format(chances))



            for char in word:
                if char in letterGuessed and (Counter(letterGuessed)!= Counter(word)):
                    print(char, end= ' ')
                    correct += 1
                
                elif (Counter(letterGuessed) == Counter(word)):
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print("Congratulations, you won!")
                    break 
                    break
                else:
                    print("_", end=" ")

        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print("You lost! Try again...")
            print("The word was {}".format(word))
        

    except KeyboardInterrupt:
        print()
        print("Bye! Try again.")
        exit()



