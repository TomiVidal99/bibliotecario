"""
    Main code that handles the logic side of the app
"""

import os
import json
from PyQt5.QtWidgets import QListWidgetItem, QMainWindow
from src.gui.app_ui import Ui_MainWindow
from src.utils.create_intial_settings import (
    create_settings_folder,
    create_intial_settings,
    create_intial_origin_folders,
    reset_settings_to_default,
)

# TODO: change this, make them dynamic and must detect OS
LINUX_SETTINGS_FOLDER = "/home/tomii/.config/bibliotecario"
LINUX_SETTINGS = "/home/tomii/.config/bibliotecario/settings.json"
LINUX_RECENTLY_MOVED = "/home/tomii/.config/bibliotecario/recently_moved.json"


class MainWindow(QMainWindow):
    """
    Main app, all code should run from this entry point
    """

    def __init__(self):
        super().__init__()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.recently_moved = []
        self.origin_folders = []
        self.destination_folders = []
        self.setup_btn_handlers()  # add callbacks to buttons
        self.restore_previous_settings()

    def setup_btn_handlers(self):
        """
        Hooks up the callbacks to the buttons in the UI
        """
        self.main_ui.btn_open_recently_moved.clicked.connect(
            self.handle_open_recently_moved
        )
        self.main_ui.btn_add_origin_folder.clicked.connect(
            self.handle_add_origin_folder
        )
        self.main_ui.btn_reset_settings.clicked.connect(self.handle_reset_settings)

    def handle_reset_settings(self):
        """
        Callback to reset the user settings
        """
        # TODO: should pop up a menu to confirm the action
        reset_settings_to_default(LINUX_SETTINGS_FOLDER)

    def check_first_init(self):
        """
        Check if this is the first time that the user inits the app.
        If this is the case should create the settings files.
        """
        # TODO: i should make a default files for destination and origin folders. (maybe have documents, desktop, music, videos, etc. some of the most common)
        has_already_init = os.path.isfile(LINUX_SETTINGS)
        if not has_already_init:
            create_settings_folder(LINUX_SETTINGS_FOLDER)
            create_intial_settings(LINUX_SETTINGS)
            create_intial_origin_folders(LINUX_RECENTLY_MOVED)

    def restore_previous_settings(self):
        """
        Load to memory cached data in temp files from the user.
        Also if such temp files doesn't exist should create the first configuration.
        """
        self.check_first_init()
        # TODO: should detect the OS and change the cache, log and settings folders for each system. think how to handle this?
        # TODO: i should have in count the edge case when the folder .config doesn't exist

        # load the data from the settings files
        with open(LINUX_RECENTLY_MOVED, "r", -1, "utf-8") as f_p:
            self.origin_folders = json.load(f_p)

        # fill the list of origin folers with the stored data
        origin_folders = self.origin_folders
        list_widget = self.main_ui.list_origin_folders
        for item in origin_folders:
            item_widget = QListWidgetItem(item)
            list_widget.addItem(item_widget)

    def handle_open_recently_moved(self):
        """
        Callback handler for when the user wants to see a moved file
        """
        print("TODO: open folder that contains the most recent moved file")
        if len(self.recently_moved) > 0:
            print(self.recently_moved[0])
        # with subprocess.Popen(r'explorer /select,' + folder_path) as open_folder_process:
        #    open_folder_process.wait()

    def handle_add_origin_folder(self):
        """
        Callback when the user wants to add a origin folder
        """
        print("TODO: add origin folder")
