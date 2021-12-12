old = 30
guess = 0
tries = 0
print("Guess how old I am!")
print("It is a number from 1 to 80. It is a multiple of 3 and also a multiple of 2. You only have 5 tries.")
while guess != old and tries < 5:
    guess = input("What's your guess? ")
    if not guess.isnumeric():
        print("Please put in a integer")
        tries = tries + 1
        continue
    else:
        guess = int(guess)
    if guess < 1 or guess > 80:
        print("Idiot! You're wasting your chances! The number is between 1 and 80!")
    elif guess%2 or guess%3:
        print("It is a multiple of 3 and also a multiple of 2.")
    else:
        if guess < old:
            print("Too low, man!")
        elif guess > old:
            print("Too high, dude!")
    tries = tries + 1
if guess == old:
    print("Avast! You got it! Now you know how old I am!")
else:
    print("No more guesses! Better luck next time!")
    print("I\'m", old, "years old!")