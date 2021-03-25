import random

player_username = input("Enter your G-Play Username: ")
# this method strip() removes white spaces left and right of the username
player_username = player_username.strip()
number = random.randint(1, 100)
tries = 0
print(f"Welcome {player_username}, Would you like to play the game now")
print("1) Yes")
print("2) No")

option = input("select your option: ")
option = int(option)

if option == 1:
    print("Welcome on onboard for the gaming session..")
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)
    tries += 1
    if guess > number:
        print("Guess a lower number")
    if guess < number:
        print("Guess a higher number")

    while (guess != number) and (tries < 5):
        guess = input("Try again: ")
        guess = int(guess)
        tries += 1

        if guess > number:
            print("Guess a lower number...")
        if guess < number:
            print("Guess a higher number...")

    if guess == number:
        print("You Won!!!..marvelous")
        print(f"Number of tries {tries}")
    else:
        print("You Lost!!!")

elif option == 2:
    print(f"Thank you {player_username}, see you next time when your ready!!")

else:
    print("Invalid option.Try again!")
