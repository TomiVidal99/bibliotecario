from PyQt5.QtWidgets import QWidget


class SettingsWindow(QWidget):
    """
    Window that contains a folder selection and filters for
    the user to add a new DestinationFolder
    """

    def __init__(self):
        super().__init__()
        self.title = 'Add a destination folder'
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.show()
