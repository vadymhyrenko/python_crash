prompt = "\nPlease, enter the name of the city you have visited:"
prompt += "\n(Enter 'quit' when you are finished).\n"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"Oh, I'd really love to go to {city.title()}!")
