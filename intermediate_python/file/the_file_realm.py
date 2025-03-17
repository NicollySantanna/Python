liked_song = {
    'bad habits': 'Ed sheeran',
    'die with a smile': 'Bruno Mars',
    'thats what i like': 'Bruno Mars'
}


def write_liked_songs_to_file(songs, file_name):
    with open(file_name, 'w') as file:
        file.write('Liked songs:\n')
        for song, artist in songs.items():
            file.write(f'{song} by {artist}\n')
    print(f'Sucessfully added liked songs to {file_name}')


write_liked_songs_to_file(liked_song, 'liked_songs.txt')
