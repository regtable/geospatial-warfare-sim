#Basic AI behavior script with state transitions
class AIEntity:
    def __init__(self, name):
        self.name = name
        self.state = 'idle'
        print('{} initialized with state: {}'.format(self.name, self.state))

    def change_state(self, new_state):
        print('{} changing state from {} to {}'.format(self.name, self.state, new_state))
        self.state = new_state

    def perform_action(self):
        if self.state == 'idle':
            print('{} is waiting...'.format(self.name))
        elif self.state == 'aggressive':
            print('{} is attacking!'.format(self.name))
        else:
            print('{} is in an unknown state'.format(self.name))

if __name__ == '__main__':
    enemy = AIEntity('Enemy1')
    enemy.perform_action()
    enemy.change_state('aggressive')
    enemy.perform_action()
