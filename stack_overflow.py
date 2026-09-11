def sum_down(n):
    if n==0:
        return 0
    return n + sum_down(n-1)

print("  sum_down(3) =", sum_down(3), "uses 3 frames")
print("  sum_down(5) =", sum_down(5), " uses 5 frames")