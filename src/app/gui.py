from PyQt5.QtWidgets import QApplication, QDialog

class gui(MainWindowUI, MainWindowBase):
    def __init__(self, mainWindow):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        wid = myWidget()

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(wid, 0, 0)
        self.frame.setLayout(self.grid)
