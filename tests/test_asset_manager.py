"""
This module contains unit tests for the AssetManager class, which is responsible for
managing and retrieving assets in the Rock-Paper-Scissors game.

The tests cover the following scenarios:
- Verifying that the AssetManager correctly retrieves the content of an existing file.
- Ensuring that an empty string is returned when the specified file does not exist.

Mocks are used to simulate file reading behavior to avoid actual file system operations.
"""


import unittest
from unittest.mock import patch, mock_open
import os

from rps.asset_manager import AssetManager


class TestAssetManager(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data="file content")
    def test_get_asset_file_exists(self, mock_file):
        # Arrange: Create an instance of AssetManager and define a file name
        am = AssetManager()
        file_name = 'test_file.txt'
        full_path = os.path.join(am.assets_dir, file_name)

        # Act: Call the get_asset method
        result = am.get_asset(file_name)

        # Assert: Check that the file content is returned and open was called with the right path
        mock_file.assert_called_once_with(full_path, 'r', encoding='utf-8')
        self.assertEqual(result, "file content")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_asset_file_not_exists(self, mock_file):
        # Arrange: Create an instance of AssetManager and define a non-existent file name
        am = AssetManager()
        file_name = 'non_existent_file.txt'

        # Act: Call the get_asset method
        result = am.get_asset(file_name)

        # Assert: Ensure an empty string is returned when the file is not found
        mock_file.assert_called_once_with(os.path.join(am.assets_dir, file_name), 'r',
                                          encoding='utf-8')
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
