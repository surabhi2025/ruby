#stair climb problem

def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs-1) + ways(stairs-2)

print("ways(3) =", ways(3))
print("ways(4) =", ways(4))