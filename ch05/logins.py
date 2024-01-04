# usernames = ['admin', 'robets', 'ashley', 'steven', 'lina']
# if usernames:
#     for username in usernames:
#         if username == "admin":
#             print("Hello, " + username + ", would you like to see your status report?")
#         else:
#             print("Hello, " + username.title() + ", have a productive day!")
# else:
#     print("No users found!")

current_users = ['john', 'rebekka', 'amy', 'Luke']
new_users = ['luke', 'richard', 'REBEKKA', 'jacob']

current_users_lower = [user.lower() for user in current_users]

# alternative way is to create an empty list and add each element from the existing one
# current_users_lower = []
# for user in current_users:
#     current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Please, choose a new login name, user {new_user} is already exist!")
    else:
        print(f"Welcome to the system, {new_user}!")