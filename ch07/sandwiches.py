# 7.8. Deli
# sandwich_orders = ['tuna', 'salmon', 'cheese']
# finished_sandwiches = []
#
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(current_sandwich)
#     print(f"I'm making a {current_sandwich} to you!")
#
# print(f"\nI've made the following sandwiches:")
# for finished_sandwich in finished_sandwiches:
#     print(f"- {finished_sandwich}")

# 7.9 No pastrami
sandwich_orders = ['pastrami', 'tuna', 'salmon', 'pastrami','cheese', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I'm making a {current_sandwich} to you!")

print(f"\nI've made the following sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich}")
