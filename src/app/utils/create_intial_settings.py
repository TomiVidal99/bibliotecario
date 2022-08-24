"""
    Handle the the initial configuration
"""

import json
import os
import shutil
from .intial_values import get_default_origin_folders


def create_settings_folder(settings_folder):
    """
    Create the folder that contains all the settings files
    """
    exists_settings_folder = os.path.exists(settings_folder)
    if not exists_settings_folder:
        os.mkdir(settings_folder)


def create_intial_settings(settings_path):
    """
    Creates the intial settings
    """
    DEFAULT_SETTINGS_FILE_RELATIVE_PATH = "./../../assets/defaultUserSettings.json"
    DEFAULT_SETTINGS_FILE = os.path.join(
        os.path.dirname(__file__), DEFAULT_SETTINGS_FILE_RELATIVE_PATH
    )
    with open(DEFAULT_SETTINGS_FILE, "r", -1, "utf-8") as default_settings_file:
        default_settings = json.load(default_settings_file)
        with open(settings_path, "+w", -1, "utf-8") as user_settings_file:
            json.dump(default_settings, user_settings_file)
            print("--LOG--> Created new user settings")


def create_intial_origin_folders(origin_path):
    """
    Creates the initial origin folders
    """
    default_origin_folders = get_default_origin_folders(origin_path)
    # TODO: should make this better and move it to another file
    with open(origin_path, "+w", -1, "utf-8") as f_p:
        json.dump(default_origin_folders, f_p)
        print("--LOG--> Done saving intial origin folders to: '" + origin_path + "'")


def reset_settings_to_default(settings_folder):
    """
    Removes user settings and sets everything to the default values.
    """
    # TODO: think how to handle the current states so we don't have to reset the app to apply changes.
    shutil.rmtree(settings_folder)
    print("--LOG--> Erased user data.")
