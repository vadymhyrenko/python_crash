sandwich_orders = ['Pastrami', 'Classic Turkey Club', 'Pastrami', 'Caprese Panini', 'Spicy Chicken Avocado Wrap',
                   'Pastrami', 'Reuben', 'Veggie Delight Submarine', 'Pastrami']
finished_sandwiches = []

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
print("Sorry, we run out of Pastrami today.")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"\nI made your {sandwich} sandwich.")

    finished_sandwiches.append(sandwich)

print("\nI've made the following sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
