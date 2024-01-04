players = ["charles", "william", "stephen", "mark"]
print(players[-1:])
for player in players [-1:]:
    print(f'Hi, {player.title()}')


my_food = ["pizza", "tom yam", "ramen"]
print(my_food)
friends_food = my_food[:] # slice the list and assign as the new varible
friends_food.append("paela")
print(friends_food)

my_food = ["pizza", "tom yam", "ramen", "pasta", "soup", "bread"]
print(f"My first favourite food is: \n{my_food[:3]}")
print(f"My second favourite food is: \n{my_food[3:6]}")
print(f"My third favourite food is: \n{my_food[-3:]}")
