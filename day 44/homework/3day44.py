age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("you are a child")
elif age <= 19:
    print("you are a teenager")
elif age <= 64:
    print("you are an adult")
else:
    print("you are a senior")
    