#list-sum

def list_sum(lst):
    if lst == []:
        return 0
    return lst[0] + list_sum(lst[1:])

print(" list_sum([1, 2, 3]) =", list_sum([1, 2, 3]))
print(" list_sum([4, 5, 6]) =", list_sum([4, 5, 6]))