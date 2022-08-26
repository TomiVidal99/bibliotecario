"""
    Folder is the basic type of data that the app handles
"""

import uuid

class Folder():
    """
    Base type of Folder
    """
    def __init__(self, name, path) -> None:
        self.id = ""
        self.name = name
        self.path = path
        self.set_id()

    def set_id(self) -> None:
        """
        Creates an unique id
        """
        self.id = str(uuid.uuid1())

    def set_name(self, name) -> None:
        """
        Setter for the name
        """
        if isinstance(name, str):
            return
        self.name = name

    def set_path(self, path) -> None:
        """
        Setter for the path
        """
        if isinstance(path, str):
            return
        self.path = path

    def get_id(self) -> str:
        """
        Getter for the id
        """
        return self.id

    def get_name(self) -> str:
        """
        Getter for the name
        """
        return self.name

    def get_path(self) -> str:
        """
        Getter for the path
        """
        return self.path
