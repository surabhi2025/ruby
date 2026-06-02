try:
    age = input("Enter your age: ")
    age = int(age)

    if age%2==0:
        print("Your age is even")
    else:
        print("Your age is odd")
except ValueError:
    print("You did not write your age correctly")