class Vehicle:

    def __init__(self, capacity):
        self.capacity = capacity


class Bus(Vehicle):

    def __init__(self, capacity, total_fare):
        super().__init__(capacity)
        self.total_fare = total_fare

    def final_fare(self):
        return self.total_fare + (self.total_fare * 0.10)


school_bus = Bus(50, 5000)

print("INR", school_bus.final_fare())

