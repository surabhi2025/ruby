rows = int(input("Please enter the total number of rows: "))


for i in range(0, rows):
    for j in range(0, i):
        print("*", end='')
    print()

