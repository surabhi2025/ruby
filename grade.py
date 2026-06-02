try:
    grade = float(input("Enter your grade: "))

    if grade >= 90 and grade <= 100:
        print("You get an A")
    elif grade >= 75 and grade <= 89:
        print("You get a B")
    elif grade >=50 and grade <=74:
        print("You get a C")
    elif grade<=50:
        print("FAIL")
    else:
        print("Invalid Input")
except ValueError as e:
    print("You have type your age wrong:", {e})

