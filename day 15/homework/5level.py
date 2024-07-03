#welcome message
print("hello! enter your GPA and we will tell you if you will be able to get scholarship or not ;<")


#get information from the user
gpa = float(input("Enter your GPA: "))
income = float(input("Enter your family's annual income: "))

#check if user can get scholarship
if income < 50000 and gpa >= 3.5:
    print("Congratulations! You qualify for a high scholarship.")
else:
    print("Sorry you cant get high scholarship.")
    