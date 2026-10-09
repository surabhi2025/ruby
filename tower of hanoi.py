#tower of hanoi problem
#solving it

def hanoi(n):
    if n==0:
        return 0
    return 2 * hanoi(n-1)+1

print("Hanoi(1) =", hanoi(1))
print("Hanoi(2) =", hanoi(2))