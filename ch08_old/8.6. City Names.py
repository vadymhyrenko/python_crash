def city_country(city, country):
    """The function returns the city and the country nealy formatted"""
    formatted_sting = f"{city}, {country}"
    return formatted_sting.title()


info = city_country('kiyv', 'ukraine')
print(info)

info = city_country('brno', 'slovakia')
print(info)

info = city_country('danzig', 'germany')
print(info)
