prompt = "\nPlease enter the city that you've visited.\n"
prompt += "Enter 'quit' if you're finished:\n"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd really like to visit {city.title()}")