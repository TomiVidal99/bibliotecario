# TODO: create a class and add methods to return the parsed information to a Folder class?
from PyQt5 import QtWidgets

def get_open_files_and_dirs(parent=None, caption='', directory='',
                            options=None, filter='', initialFilter='') -> list:
    def updateText():
        # update the contents of the line edit widget with the selected files
        selected = []
        for index in view.selectionModel().selectedRows():
            selected.append('"{}"'.format(index.data()))
        lineEdit.setText(' '.join(selected))

    dialog = QtWidgets.QFileDialog(parent, windowTitle=caption)
    dialog.setFileMode(dialog.ExistingFiles)
    if options:
        dialog.setOptions(options)
    dialog.setOption(dialog.DontUseNativeDialog, True)
    if directory:
        dialog.setDirectory(directory)
    if filter:
        dialog.setNameFilter(filter)
        if initialFilter:
            dialog.selectNameFilter(initialFilter)

    # by default, if a directory is opened in file listing mode, 
    # QFileDialog.accept() shows the contents of that directory, but we 
    # need to be able to "open" directories as we can do with files, so we 
    # just override accept() with the default QDialog implementation which 
    # will just return exec_()
    dialog.accept = lambda: QtWidgets.QDialog.accept(dialog)

    # there are many item views in a non-native dialog, but the ones displaying 
    # the actual contents are created inside a QStackedWidget; they are a 
    # QTreeView and a QListView, and the tree is only used when the 
    # viewMode is set to QFileDialog.Details, which is not this case
    stackedWidget = dialog.findChild(QtWidgets.QStackedWidget)
    view = stackedWidget.findChild(QtWidgets.QListView)
    view.selectionModel().selectionChanged.connect(updateText)

    lineEdit = dialog.findChild(QtWidgets.QLineEdit)
    # clear the line edit contents whenever the current directory changes
    dialog.directoryEntered.connect(lambda: lineEdit.setText(''))

    dialog.exec_()

    print("From func: \n")
    print(dialog.selectedFiles())

    return dialog.selectedFiles()
