class FoldersList:
    """
    The list of origin folders
    """

    def __init__(self, list_widget, folders) -> None:
        self.folders = folders
        self.list_widget = list_widget
        self.ui_list = []

    def add_folder(self, folder) -> None:
        """
        Append a new folder to the list
        """
        self.folders.append(folder)
        self.update_ui()

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
