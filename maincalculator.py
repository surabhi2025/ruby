def add(P,Q):
    return P+Q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q


print("Please select operation")
print("a, Add")
print("b, Subtract")
print("c, multiply")
print("d, divide")

choice = input("please enter choice (a/b/c/d):")

num1= int(input("Please enter the first number: "))
num2 = int(input("Please enter the secomd number"))

if choice == 'a':
    print(num1, "+", num2, "=" , add(num1, num2))
elif choice == 'b':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 'c':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == 'd':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("This is an invalid input")