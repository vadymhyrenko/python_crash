favourite_languages = {
    'mike': 'python',
    'carl': 'c++',
    'matt': 'ruby',
    'brooklyn': 'python'
}

print(f"Steve's favourite programming language is: {favourite_languages['brooklyn'].title()}")

for k, v in favourite_languages.items():
    print(f"{k.title()}'s favourite programming language is {v.title()}\n")

for name in favourite_languages.keys():  # method keys() is the default, so it's actually the same as
    # for name in favourite_languages:  # this one
    print(f"The following persons participated in the polling: {name.title()}")

friends = ['brooklyn', 'carl']
friends = []
if friends:
    for friend in friends:
        if friend in favourite_languages.keys():
            print(f"Hello, {friend.title()}!")
else:
    print("\nMy friends are not developers!\n")

buddies = ['matt', 'mike']
for name in favourite_languages.keys():
    print(f"{name.title()}")
    if name in buddies:
        print(f"  Hello, {name.title()}! I see you're developer!")
