prompt = "\nWelcome to the cinema! Tell me how old are you and I'll tell you what the ticket's price is:\n"

while True:

    age = input(prompt)
    if age == 'quit':
        break

    if int(age) < 3:
        print("The ticket is free to you!")
    elif 3 < int(age) < 12:
        print("The ticket would cost $3 to you!")
    else:
        print("The ticket would cost $5 to you!")
