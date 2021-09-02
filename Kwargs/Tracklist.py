# Joe defined a dictionary listing his favorite artists, their albums,
# and the song from each of the albums. It looks as follows:
#tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
#                      "On the Other Side": "Samara"},
#          "Cure": {"Disintegration": "Lovesong",
#                   "Wish": "Friday I'm in love"}}

# Joe's tastes can change, though.

# Your task is to define a tracklist() function that would take
# several keyword arguments representing musicians and
# dictionaries with albums and songs as values. For the example
# above, the call of this function will look as follows:


# The function should print the values from the dictionary in the 
# following form:
def tracklist(**tracks):
    for key, value in tracks.items():
        print(key)
        for k, v in value.items():
            print(f'ALBUM: {k} TRACK: {v}')

def tracklist(**artists):
    for artist, album in artists.items():
        print(artist)
        print("\n".join(f'ALBUM: {album_name} TRACK: {track}' for album_name, track in album.items()))

def tracklist(**artists):
    for artist, albums in artists.items():
        print(artist, *[f"ALBUM: {album} TRACK: {track}" for album, track in albums.items()], sep='\n')


tracklist(Woodkid={"The Golden Age": "Run Boy Run",
                   "On the Other Side": "Samara"},
          Cure={"Disintergration": "Lovesong",
                "Wish": "Friday I'm in love"})