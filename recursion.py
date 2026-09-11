# recursion, base case

def sum_down(n):
    if n==0:
        return 0
    return n+sum_down(n-1)

print(" sum_down(3) = 3 + 2 + 1 + 0 =" , sum_down(3))
print(" sum_down(4) = 4 + 3 + 2 + 1 +0 =", sum_down(4))
