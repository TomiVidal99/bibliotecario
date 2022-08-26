"""
    Main code that handles the logic side of the app
"""

import os
from .data_types.OriginFoldersList import OriginFoldersList
from .gui.app_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from .utils.create_intial_settings import (
    handle_first_init,
    reset_settings_to_default,
    get_stored_data
)

DEFAULT_USER_LANGUAGE = "en_us"
DEFAULT_SETTINGS_PATH = "/home/tomii/.config/bibliotecario"

class MainWindow(QMainWindow):
    """
    Main window of the app
    """

    def __init__(self) -> None:
        super().__init__()
        self.app_name = "bibliotecario"
        self.default_paths = {"bibliotecario": DEFAULT_SETTINGS_PATH}
        self.origin_folders = OriginFoldersList(None, None)
        self.destination_folders = [] # TODO
        self.recently_moved_folders = [] # TODO
        self.setup_language()
        self.set_default_paths()
        self.set_user_settings()
        self.build_ui()
        self.connect_buttons()
    
    def init_folders_lists(self) -> None:
        """
        Initializes the list of origin, destination and recently moved folders
        """
        # TODO: add the other folders
        origin_folders_list_widget = self.ui_components.list_origin_folders
        self.origin_folders.set_list_widget(origin_folders_list_widget)

    def update_ui(self) -> None:
        """
        Updates the ui with the current app state.
        """
        # TODO: maybe make a class STATE that handles all state related stuff??
        print("--LOG--> Updating the UI with the current state.")
        self.origin_folders.update_ui()

    def load_stored_data(self) -> None:
        """
        Gets the data stored in the settings folder and saves it into the current state
        """
        # TODO: load the rest of the data
        #settings_folder = self.default_paths["bibliotecario"]
        #settings_file = self.default_paths["settings"]
        print("--LOG--> State updated.")
        origin_folders_path = self.default_paths["origin_folders"]
        stored_origin_folders = get_stored_data(origin_folders_path)
        self.origin_folders.set_folders(stored_origin_folders)

    def connect_buttons(self) -> None:
        """
        Hook up the callbacks to the buttons click events
        """
        self.ui_components.btn_reset_settings.clicked.connect(self.handle_app_reset_settings)

    def build_ui(self) -> None:
        """
        Creates the UI components depending on the language.
        """
        # TODO
        self.ui_components = Ui_MainWindow() # this imports the GUI created in the qt-designer
        self.ui_components.setupUi(self) # this initializes the UI components
        self.setWindowTitle(self.app_name + " - Settings Panel") # TODO: change this dependently of the language
        self.init_folders_lists() # this depends on the UI, thats why it's loaded last.
        self.show() # shows the window

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
        self.default_paths["settings"] = os.path.join(
            self.default_paths.get("bibliotecario", ""), "settings"
        )
        self.default_paths["origin_folders"] = os.path.join(
            self.default_paths.get("bibliotecario", ""), "origin_folders"
        )
        self.default_paths["recently_moved_folders"] = os.path.join(
            self.default_paths.get("bibliotecario", ""), "recently_moved_folders"
        )
        self.default_paths["destination_folders"] = os.path.join(
            self.default_paths.get("bibliotecario", ""), "destination_folders"
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
        reset_settings_to_default(settings_folder) # removes the entire folder
        handle_first_init(settings_folder, settings_file, origin_folders) # creates the default values
        self.load_stored_data() # loads to the state the stored data in the just created files
        self.update_ui()
