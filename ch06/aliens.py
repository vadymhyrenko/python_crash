# alien_0 = {
#     'color': 'red',
#     'points': '5',
#     'speed': 'slow',
# }
# alien_1 = {
#     'color': 'yellow',
#     'points': '10',
#     'speed': 'medium',
# }
# alien_2 = {
#     'color': 'grey',
#     'points': '15',
#     'speed': 'fast',
# }
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

aliens = []

# returns a set of numbers, which just tells Python how many times we want the loop to repeat
# each time the loop runs, we create a new alien and then append it to the list of aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)
# print(alien_number)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'blue'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'blue':
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'
# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)

# show how many aliens were created in total
# print(f"The total number of created aliens is {len(aliens)}")
