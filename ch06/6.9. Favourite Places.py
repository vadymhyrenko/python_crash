favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire']
}
for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favourite places are:")
    for place in places:
        print(f"- {place.title()}")
       