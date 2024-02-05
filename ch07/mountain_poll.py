responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to allow another person to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results #
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
