prompt = "\nGreetings! Please, tell me how old you are?\n"
prompt += "Enter 'quit' when you are finished.\n"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age <= 3:
        print("The ticket is free for you!")
    elif 4 <= age < 12:
        print("The ticket will cost $5 to you!")
    else:
        print("The ticket will cost you $10")
