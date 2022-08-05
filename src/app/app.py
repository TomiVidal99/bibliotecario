# Main code that handles the logic side of the app

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from app_ui import Ui_MainWindow


class MainApp(QMainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainApp()
    win.show()
    sys.exit(app.exec_())
