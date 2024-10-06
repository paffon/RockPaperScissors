import os

class AssetManager:
    def __init__(self, asset_folder):
        self.asset_folder = asset_folder

    def get_asset(self, filename):
        path = os.path.join(self.asset_folder, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return ""
