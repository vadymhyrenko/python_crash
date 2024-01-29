alien0 = {'color': 'green', 'points': 5}
print(alien0['color'])
print(alien0['points'])

new_points = alien0['points']
print(f"You just earned {str(new_points)} points!")

alien0['x_position'] = 0
alien0['y_position'] = 25

print(alien0)

alien1 = {}

alien1['x_position'] = 25
alien1['y_position'] = 50
print(alien1)


alien1['y_position'] = 75
print(alien1)

alien0 = {'color': 'green', 'points': 5}
print(alien0)
del alien0['color']
print(alien0)
