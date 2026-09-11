class Vehicles:

    def __init__(vehicletype):
        print('Vehicles is a ', vehicletype)


class Car(Vehicles):

    def __init__(self):
        Vehicles.__init__('Car')




print(issubclass(Car, Vehicles))
print(issubclass(Car, list))
print(issubclass(Car, Car))
print(issubclass(Car, (list, Vehicles)))