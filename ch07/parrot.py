prompt = "\nTell me something, and I'll repeat it for you: "
prompt += "\nEnter 'quit' to end the program!"

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
