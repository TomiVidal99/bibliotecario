"""
    Handle the creation of the initial configuration
"""

import json
import os

def create_settings_folder(settings_folder):
    """
    Create the folder that contains all the settings files
    """
    os.mkdir(settings_folder)

def create_intial_settings(settings_path):
    """
    Creates the intial settings
    """
    INITIAL_SETTINGS = ["TEST"]  # TODO: finish this and move it to another file?
    with open(settings_path, "+w", -1, "utf-8") as f_p:
        json.dump(INITIAL_SETTINGS, f_p)
        print("--LOG--> Done saving intial settings to: '" + settings_path + "'")


def create_intial_origin_folders(origin_path):
    """
    Creates the initial origin folders
    """
    INITIAL_ORIGIN_FOLDERS= ["$HOME/Downloads", "$HOME/Desktop"] # TODO: should make this better and move it to another file
    with open(origin_path, "+w", -1, "utf-8") as f_p:
        json.dump(INITIAL_ORIGIN_FOLDERS, f_p)
        print("--LOG--> Done saving intial origin folders to: '" + origin_path + "'")
