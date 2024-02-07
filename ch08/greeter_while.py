def formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("Please tell us who you are:")
    print("press 'q' at any moment to quit the program")

    f_name = input("What is your first name? ")
    if f_name == 'q':
        break

    l_name = input("What is your last name? ")
    if l_name == 'q':
        break

    print(f"Greetings, {formatted_name(f_name, l_name)}!\n")
