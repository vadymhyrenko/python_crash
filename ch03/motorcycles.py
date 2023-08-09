motorcycles = ['harley', 'ducati', 'jamaha', 'honda']
print(motorcycles)

motorcycles[0] = 'honda' # modifying the value of the list's element
print(motorcycles)

motorcycles = ['harley', 'ducati', 'jamaha']
print(motorcycles)

motorcycles.append('honda') # adding a new element to a list
print(motorcycles)

motorcycles = []
motorcycles.append('harley')
motorcycles.append('ducati')
motorcycles.append('jamaha')
motorcycles.append('honda')
print(motorcycles)

motorcycles = ['harley', 'ducati', 'jamaha']
motorcycles.insert(2, 'ford') # adding element to the list in a specific position/order
print(motorcycles)

motorcycles = ['harley', 'ducati', 'jamaha']
del motorcycles[0]
print(motorcycles)

motorcycles = ['harley', 'ducati', 'jamaha']
print(motorcycles)
popped_motorcycles = motorcycles.pop() # popping the last element form the list
print(popped_motorcycles)

motorcycles = ['harley', 'ducati', 'jamaha']
last_ownded = motorcycles.pop()
print("The last bike I owned is " + last_ownded.title() + ".")

motorcycles = ['harley', 'ducati', 'jamaha']
first_owned = motorcycles.pop(0) # popping the first element form the list
print("The first bike I owned is " + first_owned.title() + ".")

motorcycles = ['harley', 'ducati', 'jamaha']
print()
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['harley', 'ducati', 'jamaha']
print(motorcycles)
too_expensive = motorcycles[-1] # the same as too_expensive = 'jamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print("I decided not to buy " + too_expensive.title() + ", it's to expensive.")

employees = ['muscle', 'guardsman', 'male-cook']
rovnyi_patsyk  = employees[-1]
message = f':{rovnyi_patsyk}:' + ":sunrise:"
print(message)