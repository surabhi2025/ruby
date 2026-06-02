try:
    
    num = float(input("Enter a number: "))
    if num%2==0:
        print("Your number is even")
    else:
        print("Your number is odd")
    if num<0:
        print("Your number is negitive")
    elif num>0:
        print("Your number is positive")
except ValueError as e:
    print("Not valid:", {e})
else:
    print("Valid")

