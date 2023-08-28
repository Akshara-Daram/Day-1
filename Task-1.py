import random
lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the higher limit: "))
x = random.randint(lower, upper)  # or randrange can be used as well
attempts = 0

for y in range(1, 11):
    print("You have 10 attempts u guess your number correctly")
    guess = int(input("Guess a number: "))
    attempts += 1

    if guess < x:
        print("Too low!")
    elif guess > x:
        print("Too high!")
    else:
        print(f"Congrats! You are right. It took you {attempts} attempts.")
        break
else:
    print(f"Sorry, you couldn't guess the number. The number was {x}.")