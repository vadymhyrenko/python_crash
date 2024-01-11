# a list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'pepperoni', 'olives']
}
print(f"You've ordered {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"- {topping}")
print(f"My favourite topping is {pizza['toppings']}")