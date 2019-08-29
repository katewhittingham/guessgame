import random

n = random.randint(1,100)

guess = int(input("Guess a number from 1 to 99: "))

a = abs(guess - n)

while a != 0:
    if 15 < a < 50:
        print("You are warm!")
        guess = int(input("Guess again: "))
        break
    elif a < 16:
        print("You are very warm!")
        guess = int(input("Guess again: "))
        break
    else:
        print("You are cold!")
        guess = int(input("Guess again: "))
        break
else:
    print("You guessed it!")

    
b = a

a = abs(guess - n)


while a != 0:
    if a < b:
        print("You are warmer!")
    if a > b:
        print("You are cooler!")
    elif a == b:
        print("You are the same temp!")
        
    guess = int(input("Guess again: "))
    b = a
    a = abs(guess - n)
else:
    print("You guessed it!")

    
