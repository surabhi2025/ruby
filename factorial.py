# factorial

def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)

print(" Factorial of 4 is:", factorial(4), "  = 4 x 3 x 2 x 1")
print(" Factorial of 5 is:", factorial(5), " = 5 x 4 x 3 x 2 x 1")