"""
This module provides the AssetManager class, which is responsible for managing and retrieving assets
from a specified folder. The default asset folder is set to '../assets', relative to the script's
location.

The module includes the following functionality:
- Initializing the asset manager with a default asset directory.
- Retrieving the content of an asset file by its filename.

Usage:
    Create an instance of AssetManager and call the get_asset() method with the filename to retrieve
    the content of the file.
"""


import os


class AssetManager:
    """
    AssetManager is responsible for managing and retrieving assets from a specified asset folder.
    The asset folder is assumed to be located at '../assets' relative to the script's location.

    Attributes:
        assets_dir (str): The path to the folder containing assets.
    """

    def __init__(self):
        """
        Initializes the AssetManager by setting the asset folder path.
        The asset folder is located at '../assets'.
        """
        self.assets_dir = 'assets'

    def get_asset(self, filename: str) -> str:
        """
        Retrieves the content of a specified asset file.

        :param filename: The name of the file to be retrieved from the asset folder.
        :return: The content of the file as a string. Returns an empty string if the file is not
         found.
        """
        path = os.path.join(self.assets_dir, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return ""
