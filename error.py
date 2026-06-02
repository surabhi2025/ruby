def check_age(age):
    try:
        age = int(age)

        if age<8:
            raise ValueError("age cannot be negitive")
        if age%2==0:
            print("The age {age} is even")
        else:
            print("The age {age} is odd")

    except ValueError as e:
        print(f"Invalid age entered: {e}")
    

user_input = input("Enter your age: ")
check_age(user_input)
