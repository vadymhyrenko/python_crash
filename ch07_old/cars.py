cars = {}

while True:
    name = input("Hi! What's your name?\n")
    car = input("What car would you like to buy?\n")

    cars[name] = car

    repeat = input("Would you like to collect more responses? (yes/no)")
    if repeat == 'no':
        break

print("\n--- Polling results ---\n")
for name, car in cars.items():
    print(f"{name.title()} would like to buy {car.title()}. Greate choice!")
