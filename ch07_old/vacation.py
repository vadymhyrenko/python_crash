# 7.10 Dream Vacation - my
responses = {}

polling_active = True

while polling_active:
    name = input("What is you name?\n")
    response = input("Which country would you like to go?\n")

    responses[name] = response

    repeat = input("Would you like to receive one more answer? (yes/no)\n")
    if repeat == 'no':
        polling_active = False

print("--- Responses results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to go to {response.title()}")

# 7.10 Dream Vacation - solution

name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True:
    # Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)

    # Store the response.
    responses[name] = place

    # Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# Show results of the survey.
print("\n--- Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
