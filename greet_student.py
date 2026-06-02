def greet_student(name):
    print("Hello", name, ",welcome to school today")

name = input("What is your name: ")
name = str(name)

student = greet_student(name)
print(name)