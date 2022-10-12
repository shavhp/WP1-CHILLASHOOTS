from pygame import mixer

def sound_maker():
    # Instantiate mixer
    mixer.init()

    # Load audio file
    mixer.music.load('../Sound/Powerful-Trap-.mp3')

    # Set preferred volume
    mixer.music.set_volume(1.0)

    # Play the music
    mixer.music.play()

