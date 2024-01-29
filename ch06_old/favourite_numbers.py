favourite_numbers = {
    'kelly': [3],
    'andrew': [6, 8],
    'patrick': [2, 3],
    'stanley': [1, 5, 9],
}
if favourite_numbers:
    for person, favourite_number in favourite_numbers.items():
        if len(favourite_number) > 1:
            print(f"{person.title()}'s favourite numbers are:")
            for number in favourite_number:
                print(f"  {number}")
        else:
            print(f"\n{person}'s favourite number is:")
            for number in favourite_number:
                print(f"  {number}")
else:
    print("No records in a dictionary found")
