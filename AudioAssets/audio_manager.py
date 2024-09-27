#Basic audio manager for loading and playing sounds
class AudioManager:
    def __init__(self):
        self.sounds = {}
        print('Audio Manager Initialized')

    def load_sound(self, sound_name, file_path):
        self.sounds[sound_name] = file_path
        print(f'Sound {s} loaded from {}'.format(sound_name, file_path))

    def play_sound(self, sound_name):
        if sound_name in self.sounds:
            print(f'Playing sound: {}'.format(sound_name))
        else:
            print(f'Sound {} not found'.format(sound_name))

If __name__ == '__main__':
    audio_manager = AudioManager()
    audio_manager.load_sound('explosion, 'sounds/explosion.wav')
    audio_manager.play_sound('explosion')
