"""
    Handle the the initial configuration
"""

import json
import os
import pickle
import shutil
from .intial_values import get_default_origin_folders
from src.data_types.OriginFolder import OriginFolder


def handle_first_init(settings_folder, settings_file, origin_folders) -> None:
    """
    If the user has no settings folder this handles the creation of it and it corresponding
    default settings
    """
    exists_settings_folder = os.path.exists(settings_folder)
    if not exists_settings_folder:
        os.mkdir(settings_folder)
        create_intial_settings(settings_file)
        create_intial_origin_folders(origin_folders)


def create_intial_settings(settings_file) -> None:
    """
    Creates the intial settings
    """
    print("--LOG--> TODO.")
    # TODO: think if we really want for it to be JSON, it's cool but necessary?
    # default_settings_file_relative_path = "./../assets/defaultUserSettings.json"
    # default_settings_file = os.path.join(
    #     os.path.dirname(__file__), default_settings_file_relative_path
    # )
    # with open(default_settings_file, "r", -1, "utf-8") as default_settings_file:
    #     default_settings = json.load(default_settings_file)
    #     with open(settings_file, "+w", -1, "utf-8") as user_settings_file:
    #         json.dump(default_settings, user_settings_file)
    #         print("--LOG--> Created new user settings")


def create_intial_origin_folders(origin_path) -> None:
    """
    Creates the initial origin folders
    """
    default_origin_folders = get_default_origin_folders()
    set_stored_data(origin_path, default_origin_folders)


def reset_settings_to_default(settings_folder) -> int:
    """
    Removes user settings and sets everything to the default values.
     -> returns 1 if the settings folder has been removed successfully else returns 0
    """
    # TODO: think how to handle the current states so we don't have to reset the app to apply changes.
    does_it_have_settings = os.path.exists(settings_folder)
    if does_it_have_settings:
        shutil.rmtree(settings_folder)
        print("--LOG--> Erased user data.")
        return 1

    print("--LOG--> Already erased data.")
    return 0


def set_stored_data(data_filepath, payload) -> None:
    """
    Saves in the disk settingsd data
    """
    # TODO: maybe add error handling?? return a tuple with an error state???
    with open(data_filepath, "wb") as _fp:
        pickle.dump(payload, _fp)
        print("--LOG--> Done storing data in '" + data_filepath + "'.")


def get_stored_data(data_filepath) -> list:
    """
    Returns the data stored in some user's settings file
    """
    # TODO: maybe add error handling?? return a tuple with an error state???
    # load the data from the settings files
    with open(data_filepath, "rb") as _fp:
        data = pickle.load(_fp)
        print("--LOG--> Done loading data from '" + data_filepath + "'.")

    return data
