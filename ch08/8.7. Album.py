def make_album(artist_name, album_title, songs_number=None):
    """Function returns a dictionary"""
    dictionary = {
        'artist': artist_name.title(),
        'title': album_title.title(),
    }
    if songs_number:
        dictionary['songs_number'] = songs_number
    return dictionary


prompt_artist_name = "\nEnter the artist's name: \n"
prompt_album_name = "\nEnter the album's title: \n"

while True:
    print("\nPlease enter the information about the album:")
    print("press 'q' to quit at any time:")

    artist = input(prompt_artist_name)
    if artist == 'q':
        break

    album = input(prompt_album_name)
    if album == 'q':
        break

    album = make_album(artist, album)
    print(album)
