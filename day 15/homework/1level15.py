#welcome message
import random


print("hello! can you write number between 1 and 1000 ;)")

#entering number between 1 and 1000
secret_number = random.randint(1, 1000)

#ask user to guess the number
print("Guess the number between 1 and 1000!")
user_guess = int(input("Enter your guess: "))


#checking if guess is correct
if user_guess == secret_number:
    print("Correct!")

#and if guess is incorrect then output
print("Incorrect. The number was:", secret_number)

#another message
print("hope you had fun while doing this! have a nice day/night")