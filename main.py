import random
print("Welcome to the Number Guessing Game!")
secret_number = random.randint(1,10)
attempts = 1
max_attempts = 5

guess = int(input("Guess a number between 1 and 10: "))

while guess!=secret_number and attempts < max_attempts:
        if guess < secret_number:
                print("Too Low!")
        else:
                print ("Too Hihg!")

        attempts += 1
        guess = int(input("Try again:"))

if guess == secret_number:
    print("Correct!")
    print("You guessed it in", attempts,"attempts!")
else:
    print("Game Over!")
    print("The secret number was", secret_number)
