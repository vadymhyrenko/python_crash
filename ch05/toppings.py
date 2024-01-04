# requested_toppings = ['tomatoes', 'cheese', 'olives', 'shrimps']
#
# for requested_topping in requested_toppings:
#     if requested_topping == 'shrimps':
#         print("Sorry, we're out of shrimps now!")
#     else:
#         print("Adding " + requested_topping + " to your pizza..")
# print("\nPizza's ready!")
#
#
# requested_toppings = []
# if requested_toppings:  # when the name of the list is used in statement, Python returns True if the list contains at
#     # least one element
#     for requested_topping in requested_toppings:
#         print("Adding " + requested_topping + ".")
#     print("Finishing making pizza!")
# else:
#     print("You're pizza will be plain!")
available_toppings = ['tomatoes', 'cheese', 'olives', 'mushrooms', 'pepper']

requested_toppings = ['pepper', 'olives', 'pineapple']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding requested " + requested_topping + " to a pizza")
    else:
        print("We don't have a " + requested_topping + ". Sorry!")
print("We're already cooking your pizza!")
