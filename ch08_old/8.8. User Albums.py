def make_album(artist_name, album_title, songs_number=None):
    """Return a dictionary containing an artist name and an album title"""
    album_dict = {
        'artist': artist_name.title(),
        'album_title': album_title.title(),
    }
    if songs_number:
        album_dict['songs_number'] = songs_number
    return album_dict


prompt_artist_name = "\nEnter the artist's name: \n"
prompt_album_name = "\nEnter the album's title: \n"


while True:
    print("\nPlease enter the information about the album:")
    print("press 'q' to quit at any time:")

    artist = input(prompt_artist_name)
    if prompt_artist_name == 'q':
        break

    album = input(prompt_album_name)
    if prompt_album_name == 'q':
        break

    album = make_album(artist, album)
    print(album)
