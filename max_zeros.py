def max_zeros(n):
    arr = [1] + [0]*n + [1]
    streak = best = 0
    for x in arr:
        if not x:
            streak += 1
        else:
            streak = 0
        if streak > best:
            best = streak
    return best

print("max zeros 3 :", max_zeros(3))
print("max zeros 4:", max_zeros(4))