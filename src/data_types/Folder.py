"""
    Folder is the basic type of data that the app handles
"""

class Folder():
    """
    Base type of Folder
    """
    def __init__(self, id_, name, path) -> None:
        self.id = id_
        self.name = name
        self.path = path

    def set_id(self, id_) -> None:
        """
        Setter for the id
        """
        if isinstance(id_, int):
            return
        self.id = id

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
