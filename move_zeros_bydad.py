def move_zeros():

    write = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[write] = arr[i]
            write += 1

    for i in range(write, len(arr)):
        arr[i] = 0

    return arr
arr = gene_counts = [8, 0, 3, 0, 0, 5, 2]


print("two pointer:", move_zeros())