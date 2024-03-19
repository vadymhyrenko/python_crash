filename = 'guest_book.txt'

print("Enter 'quit' or 'q' when you finish")
while True:
    name = input("Greetings! What is your name, friend? ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print("Your name was added to the guest book!")
