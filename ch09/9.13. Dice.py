import random


class Die:
    """A simple class represents die rolling"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        # print(f"\nThis dice has {self.sides} sides")
        # random_number = random.randint(1, self.sides)
        # print(f"You rolled: {random_number}")
        return random.randint(1, self.sides)


# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()
results = []

for roll_num in range(10):
    roll_num = d6.roll_die()
    results.append(roll_num)
print(f"\nThe results of 10-times rolling 6-sided die: \n {results}")

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(10)
results = []

for roll_num in range(10):
    roll_num = d10.roll_die()
    results.append(roll_num)
print(f"\nThe results of 10-times rolling 10-sided die: \n {results}")

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(20)
results = []

for roll_num in range(10):
    roll_num = d20.roll_die()
    results.append(roll_num)
print(f"\nThe results of 10-times rolling 20-sided die: \n {results}")
