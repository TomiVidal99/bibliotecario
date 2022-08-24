"""
    Handle the creation of the default origin and destination folders, with most common filters.
    All of this depends on the current OS (Windows, Linux, MacOS)
"""

import platform
import os
import json
from pathlib import Path


def get_current_os():
    """
    Returns 'Windows', 'Linux', 'MacOS'.
    """
    return platform.system()


def get_default_origin_folders(default_origin_folders_file):
    """
    Creates the default origin folders depending on the current OS.
    """
    current_os = get_current_os()
    # create the path to documents and download depending on the user and the OS
    # TODO: check case for MacOS? or just ignore that system.
    if current_os == "Windows":
        user_path = os.path.expanduser("~")
        downloads_folder = os.path.join(user_path, "downloads")
        desktop_folder = os.path.join(user_path, "desktop")
    else:
        user_path = Path.home()
        downloads_folder = str(os.path.join(user_path, "Downloads"))
        desktop_folder = str(os.path.join(user_path, "Desktop"))
    # push the folders to the settings
    return [downloads_folder, desktop_folder]
