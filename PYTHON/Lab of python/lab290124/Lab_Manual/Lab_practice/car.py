class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

# Creating an object (instance) of the Car class
my_car = Car("audi", "a4", 2019)

# Accessing attributes and calling methods of the object
print(my_car.get_descriptive_name())  # Output: 2019 Audi A4
my_car.read_odometer()  # Output: This car has 0 miles on it.

# Modifying an attribute through a method
my_car.update_odometer(50)
my_car.read_odometer()  # Output: This car has 50 miles on it.

# Incrementing an attribute value through a method
my_car.increment_odometer(100)
my_car.read_odometer()  # Output: This car has 150 miles on it.
