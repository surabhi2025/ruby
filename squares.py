max_range = int(input("Enter a range: "))

squares = []
even_squares = []
odd_squares = []

for num in range(max_range):
    square = num **2
    squares.append(square)

    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("All squares:", squares)
print("Even squares:", even_squares)
print("Odd squares: ", odd_squares)