cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby_mountains': 'andes',
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby_mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby_mountains': 'himilaya',
    }
}
for city, city_info in cities.items():
    country = city_info['country']
    population = city_info['population']
    nearby_mountains = city_info['nearby_mountains']

    print(f"\n{city.title()} is in {country.title()}.")
    print(f"It has a population of about {population} people.")
    print(f"The nearby mountains are {nearby_mountains.title()}.")