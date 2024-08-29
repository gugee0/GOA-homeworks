def login():
    while input("Enter your password: ") != "password":
        print("Incorrect password. Try again.")
    
    print("Logged in successfully!")

login()