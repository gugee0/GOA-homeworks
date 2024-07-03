#welcome message
print("please enter you weight and height!;>")

#user has to enter their weight and height
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

# output BMI result
print("Your BMI is:", round(bmi, 2))
