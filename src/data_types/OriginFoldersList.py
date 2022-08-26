from PyQt5.QtWidgets import QListWidgetItem


class OriginFoldersList:
    """
    The list of origin folders
    """

    def __init__(self, list_widget, folders) -> None:
        self.folders = folders
        self.list_widget = list_widget
        self.ui_list = []

    def set_list_widget(self, list_widget) -> None:
        """
        Setter for the list widget
        """
        self.list_widget = list_widget

    def get_folders(self) -> list:
        """+
        Getter for the folders, returns the current list of origin folders
        """
        return self.folders

    def set_folders(self, folders) -> None:
        """
        Setter for the folders, set the folders to a new list
        """
        self.folders = folders
        self.update_ui()

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
