

#printing title

print("MY COUNT DOWN TIMER CHALLENGE")

#recursion
# when a functions calls itself with a smaller version of the same problem

def countdown(number):
    #until reaching base case
    if number == 0:
        print("Time is up!")
        return
    print(number)
    countdown(number - 1)


print("Count down from 5:")
countdown(5)

# Build and Unwind
def build_and_unwind(level):
    #reaching base case
    if level == 0:
        print("base Case reached. Now the unwinding begins")

    print("Building level:", level)
    build_and_unwind(level-1)
    print("Unwinding Level:", level)


print("Build and Unwind Demo:")
build_and_unwind(3)

#counting with recursion
def counting_up(number):
    #reachuign base case

    if number > 10:
        return

    print(number)
    counting_up(number+1)

print("Counting from 1 to 10:")
counting_up(1)

#factorial using recursion

def factorial(number):
    #base case
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)



print(" Factorial Result:")
print("5! =", factorial(5))

#stack overflow

def unsafe_countdown(number):
    print(number)


print("Stack overflow note: ")
print(" A recursive function must have a base case to stop safely.")
print("The unsafe condition function is wrriten but not called.")
print("======================================")