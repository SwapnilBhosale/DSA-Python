
""" Given a map Map < String, List < String > > userSongs with user names as keys
and a list of all the songs that the user has listened to as values.

Also given a map Map < String, List < String > > songGenres, with song genre as keys
and a list of all the songs within that genre as values. The song can only belong to only one genre.

The task is to return a map Map < String, List < String > >, where the key is a user name and
the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre.
A user can have more than one favorite genre if he/she has listened to the same number of songs per each of
the genres.
 """

def get_favourite_genre(songs, genre):
    res = {}
    for k in songs:
        res[k] = get_fav_genre(k, songs[k], genre)
    return res


def get_genre(song, genre):
    return [kv[0] for kv in genre.items() if song in kv[1]]


def get_fav_genre(k, songs, genre):
    if len(genre) == 0:
        return []
    my_choice_map = {}
    for song in songs:
        temp = get_genre(song, genre)
        if len(temp) == 0:
            continue
        computed_genre = temp[0]
        my_choice_map[computed_genre] = my_choice_map.get(
            computed_genre, 0) + 1
    max_song_key = max(my_choice_map.items(), key=lambda x: x[1])

    res = []
    for key, value in my_choice_map.items():
        if value == max_song_key[1]:
            res.append(key)
    return res


user_songs_1 = {
    "David": ["song1", "song2", "song3", "song4", "song8"],
    "Emma":  ["song5", "song6", "song7"]
}

song_genres_1 = {
    "Rock":    ["song1", "song3"],
    "Dubstep": ["song7"],
    "Techno":  ["song2", "song4"],
    "Pop":     ["song5", "song6"],
    "Jazz":    ["song8", "song9"]
}

output_1 = {
    "David": ["Rock", "Techno"],
    "Emma":  ["Pop"]
}

""" Why?
  David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
  Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre. """


user_songs_2 = {
    "David": ["song1", "song2"],
    "Emma":  ["song3", "song4"]
}

song_genres_2 = {}

output_2 = {
    "David": [],
    "Emma":  []
}

print(get_favourite_genre(user_songs_1, song_genres_1))
print(get_favourite_genre(user_songs_2, song_genres_2))
assert(get_favourite_genre(user_songs_1, song_genres_1) == output_1)
assert(get_favourite_genre(user_songs_2, song_genres_2) == output_2)
