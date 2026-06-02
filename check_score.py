def check_grade(score):
    if score >= 90 and score <= 100:
        print("You get an A")
    elif score >=80 and score <= 89:
        print("You get a B")
    elif score >=70 and score <=79:
        print("You get a c")
    elif score >=60 and score<=69:
        print("You get a d")
    elif score<60:
        print("You get a f")
    return score

score = input("What is your score?: ")
score = float(score)

grade = check_grade(score)
print(grade)