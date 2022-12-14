"""
    DestinationFolder inherits Folder.
    Describes the folder that is going to be recieving the files that are being filtered.
"""

from src.data_types.Folder import Folder
from src.data_types.Filter import Filter


class DestinationFolder(Folder):
    """
    The folder that recieves the files that are being organized.
    """

    def __init__(self, name, path, filters) -> None:
        super().__init__(name, path)
        self.filters = filters

    def set_filters(self, filters):
        """
        Setter for the filters.
        filters is a list of objects of Filter.
        """
        # TODO: make a better checking of the type of the filters
        if isinstance(filters, list):
            return
        self.filters = filters
