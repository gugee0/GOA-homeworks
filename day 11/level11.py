# Welcome message
print("Welcome! Let's calculate and find out who is the eldest ;)")


# enter first persons age
age1 = float(input("Please enter the first person's age: "))


# enter second persons age
age2 = float(input("Please enter the second person's age: "))


# Calculate the sum of ages
total_age = age1 + age2
print("The total age is:", total_age)


# calculate the eldest person
if age1 > age2:
    print("\nThe first person is the eldest.")
elif age2 > age1:
    print("\nThe second person is the eldest.")
else:
    print("\nBoth persons are of the same age.")
