class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")
    
    def swim(self):
        print("Swim faster")

class Penquin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penquin")
    
    def run(self):
        print("Run faster")


peggy = Penquin()
peggy.whoisThis()
peggy.swim()
peggy.run()