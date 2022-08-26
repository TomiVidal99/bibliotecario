from .FoldersList import FoldersList
from PyQt5.QtWidgets import QListWidgetItem

class DestinationFoldersList(FoldersList):
    """
    The list of DestinationFolders
    """

    def __init__(self, list_widget, folders) -> None:
        super().__init__(list_widget, folders)

    def update_ui(self) -> None:
        """
        Updates the UI list of components with the current list of origin folders
        """
        # TODO: make this
        folders_name = []
        self.list_widget.clear() # remove all items of the list first
        for folder in self.folders:
            folders_name.append(folder.get_path())
        for item in folders_name:
            item_widget = QListWidgetItem(item)
            self.list_widget.addItem(item_widget)
