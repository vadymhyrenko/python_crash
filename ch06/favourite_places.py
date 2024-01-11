favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'abraham': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire']
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favourite place is:")
    for place in places:
        print(f"{place.title()}")