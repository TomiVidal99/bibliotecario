'''
    Main script that runs the hole app.
'''

import sys
from PyQt5.QtWidgets import QApplication
from src.app import MainWindow

# Good practice when a file is executable is to describe it as follows
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
