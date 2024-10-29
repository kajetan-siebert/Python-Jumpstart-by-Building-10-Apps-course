import random

print("---------------------------")
print("---GUESS THE NUMBER GAME---")
print("---------------------------")

random_number = random.randint(0, 100)
user_number=-1

while True:

    user_input = input("Guess the number between 0 and 100: ")
    user_number = int(user_input)

    if user_number > random_number:
        print(f"Sorry but the number {user_number} is higher than the number"
              f" you're looking for")
    elif user_number < random_number:
        print(f"Sorry, but the number {user_number} is lower than the number"
              f" you're looking for")
    else:
        print(f"Yes, you've guessed it right, the number is {random_number}!")
        break
