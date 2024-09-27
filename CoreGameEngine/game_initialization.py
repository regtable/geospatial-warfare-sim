#Core game initialization script with additional logic

class GameEngine:
    def __init__(self):
        self.world = None
        self.players = []
        self.events = []
        print('Game Engine Initialized')

    def generate_world(self):
        self.world = 'Generated Complex World'
        print('World generated successfully')

    def add_player(self, player_name):
        self.players.append(player_name)
        print(f'Player ${player_name} added')

    def trigger_event(self, event_name):
        self.events.append(event_name)
        print(f'Event ${event_name} triggered')

if __name__ == '__main__':
    engine = GameEngine()
    engine.generate_world()
    engine.add_player('Player1')
    engine.trigger_event('Earthquake')
