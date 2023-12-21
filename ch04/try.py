numbers = list(range (1,21,2))
print(numbers)

numbers = [value*3 for value in range(3,30)]
print(numbers)

numbers = []
for value in range (3,30):
    number = value**3
    numbers.append(number)
print(numbers)


numbers = [value**3 for value in range(3,30)]
print(numbers)

numbers = list(range(1,10000001))
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))