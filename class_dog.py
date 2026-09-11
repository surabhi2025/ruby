class Dog:
    species = "Dog"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

ruby = Dog("Labrodor Retriver", "yellow")
diamond = Dog("Golden Retriver", "white")

print("Ruby is a {}".format(ruby.species))
print("Diamond is also a {}".format(diamond.species))

print("Diamond is a {} and her color is {}".format(diamond.breed, diamond.color))
print("Ruby is {} and her color is {}".format(ruby.breed, ruby.color))
