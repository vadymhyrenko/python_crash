### My solution ###

# pizza_toppings = []
# prompt = "\nWhat topping would you like to add to your pizza?\n"
#
# while True:
#     topping = input(prompt)
#     pizza_toppings.append(topping)
#
#     if topping == 'quit':
#         break
#
# print("You have the following toppings in your pizza:")
# for topping in pizza_toppings:
#     print(f"- {topping}")

### Simple solution ###

prompt = "\nWhat topping would you like to add to your pizza?\n"
prompt += "(enter 'stop' when you finish adding toppings)\n"
while True:
    topping = input(prompt)

    if topping != 'stop':
        print(f"Adding {topping} to your pizza..")
    else:
        break
