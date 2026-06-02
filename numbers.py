import random
playing = True
number = str(random.randint(10,20))

print("I will genarate a number from 0 to 9, and you have guess on number at a time")
print("The game will end when you get 1 hero")

while playing:
    guess = input("Give me your best guess! \n")
    if number == guess:
        print("You win the game")
        print("The number was", number)
        break
    else:
        print("Your guess isn't quite right, try again. \n")