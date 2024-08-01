def get_score(prompt):
    while True:
        score = input(prompt)
        try:
            score = float(score)
            if 0 <= score <= 100:
                return score
            else:
                print("Tthe score must be between 0 and 100 please try again ;p")
        except ValueError:
            print("invalid input, please enter a number ;>")


print("Enter your scores:")
midterm = get_score("midterm score (0-100): ")
final = get_score("final exam score (0-100): ")
project = get_score("project score (0-100): ")


average = (midterm * 0.20) + (final * 0.40) + (project * 0.40)
print("your average score is: {:.2f}".format(average))

if average >= 70:
    print("you passed.")
else:
    print("you failed.")