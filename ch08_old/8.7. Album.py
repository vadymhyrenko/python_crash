def make_album(artist_name, album_title, songs_number=None):
    """Return a dictionary containing an artist name and an album title"""
    album_dict = {
        'artist': artist_name.title(),
        'album_title': album_title.title(),
    }
    if songs_number:
        album_dict['songs_number'] = songs_number
    return album_dict


album = make_album('metallica', 'saint anger', 15)
print(album)

album = make_album('blind guardian', 'victory')
print(album)

album = make_album('deep purple', 'color of the rain', 12)
print(album)
