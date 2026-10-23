def minElement(a, size):
    temp = a[0]
    for i in range(1, size):
        temp = min(temp, a[i])
    return temp

def maxElement(a, size):
    temp =a[0]
    for i in range(1, size):
        temp = max(temp, a[i])
        return temp


a = [12,1234, 45, 67, 1]
size = len(a)
print("Minimum element :", minElement(a, size))
print("Maximum element :", maxElement(a, size))