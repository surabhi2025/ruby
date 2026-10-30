def reverse(n):

    arr = list(range(1, n + 1))

    i = 0

    j = n - 1

    while i < j:

      arr[i], arr[j] = arr[j], arr[i]

      i += 1

      j -= 1

    return arr

print("reverse(4) =", reverse(4))

print("reverse(5) =", reverse(5))


