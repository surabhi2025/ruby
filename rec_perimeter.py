def rec_perimeter(side1, side2):
    return (side1+side2)*2

side1 = float(input("Enter the largest side: "))
side2 = float(input("Enter the smallest side: "))

perimeter = rec_perimeter(side1, side2)
print(perimeter)