name = input("Greeings! What is your name?\n")
age = input(f"How old are you, {name.title()}?\n")

if int(age) < 16:
    print(f"I'm afraid you're to young for voting, {name.title()}.")

elif int(age) > 100:
    print(f"{name.title()}, I'm afraid you're to old for voting.")

else:
    print(f"{name.title()}, you're old enough for voting. Just don't for Trump, please!")
