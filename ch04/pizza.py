# pizzas = ["pepperoni", "cheese", "tuna"]
# print(pizzas)
# for pizza in pizzas:
#     print(f"I really like {pizza} pizza, it's my favourite!")
# print("I really like pizza!\n")
#
#
# numbers = [number+2 for number in range(1,5)]
# print(numbers)
#

friend_pizzas = ["pepperoni", "cheese", "tuna", "vegan"]
my_pizza = friend_pizzas[:]
print(my_pizza)
print(friend_pizzas)
friend_pizzas.append("new york")
my_pizza.insert(0,"paper")
print(my_pizza)
print(friend_pizzas)
