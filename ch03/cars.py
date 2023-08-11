cars = ["volvo", "honda", "mazda", "audi"]
cars.sort() # sorting the list in alphabet order
print(cars)

cars = ["subaru", "toyota", "bmw", "porsche"]
cars.sort(reverse=True) # sorting the list in alphabet order. If you want to sort the original list in place;
# you can use the list.sort() method with the reverse parameter
print(cars)

# Sorting a list with sorted() function
cars = ["volvo", "honda", "mazda", "audi"]
print("\nHere's sorted list alphabetically:")
print(sorted(cars)) # sorting the list in alphabet order temporary. This method doesn't modify the original list;
# it creates a new sorted list

print("\nHere's sorted list reversed alphabetically:")
print(sorted(cars, reverse=True)) # sorting the list in reversed alphabet order temporary

print("\nHere's sorted list alphabetically individually:")

# Print the sorted list
for car in cars:
    print(car)

print("\nHere's original list:")
print(cars)

# Printing a list in reverse order
cars = ["mitsubishi", "tesla", "lotus", "dacia"]
cars.reverse()
print(cars)

# Finding the Length of a List
cars = ["subaru", "mercedes", "lotus", "chevrolet"]
print(len(cars))