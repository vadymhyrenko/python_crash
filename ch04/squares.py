# the following code below is equal
squares = []
for value in range (1,11):
    square = value**2
    squares.append(square)
print(squares)

# to this one, but much simpler
squares2 = []
for value in range (1,11):
    squares2.append(value**2)
print(squares2)

# or even this
squares3 = [value**2 for value in range (1,11)]
print(squares3)