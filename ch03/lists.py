bicycles = ["specialized", "trek", "cherokee"]
print(bicycles)

print(bicycles[0])

print(bicycles[2].title())


motorcycles = []
motorcycles.append("honda")
motorcycles.append("harley")
print(motorcycles)

motorcycles.insert(1, "ducati")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ["yamaha", "honda", "harley"]
last_owned = motorcycles.pop()
print("My last motorcycle was " + last_owned.title() + ".")
first_owned = motorcycles.pop(0)
print("My fist motorcycle was " + first_owned.title() + ".")

# removing the item from the list by the value
motorcycles = ["yamaha", "honda", "harley"]
motorcycles.remove("honda")
print(motorcycles)

motorcycles = ["yamaha", "honda", "harley", "ducati"]
too_expensive = motorcycles[-1]
print(motorcycles)
motorcycles.remove(too_expensive)
print("A " + too_expensive.title() + " is way expensive for me")
print(motorcycles)