pizza = {
    'crust': 'thick',
    'toppings': ['olives', 'mushrooms', 'cheese', 'pepper']
}
print(f"So you've ordered a {pizza['crust']} pizza with the following toppings:")
for topping in pizza['toppings']:
    print(f"- {topping}")
