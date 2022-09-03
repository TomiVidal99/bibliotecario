"""
Creates a popup window that lets you pick a folder
"""

class PickUpFolder():
    """
    Pops up a window that lets you select a folder
    """
    def __init__(self, ui_parent) -> None:
        self.ui_parent = ui_parent
        self.selected_folder = ""

    def update_folder_text(self) -> None:
        """
        Sets the display text of the UI component with the current selected folder
        """
        # TODO

    def pick_foler(self) -> None:
        """
        Lets the user pick a folder from their system
        """
