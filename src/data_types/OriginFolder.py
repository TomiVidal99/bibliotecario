"""
    OriginFolder inherits Folder, describes the folder that holds the files that are going to be watched
"""

from src.data_types.Folder import Folder

class OriginFolder(Folder):
    """
    The folder that is going to be watched for changes.
    """
    def __init__(self, name, path) -> None:
        super().__init__(name, path)
