pets = []

pet_1 = {
    'name': 'pundyk',
    'kind': 'cat',
    'color': 'white',
    'owner': 'brooklyn',
}
pets.append(pet_1)

pet_2 = {
    'name': 'chekh',
    'kind': 'dog',
    'color': 'brown',
    'owner': 'steve',
}
pets.append(pet_2)

pet_3 = {
    'name': 'naginny',
    'kind': 'snake',
    'color': 'red',
    'owner': 'martyn',
}
pets.append(pet_3)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for k, v in pet.items():
        print(f"\t{k.title()}: {v.title()}")