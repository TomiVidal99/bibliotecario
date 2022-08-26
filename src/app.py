"""
    Main code that handles the logic side of the app
"""

import os
from .data_types.DestinationFolder import DestinationFolder
from .data_types.OriginFoldersList import OriginFoldersList
from .data_types.DestinationFoldersList import DestinationFoldersList
from .data_types.RecentlyMovedFoldersList import RecentlyMovedFoldersList
from .gui.app_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from .utils.create_intial_settings import (
    OriginFolder,
    handle_first_init,
    reset_settings_to_default,
    get_stored_data,
    set_stored_data,
    get_default_user_settings_path,
)

DEFAULT_USER_LANGUAGE = "en_us"


class MainWindow(QMainWindow):
    """
    Main window of the app
    """

    def __init__(self) -> None:
        super().__init__()
        self.app_name = "bibliotecario"
        self.default_paths = {}
        self.origin_folders = OriginFoldersList([], None)
        self.destination_folders = DestinationFoldersList([], None)
        self.recently_moved_folders = RecentlyMovedFoldersList([], None)
        self.setup_language()
        self.set_default_paths()
        self.set_user_settings()
        self.build_ui()
        self.connect_buttons()

    def init_folders_lists(self) -> None:
        """
        Initializes the list of origin, destination and recently moved folders
        """
        origin_folders_list_widget = self.ui_components.list_origin_folders
        destination_folders_list_widget = self.ui_components.list_destination_folders
        recently_moved_folders_list_widget = self.ui_components.list_recently_moved
        self.origin_folders.set_list_widget(origin_folders_list_widget)
        self.destination_folders.set_list_widget(destination_folders_list_widget)
        self.recently_moved_folders.set_list_widget(recently_moved_folders_list_widget)
        self.load_stored_data()  # this is here instead in the function that handles the first init because it requires UI initilization
        self.origin_folders.set_update_stored_folders_callback(
            self.update_stored_origin_folders
        )

    def update_ui(self) -> None:
        """
        Updates the ui with the current app state.
        """
        # TODO: maybe make a class STATE that handles all state related stuff??
        # TODO: think what happens when the state of some list has not changed but we update the UI: lots of cpu and mem usage = BAD
        print("--LOG--> Updating the UI with the current state.")
        self.origin_folders.update_ui()
        self.destination_folders.update_ui()
        self.recently_moved_folders.update_ui()

    def load_stored_data(self) -> None:
        """
        Gets the data stored in the settings folder and saves it into the current state
        """
        # TODO: load the rest of the data
        # settings_folder = self.default_paths["bibliotecario"]
        # settings_file = self.default_paths["settings"]
        print("--LOG--> State updated.")
        origin_folders_path = self.default_paths["origin_folders"]
        destination_folders_path = self.default_paths["destination_folders"]
        recently_moved_folders_path = self.default_paths["recently_moved_folders"]
        stored_origin_folders = get_stored_data(origin_folders_path)
        stored_destination_folders = get_stored_data(destination_folders_path)
        stored_recently_moved_folders = get_stored_data(recently_moved_folders_path)
        self.origin_folders.set_folders(stored_origin_folders)
        self.destination_folders.set_folders(stored_destination_folders)
        self.recently_moved_folders.set_folders(stored_recently_moved_folders)

    def connect_buttons(self) -> None:
        """
        Hook up the callbacks to the buttons click events
        """
        self.ui_components.btn_reset_settings.clicked.connect(
            self.handle_app_reset_settings
        )
        self.ui_components.btn_add_origin_folder.clicked.connect(self.add_origin_folder)
        self.ui_components.btn_add_destination_folder.clicked.connect(
            self.add_destination_folder
        )
        self.ui_components.btn_remove_origin_folder.clicked.connect(
            self.remove_origin_foler
        )
        self.ui_components.btn_save_settings.clicked.connect(
            self.update_stored_origin_folders
        )

    def build_ui(self) -> None:
        """
        Creates the UI components depending on the language.
        """
        self.ui_components = (
            Ui_MainWindow()
        )  # this imports the GUI created in the qt-designer
        self.ui_components.setupUi(self)  # this initializes the UI components
        self.setWindowTitle(
            self.app_name + " - Settings Panel"
        )  # TODO: change this dependently on the language
        self.init_folders_lists()  # this depends on the UI, thats why it's loaded last.
        self.show()  # shows the window

    def setup_language(self) -> None:
        """
        Sets the app language and load the corresponding text translations
        """
        # TODO
        self.app_language = DEFAULT_USER_LANGUAGE

    def set_default_paths(self) -> None:
        """
        Creates the default user paths depending on the OS and the user
        i.e: 'bibliotecario', 'Downloads', 'Settings'
        """
        # TODO: improve this and add more paths?
        self.default_paths["bibliotecario"] = get_default_user_settings_path()
        self.default_paths["settings"] = os.path.join(
            self.default_paths.get("bibliotecario", ""), "settings"
        )
        self.default_paths["origin_folders"] = os.path.join(
            self.default_paths.get("bibliotecario", ""), "origin_folders.bin"
        )
        self.default_paths["recently_moved_folders"] = os.path.join(
            self.default_paths.get("bibliotecario", ""), "recently_moved_folders.bin"
        )
        self.default_paths["destination_folders"] = os.path.join(
            self.default_paths.get("bibliotecario", ""), "destination_folders.bin"
        )

    def set_user_settings(self) -> None:
        """
        Gets the user settings saved from previous sessions.
        Should handle the creation of the default settings as well.
        """
        # TODO
        settings_folder = self.default_paths["bibliotecario"]
        settings_file = self.default_paths["settings"]
        origin_folders = self.default_paths["origin_folders"]
        handle_first_init(settings_folder, settings_file, origin_folders)

    def handle_reset_settings(self) -> None:
        """
        Removes the settings folder
        """
        settings_folder = self.default_paths["bibliotecario"]
        reset_settings_to_default(settings_folder)

    def handle_app_reset_settings(self) -> None:
        """
        Callback when the user wants to set the app to the default settings
        """
        settings_folder = self.default_paths["bibliotecario"]
        settings_file = self.default_paths["settings"]
        origin_folders = self.default_paths["origin_folders"]
        reset_settings_to_default(settings_folder)  # removes the entire folder
        handle_first_init(
            settings_folder, settings_file, origin_folders
        )  # creates the default values
        self.load_stored_data()  # loads to the state the stored data in the just created files
        self.update_ui()

    def add_origin_folder(self) -> None:
        """
        Creates a new origin folder and pushes it to the list
        """
        print("--LOG--> Adding new origin folder")
        # TODO: make a new popup window that has the inputs
        folder_path = "test/path/a"
        folder_name = "Test path"
        folder = OriginFolder(folder_name, folder_path)
        self.origin_folders.add_folder(folder)
        print("--LOG--> Added '" + folder_name + "', with id = " + folder.get_id())

    def remove_origin_foler(self) -> None:
        """
        Removes an origin folder from the list
        """
        # TODO
        folder_id = self.origin_folders.get_last_clicked()
        if folder_id != "":
            self.origin_folders.remove_folder(folder_id)

    def add_destination_folder(self) -> None:
        """
        Creates a new destination folder and pushes it to the list
        """
        print("--LOG--> Adding new destination folder")
        # TODO: make a new popup window that has the inputs and the filters
        folder_path = "/my/second/test/abcd"
        folder_name = "Some cool destination folder like Documents/pdfs"
        folder = DestinationFolder(folder_name, folder_path, [])
        self.destination_folders.add_folder(folder)
        print("--LOG--> Added '" + folder_name + "', with id = " + str(folder.get_id()))

    def remove_destintion_folder(self) -> None:
        """
        Removes a destination folder from the list
        """
        # TODO

    def update_stored_origin_folders(self) -> None:
        """
        Before we destroy the app save the current state
        """
        # TODO: think, do i wanna save just the list of folders or the entire OriginFolders instance?
        origin_folders_path = self.default_paths["origin_folders"]
        set_stored_data(origin_folders_path, self.origin_folders.folders)
        print("--LOG--> Saved current state'")
