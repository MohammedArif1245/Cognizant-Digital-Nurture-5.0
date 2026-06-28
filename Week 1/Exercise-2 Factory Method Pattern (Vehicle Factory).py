class Vehicle:

    def drive(self):
        pass


class Car(Vehicle):

    def drive(self):
        print("Car is running")


class Bike(Vehicle):

    def drive(self):
        print("Bike is running")


class Truck(Vehicle):

    def drive(self):
        print("Truck is running")


class VehicleFactory:

    @staticmethod
    def get_vehicle(vehicle_type):

        if vehicle_type == "car":
            return Car()

        elif vehicle_type == "bike":
            return Bike()

        elif vehicle_type == "truck":
            return Truck()

        else:
            return None


vehicle1 = VehicleFactory.get_vehicle("car")
vehicle2 = VehicleFactory.get_vehicle("bike")
vehicle3 = VehicleFactory.get_vehicle("truck")

vehicle1.drive()
vehicle2.drive()
vehicle3.drive()