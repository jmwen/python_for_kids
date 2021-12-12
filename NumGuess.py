import random
secret = random.randint(1, 100)
guess = 0
tries = 0
print("AHOY! I'm the Dread Pirate Roberts, and I have a secret!")
print("It is a number from 1 to 100. I'll give you 6 tries. ")
while guess != secret and tries < 6:
    guess = int(input("What's yer guess? "))
    if guess < 1 or guess > 100:
        print("Idiot! You're wasting your chances! The number is between 1 to 100!")
    else:
        if guess < secret:
            print("Too low, ye scurvy dog!")
        elif guess > secret:
            print("Too high, landlubber!")
    tries = tries + 1
if guess == secret:
    print("Avast! Ye got it! Found my secret, ye did!")
else:
    print("No more guesses! Better luck next time, matey!")
    print("The secret number was", secret)
