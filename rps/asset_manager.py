import os

class AssetManager:
    def __init__(self):
        self.asset_folder = os.path.join('..', 'assets')

    def get_asset(self, filename) -> str:
        path = os.path.join(self.asset_folder, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return ""