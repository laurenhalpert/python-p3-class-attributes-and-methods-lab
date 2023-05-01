import ipdb
from collections import Counter
class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    multiple_genres=[]
    artist_count={}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song(self)
        Song.add_to_genres(genre)
        Song. add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song(cls, count):
        Song.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in Song.genres:
            Song.genres.append(genre)
            Song.multiple_genres.append(genre)
        else:
            Song.multiple_genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in Song.artists:
            Song.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # if genre not in Song.genre_count:
        #     Song.genre_count[genre] = 1
        # else:
        #     Song.genre_count[genre] += 1
        Song.genre_count = dict(Counter(Song.multiple_genres))
        # return Song.genre_count
        # ipdb.set_trace()

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in Song.artist_count:
            Song.artist_count[artist] =1
        else:
            Song.artist_count[artist] +=1
        
        
        


