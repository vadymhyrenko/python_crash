aliens = []

for alien_number in range(30):
    new_alien = {'color': 'grey', 'speed': 'fast', 'points': '15'}
    aliens.append(new_alien)

    for alien in aliens[:3]:
        if alien['color'] == 'grey':
            alien['color'] = 'yellow'
            alien['speed'] = 'extremely_fast'
            alien['points'] = '30'

for alien in aliens[:5]:
    print(alien)

print(f"The total number of aliens is {len(aliens)}")
