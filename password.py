import string
import random

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

all =  upper + lower + numbers

password = []

for i in range(12):
    password.append(random.choice(all))

   
print("The new password is", ''.join(map(str, password)))