# from pathlib import Path
#
# path = Path("guest.txt")
# content = input("Greetings! What's your name, friend? ")
# path.write_text(content)

# Preferred option

name = input("What's your name? ")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(name)
