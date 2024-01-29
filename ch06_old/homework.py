# aliens = []
#
# for alien_fleet in range(30):
#     new_alien = {'name': 'ET', 'color': 'grey', 'size': 'medium',}
#     aliens.append(new_alien)
# #print(aliens)
#
# for alien in aliens:
#     print(alien)

programming_languages = {
    'python': {
        'author': 'guido van rossum',
        'year': '1991',
        'logo': 'snake',
    },
    'java': {
        'author': 'james gosling',
        'year': '1995',
        'logo': 'mug',
    },
    'fortran': {
        'author': 'john backus',
        'year': '1957',
        'logo': 'letter',
    },
}
for language, language_info in programming_languages.items():
    author = language_info['author']
    year = language_info['year']
    logo = language_info['logo']
    print(f"\nHere's some details about the {language}:")
    print(f"  It was designed by {author.title()} in {year} and has a {logo} logo.")
