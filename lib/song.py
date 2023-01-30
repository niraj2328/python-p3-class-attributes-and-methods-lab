import ipdb

class Song:

    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    count = 0

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_artist(artist)
        Song.add_genre(genre)
        Song.count += 1
        self.update_artist_count(artist)
        self.update_genre_count(genre)

    @classmethod
    def add_artist(cls, artist):
        Song.artists.append(artist)

    @classmethod
    def add_genre(cls, genre):
        Song.genres.append(genre)

    @classmethod
    def increment_song_count(cls):
        Song.count += 1

    def update_artist_count(self, artist):
        # ipdb.set_trace()
        if(Song.artist_count.__contains__(artist)):
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

    def update_genre_count(self, genre):
        # ipdb.set_trace()
        if(Song.genre_count.__contains__(genre)):
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1



