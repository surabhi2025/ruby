# flip number

def flip_number(num):
    if num<10:
        return num

    else:
        last_digit = num % 10
        remaining = num // 10
        return str(last_digit) + str(flip_number(remaining))


print("flip number 123 =", flip_number(123))
print("flip number 456 =", flip_number(456))