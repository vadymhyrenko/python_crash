dream_vacation = {}

polling_active = True
while polling_active:
    name = input("What is your name? ")
    vacation = input("If you could visit one place in a world, where would you go? ")

    dream_vacation[name] = vacation

    repeat = input("Would you like to ask another person? (yes / no) ")
    if repeat == 'no':
        polling_active = False

for name, vacation in dream_vacation.items():
    print(f"{name.title()} would like to visit {vacation.title()}.")
