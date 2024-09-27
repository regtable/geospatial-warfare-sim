#Basic asset loader for managing textures and models
class AssetLoader:
    def __init__(self):
        self.assets = {}
        print('Asset Loader Initialized')

    def load_texture(self, texture_name, file_path):
        self.assets[texture_name] = file_path
        print(f'Texture {} loaded from {}'.format(texture_name, file_path))

    def get_asset(self, asset_name):
        return self.assets.get(asset_name, 'Asset not found')

If __name__ == '__main__':
    asset_loader = AssetLoader()
    asset_loader.load_texture('character', 'textures/character.png')
    print(asset_loader.get_asset('character'))
