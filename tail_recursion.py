#tail recursion and linear recursion

def tail_sum(n, acc=0):
    if n == 0:
        return acc
    return tail_sum(n-1, acc + n)

print("  tail_sum(4) =", tail_sum(4), " = 4 + 3 + 2 + 1")
print("  tail_sum(5) =", tail_sum(5), " = 5 + 4 + 3 + 2 + 1")