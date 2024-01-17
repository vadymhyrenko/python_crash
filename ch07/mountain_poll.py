responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb?")

    responses[name] = response

    repeat = input("Would you like to let another person to response? (yes/no)")
    if repeat == 'no':
        polling_active = False
print("\n---- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")
