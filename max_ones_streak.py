def max_ones(n):
    arr = [1]*n + [0] + [1]*n
    streak = best = 0
    for x in arr:
        if x:
            streak +=1
        else:
            streak = 0
        if streak > best:
            best = streak
    return best

print("max ones 3:", max_ones(3))
print("max ones 4:", max_ones(4))