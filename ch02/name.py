name = "ada lovelace"
print(name.title())

name = "ADA lOveLACE"
print(name.title())

name = "ada lovelace"
print(name.upper())

name = "ADA LOVELACE"
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name= first_name + " " + last_name
print("Hello, " + full_name.title() + ", I'm very glad to meet you!")

first_name = "ada"
last_name = "lovelace"
full_name= first_name + " " + last_name
message = "Hello, " + full_name.title() + ", I'm very glad to meet you!\nIn this case I used the concatenation"
print(message)

first_name = "MALE"
last_name = "COOK"
full_name = first_name + '-' + last_name
message = f':{full_name.lower():}' + ':sunrise:'
print(message)

first_name = "  MALE"
last_name = "COOK  "
full_name = first_name + '-' + last_name
message = f':{full_name.lower().strip():}' + ':sunrise:'
print(message)