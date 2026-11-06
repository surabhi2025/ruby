


def reverse(n):
    """
    arg n: the number of elements in the list to be reversed.
    return: the reversed list of elements from 1 to n.
    """
    arr = list(range(1, n+1))
    i = 0 # index of the first element in the list
    j = n-1 # index of the last element in the list

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr

print(" reverse(4) =", reverse(4))
print(" reverse(5) =", reverse(5))

