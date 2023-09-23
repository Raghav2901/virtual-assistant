def playMusic(directory):
    songs = os.listdir(directory)
    song = random.choice(songs) # Pick a random song from the directory
    print(f"Playing {song}")
    os.startfile(os.path.join(directory, song)) # Play the selected song using the default player 