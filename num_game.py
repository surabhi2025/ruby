def num_game(n):
    for i in range(n):
        if i % 3 == 0 and i %5 == 0:
            print("FizzBuzz")
        elif i%5==0:
            print("Buzz")
        elif i%3 == 0:
            print("Fizz")
        else:
            print(i)
    return(n)

n = input("Enter a number")
n = int(n)

game = num_game(n)
print(game)
