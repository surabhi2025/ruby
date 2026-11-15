def max_ones():
    
    streak = best = 0
    for x in arr:
        if x:
            streak +=1
        else:
            streak = 0
        if streak > best:
            best = streak
    return best
arr = [1, 1, 0, 1, 1, 1, 0, 1]
print(" longest streak:", max_ones())