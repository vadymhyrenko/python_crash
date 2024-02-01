guests = input("How many people are going to visit the restaurant?\n")
guests = int(guests)

if guests >= 8:
    print("Sorry, you'll have to wait a little while we're preparing a table for you!")
else:
    print("Please, take any free table!")
