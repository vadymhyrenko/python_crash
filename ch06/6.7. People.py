person_1 = {
    'first_name': 'Vyktor',
    'last_name': 'Hyrenko',
    'age': 38,
    'city': 'Kyiv',
}
person_2 = {
    'first_name': 'Vadym',
    'last_name': 'Hyrenko',
    'age': 33,
    'city': 'Kyiv',
}
person_3 = {
    'first_name': 'Liubov',
    'last_name': 'Hyrenko',
    'age': 31,
    'city': 'Kyiv',
}
people = [person_1, person_2, person_3]
for person in people:
    name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city'].title()
    print(f"{name} is living in {city} and {age} years old")