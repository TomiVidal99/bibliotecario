"""
    OriginFolder inherits Folder, describes the folder that holds the files that are going to be watched
"""

from Folder import Folder

class OriginFolder(Folder):
    """
    The folder that is going to be watched for changes.
    """
    def __init__(self, id_, name, path) -> None:
        super().__init__(id_, name, path)
