age = input(" please enter your age :) ")
try:
    age = int(age)
    if age <= 0:
        print("Please enter a positive number.")
        exit()
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

experience = input("please enter your years of driving experience ;3 ")
try:
    experience = int(experience)
    if experience <= 0:
        print("please enter a positive number.")
        exit()
except ValueError:
    print("invalid input ;( please enter a number")
    exit()

# Check eligibility
if age >= 18:
    if experience >= 1:
        print("you are eligible for a driver's license.")
    else:
        print("you need at least 1 year of driving experience!!")
elif age < 18:
    print("you must be at least 18 years old ;>")
    