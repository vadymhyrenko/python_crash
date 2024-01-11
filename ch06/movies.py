favourite_movies = {
    'vadym': ['the godfather', 'the lord of the rings', 'star wars'],
    'liubania': ['dracula'],
    'viktor': ['terminator', 'naked gun', 'avengers'],
}

for k, v in favourite_movies.items():
    if len(v) > 1:
        print(f"\n{k.title()}'s favorite movie are:")
        for movie in v:
            print(f"\t {movie.title()}")
    else:
        print(f"\n{k.title()}'s favorite movies is:")
        for movie in v:
            print(f"\t {movie.title()}")
