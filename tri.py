import math

h = float(input("Enter the hypotnuse: "))
oppo = float(input("Enter the oppisite side: "))
add = float(input("Enter the adjecent side: "))


sin = oppo/ h
cos = add/h
tan = oppo/add

angle_1 = math.degrees(math.atan(tan))
angle_2 = math.degrees(math.acos(cos))
angle_3 = math.degrees(math.asin(sin))

print("The 3 angles are:", angle_1, angle_2,angle_3)