def print2largest(a):
    a = list(set(a))
    a.sort()


    if len(a) < 2:
        print("there is no second largest number")
    else:
        print(a[-2])


a =[1, 2, 3, 4, 5, 6, 7, 8, 9]
print2largest(a)