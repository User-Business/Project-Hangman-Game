from random import randint
from math import log2
lower_bound = int(input("Choice a lower value: "))
upper_bound = int(input("Choice a upper value: "))
number_chosen_system = randint(lower_bound, upper_bound)
maximum_attempts = int(log2((upper_bound-lower_bound)+1))
print(f"The maximum attempts is {maximum_attempts}")
attempts = 0
number_chosen = int(input("Choose a value: "))
while attempts < maximum_attempts:
    attempts += 1
    if number_chosen == number_chosen_system:
        print("Congratulations!!!")
        break
    elif number_chosen > number_chosen_system:
        print("To high a value")
    elif number_chosen < number_chosen_system:
        print("To lower a value")

    
    number_chosen = int(input("Choose a value: "))

    if attempts > 6:
        break

else:
    print("You couldn't guess the value!!!")

print(f"Total Number of guesses = {attempts}")
print(attempts)


