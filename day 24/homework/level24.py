print("Think of a number between 1 and 100 and i will try and guess it!! ;D")

low = 1
high = 100
guess = (low + high) // 2

while True:
    print(f"My guess is: {guess}")
    response = input("Is it correct? (yes, too high, too low): ").strip().lower()
    
    if response == "yes":
        print(f"yay! I guessed your number;> {guess}.")
        break
    elif response == "too high":
        high = guess - 1
    elif response == "too low":
        low = guess + 1
    else:
        print("Please enter 'yes', 'too high', or 'too low'.")
    
    guess = (low + high) // 2

print("thanks for playing my game!")