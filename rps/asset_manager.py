import os


class AssetManager:
    """
    AssetManager is responsible for managing and retrieving assets from a specified asset folder.
    The asset folder is assumed to be located at '../assets' relative to the script's location.

    Attributes:
        asset_folder (str): The path to the folder containing assets.
    """

    def __init__(self):
        """
        Initializes the AssetManager by setting the asset folder path.
        The asset folder is located at '../assets'.
        """
        self.asset_folder = os.path.join('..', 'assets')

    def get_asset(self, filename: str) -> str:
        """
        Retrieves the content of a specified asset file.

        :param filename: The name of the file to be retrieved from the asset folder.
        :return: The content of the file as a string. Returns an empty string if the file is not found.
        """
        path = os.path.join(self.asset_folder, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return ""
