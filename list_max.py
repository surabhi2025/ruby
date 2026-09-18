def list_max(lst):
    if len(lst) == 1:
        return lst[0]

    rest = list_max(lst[1:])

    if lst[0] > rest:
        return lst[0]
    else:
        return rest


print(list_max([3, 7, 2]))
print(list_max([8, 1, 5]))