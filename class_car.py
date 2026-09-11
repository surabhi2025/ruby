class Ferrari:

    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def info(self):
        print(f"I am a Ferrari. My fuel type is {self.fuel_type}. My max speed is {self.max_speed} miles per hour")

    
class BMW:

    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed

    def info(self):
        print(f"I am a BMW. My fuel type is {self.fuel_type}. My max speed is {self.max_speed} miles per hour.")


Car1 = Ferrari("Premium Unleaded Gasoline", 205)
Car2 = BMW("Premium Unleaded Gasoline", 155)


for car in (Car1, Car2):
    car.info()