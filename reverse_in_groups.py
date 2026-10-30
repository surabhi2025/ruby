def group_reverse(n):
    arr = [1, 2, 3, 4, 5, 6]
    for i in range(0, 6, n):
        arr[i:i+n] = arr[i:i+n][::-1]

    return arr

print("reverse(2)", group_reverse(2))
print("reverse(3)", group_reverse(3))