n = int(input("Enter a decimal number: "))
result = ""


power = 0
while (2 ** power) <= n:
    power += 1
power -= 1

while power >= 0:
    value = 2**power
    if n >= value:
        result += "1"
        n -= value
    else:
        result += "0"
    power -=1

print(result)
