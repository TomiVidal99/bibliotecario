class FoldersList:
    """
    The list of origin folders
    """

    def __init__(self, list_widget, folders) -> None:
        self.folders = folders
        self.list_widget = list_widget
        self.ui_list = []
        self.last_clicked = ""

    def get_last_clicked(self) -> str:
        """
        Getter for the last clicked
        """
        return self.last_clicked

    def set_last_clicked(self) -> None:
        """
        Sets a callback that it's triggered when an item in the list has been clicked
        """
        def set_clicked(item) -> None:
            folder_name = item.text()
            # find the folder in the list that corresponds to the one that the user has clicked
            for folder in self.folders:
                if folder_name == folder.get_path():
                    self.last_clicked = folder.get_id()
                    print(folder.get_name())
        self.list_widget.itemClicked.connect(set_clicked)

    def add_folder(self, folder) -> None:
        """
        Append a new folder to the list
        """
        self.folders.append(folder)
        self.update_ui()

    def remove_folder(self, folder_id) -> None:
        """
        Removes a folder from a given id from the list
        """
        for folder in self.folders:
            if folder.get_id() == folder_id:
                self.folders.remove(folder)
                self.update_ui()

    def set_list_widget(self, list_widget) -> None:
        """
        Setter for the list widget
        """
        self.list_widget = list_widget
        self.set_last_clicked()

    def get_folders(self) -> list:
        """
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
