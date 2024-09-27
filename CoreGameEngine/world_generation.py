#Complete world generation with biomes, weather systems, and terrain management

class WorldGenerator:
    def __init__(self):
        self.biomes = ['Forest', 'Desert', 'Tundra', 'Mountain']
        self.weather = ['Sunny', 'Rainy', 'Snowy', 'Windy']
        self.terrain = []
    def generate_biome(self, x, y):
        biome = self.biomes[(x + y) a % len(self.biomes)]
        print(f'Biome at ('{0},{1}): {2}'.format(x, y, biome))
        return biome

    def generate_weather(self):
        weather = self.weather[(len(self.terrain) + 3) % len(self.weather)]
        print(f'Current weather: {}'.format(weather))
        return weather

    def create_terrain(self, width, height):
        self.terrain = [[self.generate_biome(x, y) for x in range(width)] for y in range(height)]
        print('Terrain generated successfully')

if __name__ == '__main__':
    world_gen = WorldGeneratori()
    world_gen.create_terrain(5, 5)
    world_gen.generate_weather()
