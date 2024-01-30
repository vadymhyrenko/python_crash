favourite_languages = {
    'jen': 'c++',
    'bill': 'python',
    'alice': 'python',
    'kate': 'ruby',
    'vadym': 'fortran',
}

for name, language in favourite_languages.items():
    print(f"{name.title()} is studying {language.title()}")

print("\n")

polling_participants = ['mathew', 'kate', 'bill', 'phill', 'caren', 'ross', 'jen']
for participant in polling_participants:
    if participant in favourite_languages:
        print(f"{participant.title()}, thanks for participating in a polling!")
    else:
        print(f"{participant.title()}, you should participate in a polling too!")
