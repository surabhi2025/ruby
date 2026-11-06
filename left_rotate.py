def left_rotate(n):
    """
    arg
    n: the number of positions to rotate the array to the left.
    return: the array after left rotation by n positions.
    """
    arr = [1, 2, 3, 4, 5]
    n = n % len(arr)
    return arr[n:] + arr[:n]


print("left rotate(1)", left_rotate(1))
print("left rotate(2)", left_rotate(2))