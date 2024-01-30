favourite_languages = {
    'jen': 'c++',
    'bill': 'python',
    'alice': 'python',
    'kate': 'ruby',
    'vadym': 'fortran',
}

# friends_list = ['bill', 'kate']
# for name in favourite_languages.keys():
#     print(f"Hi, {name.title()}")
#
#     if name in friends_list:
#         language = favourite_languages[name].title()
#         print(f"  I see you like {language}, {name.title()}, very nice!")


# for name in sorted(favourite_languages.keys()):
#     print(f"{name.title()}, thank you for taking part in a pooling!")

for language in set(favourite_languages.values()):
    print(f"{language.title()} were mentioned in a pooling!")
