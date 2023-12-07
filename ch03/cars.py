cars = ["dodge", "mazda", "ford", "bmw"]
print("\nHere's the sorted car list:")
print(sorted(cars))
print("\nHere's the original car list:")
print(cars)
cars.sort(reverse=True)
print("\nAnd here's the reverted list:")
print(cars)

# we can reverse order of the list without sorting
cars = ["dodge", "mazda", "ford", "bmw"]
print(cars)
cars.reverse()
print(cars)