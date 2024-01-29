prompt = "\nEnter some text here:"
prompt += "\nEnter 'quit' if you want to end the program:\n"

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


