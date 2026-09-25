#reversing string

def flip_name(s):
    if len(s) == 1:
        return s
    else:
        return flip_name(s[1:]) + s[0]


print("flip_name('Maya') =", flip_name('Maya'))
print("flip_name('Code') =", flip_name('Code'))