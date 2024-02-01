number = input("Please, enter a number to determine is if an even or an odd:\n")
number = int(number)

if number % 2 == 1:
    print(f"{number} is odd")
else:
    print(f"{number} is even")
