"""
    MovedFolder inherits Folder, describes the folder that contains the file that has been moved to.
"""

from src.data_types.Folder import Folder

class MovedFolder(Folder):
    """
    Folder that contains a file that has been moved to.
    """
    def __init__(self, name, path, from_) -> None:
        super().__init__(name, path)
        self.from_ = from_

    def set_from(self, from_) -> None:
        """
        Setter for the from_.
        """
        if isinstance(from_, str):
            return
        self.from_ = from_
