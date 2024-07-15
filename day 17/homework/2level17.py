import random
#welcoming message
print("Welcome to the Number Guessing Game all you have to do is think of the number and we will guess it!")
print("Im thinking of a number between 1 and 100. Can you guess it?")

secret_number = random.randint(1, 100)
guess = None

while guess != secret_number:
    guess = int(input("Enter your guess (between 1 and 100): "))

    if guess < secret_number:
        print("Too low! Try guessing higher.")
    elif guess > secret_number:
        print("Too high! Try guessing lower.")

print(f"Congrats! You guessed the number {secret_number} correctly!")

