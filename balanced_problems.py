#balanced parentheses problem

def count_paren(n, l=0, r=0):
    if l == n and r == n:
        return 1
    total = 0
    if l>r:
        total += count_paren(n, 1, r+1)
    if l < n:
        total += count_paren(n, l+1, r)

    return total


print("count_paren(1) =", count_paren(1))
print("count_paren(2) =", count_paren(2))