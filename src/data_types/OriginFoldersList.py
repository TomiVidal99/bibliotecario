from PyQt5.QtWidgets import QListWidgetItem, QWidget, QFileDialog
from .FoldersList import FoldersList
from src.utils.get_folders_dialog import get_open_files_and_dirs

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

    def add_folders(self, parent=None, default_directory='') -> list:
        """
        Pops up a window that handles adding new folders to the list
        """
        folder_path_list = get_open_files_and_dirs(parent, '', default_directory, QFileDialog.ShowDirsOnly)
        return folder_path_list
