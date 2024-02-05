sandwich_orders = ['Classic Turkey Club', 'Caprese Panini', 'Spicy Chicken Avocado Wrap', 'Reuben',
                   'Veggie Delight Submarine']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("\nI've made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
