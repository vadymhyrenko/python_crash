rivers = {
    'nile': 'egypt',
    'tysa': 'ukraine',
    'thames': 'england',
}

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}")

print(f"\nThe following rivers were mentioned:")
for river in rivers.keys():
    print(f"- {river.title()}")

print(f"\nThe following countries were mentioned:")
for country in rivers.values():
    print(f"- {country.title()}")
