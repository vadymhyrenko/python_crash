person_1 = {
    'first_name': 'luibania',
    'last_name': 'hyrenko',
    'age': 31,
    'city': 'kyiv'
}
# print(f"{person['first_name'].title()}'s living in {person['city'].title()}, and she's {person['age']}'s old.")
person_2 = {
    'first_name': 'vadym',
    'last_name': 'hyrenko',
    'age': 33,
    'city': 'kyiv'
}
person_3 = {
    'first_name': 'vyktor',
    'last_name': 'hyrenko',
    'age': 37,
    'city': 'kyiv'
}
people = [person_1, person_2, person_3]
if people:
    for person in people:
        full_name = f"{person['first_name']} {person['last_name']}"
        age = person['age']
        city = person['city'].title()
        print(f"{full_name.title()} is {age} years old and is living in {city}")
