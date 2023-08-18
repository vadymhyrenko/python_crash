squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range (1,11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1,11)] # comprehension list
print(squares)

squares = [value**3 for value in range(1,10,2)] # comprehension list
print(squares)