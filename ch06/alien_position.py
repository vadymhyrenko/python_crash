alien = {
    'color': 'red',
    'x_position': 25,
    'y_position': 5,
    'speed': 'fast',
}

if alien['speed'] == 'fast':
    increment = 20
elif alien['speed'] == 'medium':
    increment = 10
else:
    increment = 5
print(f"{alien['color'].title()}'s alien new x postion is {alien['x_position'] + increment}")

