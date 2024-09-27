#core game initialization script

class GameEngine:
    def __init__(self):
        self.world = None
        print('initializing game engine')

    def generate_world(self):
        self.world = 'Generated World'
        print('World generated successfully')

if __name__ == '__main__':
    engine = GameEngine()
    engine.generate_world()
