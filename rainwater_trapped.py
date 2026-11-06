def rainwater(n):
    bars = [0, n, 0, n, 0]
    return min(max(bars[:3]), max(bars[2:])) - bars[2]

print(" rainwater 3:", rainwater(3))
print(" rainwater 4:", rainwater(4))