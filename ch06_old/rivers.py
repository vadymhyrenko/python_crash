rivers = {
    'amazon': 'brazil',
    'nile': 'egypt',
    'yangtze': 'china',
    'mississippi': 'usa',
}

if rivers:
    for k, v in rivers.items():
        print(f"{k.title()} runs through the {v.title()}")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())
