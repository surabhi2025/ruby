import random
#import numpy as np

n = int(input("Enter the number of numbers: "))

rand_int = []


for i in range(n):
    x = random.randint(0,1000000)
    rand_int.append(x)
    #print(x, rand_int)

sum_numbers = sum(rand_int)
print(sum_numbers)

mean_num = sum_numbers / len(rand_int)

print(mean_num)

#print(np.array(rand_int).mean())