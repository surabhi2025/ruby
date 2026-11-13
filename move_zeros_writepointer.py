def move_zeros(n):
    arr = [0, 1] * n
    write = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write] = arr[i]
            write += 1

    for i in range(write, len(arr)):
        arr[i] = 0

    return arr

print("move zeros 3:", move_zeros(3))
print("move zeros 4:", move_zeros(4))