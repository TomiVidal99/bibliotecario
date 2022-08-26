from PyQt5.QtWidgets import QListWidgetItem
from .FoldersList import FoldersList

class OriginFoldersList(FoldersList):
    """
    The list of origin folders
    """

    def __init__(self, list_widget, folders) -> None:
        super().__init__(list_widget, folders)
        self.update_stored_folders_callback = None

    def set_update_stored_folders_callback(self, callback) -> None:
        """
        Callback to update the stored data
        """
        self.update_stored_folders_callback = callback

    def update_ui(self) -> None:
        """
        Updates the UI list of components with the current list of origin folders
        """
        folders_name = []
        self.list_widget.clear() # remove all items of the list first
        for folder in self.folders:
            folders_name.append(folder.get_path())
        for item in folders_name:
            item_widget = QListWidgetItem(item)
            self.list_widget.addItem(item_widget)

        if self.update_stored_folders_callback != None:
            self.update_stored_folders_callback()
