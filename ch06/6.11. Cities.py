cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
    }
}
for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    nearby_mountains = city_info['nearby mountains']
    
    print(f"\nHere's some facts about the {city.title()}:")
    print(f"Population: {population}")
    print(f"Nearby mountains: {nearby_mountains.title()}")
