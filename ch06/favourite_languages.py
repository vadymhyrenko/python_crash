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

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you!")

# ### grabbing only values from the dictionary using values() method: ###
print("The following languages were mentioned in the polling:\n")
for language in favourite_languages.values():
    print(language.title())

# ### grabbing only UNIQUE values from the dictionary using set method along with the values() method: ###
print("The following unique languages were mentioned in the polling:\n")
for language in set(favourite_languages.values()):
    print(language.title())

print("\n")

close_friends = ['brooklyn', 'robert', 'susan', 'patrizia']
if close_friends:
    for close_friend in close_friends:
        if close_friend in favourite_languages.keys():
            print(f"I see you've been studying some programming, {close_friend.title()}! Very nice!")
        else:
            print(f"You've already participated in the polling, {close_friend.title()}!")
else:
    print("I don't have close friends :harold_face:")
