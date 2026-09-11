# head recursion and increasing-decreasing

def mirror(n):
    if n==0:
        return 0
    rest = mirror(n-1)
    return rest + 2*n

print("  mirror(3) =", mirror(3))
print("  mirror(4) =", mirror(4))