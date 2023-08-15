numbers = [1,2,3,4,5]
for number in numbers:
    print(number)

for value in range (6,10):
    print(value)

print("\nNow lets use list with range methods:\n")

numbers = list(range(1,11))
print(numbers)

for number in numbers:
    print(number)

digits = [1,3,4,5,7,9]
print(min(digits))
print(max(digits))
print(sum(digits))

even_numbers = list(range(2,11,2))
for number in even_numbers:
    print(number)
