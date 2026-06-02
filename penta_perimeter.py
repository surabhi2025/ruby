
def penta_perimeter(side):
    t = side * 5
    return t

side = input("Enter one side of the pentagon: ")
print("Datatype of user input:", type(side))
side = float(side)

perimeter = penta_perimeter(side)
#print(perimeter)
print(penta_perimeter)