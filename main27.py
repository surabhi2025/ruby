age = float(input("Enter your age:"))
student = bool(input("Are you a student?:"))
senior = bool(input("Are you a senior?:"))

if age < 5:
    price = 0
elif age <= 12:
    price = 5
elif age <= 59:
    price = 10
else:
    price = 7

if price != 0:
    if student == "yes":
        price = price * 0.8
    if senior == "yes":
        price = price * 0.9

print("Your ticket price is dollar", price)
