favourite_languages = {
    'jen': ['c++', 'ruby'],
    'bill': ['python'],
    'alice': ['python', 'assembler'],
    'kate': ['ruby'],
    'vadym': ['fortran', 'python'],
}

for name, languages in favourite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favourite languages are:")
    else:
        print(f"{name.title()}'s favourite language is:")
    for language in languages:
        print(f"- {language.title()}")
