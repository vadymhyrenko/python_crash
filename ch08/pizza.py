# def make_pizza(size, *toppings):
#     """Print the list of toppings that have been requested"""
#     print(f"\nMaking a {size}-inch pizza from the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
#
# make_pizza(21, 'tuna', 'blueberry')
# make_pizza('15', 'mushrooms', 'papper','olives')


### using pizza as module ###
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested"""
    print(f"\nMaking a {size}-inch pizza from the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
