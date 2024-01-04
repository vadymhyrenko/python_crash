cars = ("bmw", "ford", "subaru", "mazda")
for car in cars:
    if car == "bmw":  # conditional test True
        print(car.upper())
    elif car == "honda":  # conditional test False
        print("Howdy?")
    else:
        print(car.title())
