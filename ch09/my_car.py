from car import Car
my_new_car = Car("Mazda", "CX5", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 30
my_new_car.read_odometer()