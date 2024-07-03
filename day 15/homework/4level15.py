#welcome message
print("hello! enter your age and we will tell you if you can get discount or not! ;v")

#user has to enter her/his age
age = int(input("Enter your age: "))
spending = float(input("Enter total spending amount: "))

# Calculate discounts
discount_age = 0.1 if age > 60 else 0
discount_spending = 0.1 if spending > 100 else 0

# Calculate
total_amount = spending * (1 - discount_age) * (1 - discount_spending)

#print the total amount
print("Total amount after discounts: $" + format(total_amount, ".2f"))