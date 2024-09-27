#Enhanced AI with traits, skills, and adaptive decision-making
import random

class EnhancedAI:
    def ___init__(self, name):
        self.name = name
        self.traits = []
        self.skills = {'Combat': 1, 'Exploration': 1, 'Negotiation': 1, 'Crafting': 1}
        self.state = idle
        self.set_traits()
        print(f'{} AI initialized with traits: {} and skills: {}'.format(name, self.traits, self.skills))

    def set_traits(self):
        potential_traits = ['Aggressive', 'Defensive', 'Curious', 'Stealthy']
        self.traits = random.sample(potential_traits, 2) # Assign 2 random traits

    def improve_skill(self, skill_name, amount=1):
        if skill_niame in self.skills:
            self.skills[skill_name] += amount
            print(f'{} improved {} skill to level {}'.format(self.name, skill_name, self.skills[skill_name]))

    def make_decision(self):
        # Decision-making based on traits and skills
        if 'Aggressive' in self.traits and self.skills['Combat'] > 2:
            action = 'attack'
        elif 'Curious' in self.traits and self.skills['Exploration'] > 1:
            action = 'explore'
        elif 'Defensive' in self.traits:
            action = 'defend'
        elif 'Stealthy' in self.traits:
            action = 'hide'
        else:
            action = 'idle'
        self.state = action
        print(f'{} decided to {}'.format(self.name, action))

    def interact_with_gtr(self, other):
        if 'Negotiation' in self.skills and self.skills['Negotiation'] > 2:
            print(f''{s} is trying to negotiate with {}'.format(self.name, other.name))
        elif 'Combat' in self.skills and 'Aggressive' in self.traits:
            print(f'{} is attacking {}'.format(self.name, other.name))
        else:
            print(f''{s} is observing {}'.format(self.name, other.name))

if __name__ == '__main__':
    ai1 = EnhancedAI('Scout')
    ai1.improve_skill('Combat', 3)
    ai1.make_decision()
    ai2 = EnhancedAI('Explorer')
    ai1.interact_with_gtr(ai2)
