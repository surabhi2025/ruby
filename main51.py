string = input("Please enter your own word :")
char = input("Please enetr your own Character: ")

i = 0
count = 0

while(i <len(string)):

    if (string[i] == char):
        count = count+1
    i = i+1


print("The total number of times ", char, "has occurred=",count)



