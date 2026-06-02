password = str(input("Enter any password"))

if len(password) < 6:
    print("You have a weak password")

elif len(password) <= 10:
    print("You have a medium password")

else:
    print("You have a strong password")
