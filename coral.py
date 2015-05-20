#!/usr/bin/python
import sys
import os
from PyQt4 import QtCore as qtcore
from PyQt4 import QtGui as qtgui
from ui import Ui_mainWindow

class StartQt4(qtgui.QMainWindow):
    def __init__(self,parent=None):
        qtgui.QWidget.__init__(self,parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Coral - Unsaved Document")
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionNew.triggered.connect(self.new_file)
        self.ui.actionQuit.triggered.connect(self.quit)
        self.ui.actionAbout.triggered.connect(self.about_dialog)
        self.ui.newButton.clicked.connect(self.new_file)
        self.ui.openButton.clicked.connect(self.open_file)
        self.ui.saveButton.clicked.connect(self.save_file)

    def about_dialog(self):
        dialog = qtgui.QDialog()
        dialog.show()

    def quit(self):
        self.close()

    def new_file(self):
        self.setWindowTitle("Coral - Unsaved Document")
        self.ui.textEdit.setText("")

    def open_file(self):
        tedit = self.ui.textEdit
        self.filename = qtgui.QFileDialog.getOpenFileName(self,"Open File")
        from os.path import isfile
        if isfile(self.filename):
            txt = open(self.filename,'r').read()
            tedit.setText(txt)
            self.setWindowTitle("Coral - " + self.filename)


    def save_file(self):
        txtbuffer = self.ui.textEdit.toPlainText()
        self.filename = qtgui.QFileDialog.getSaveFileName(self,"Save File")
        if self.filename != '':
            f = open(self.filename,'w')
            f.write(txtbuffer)
            f.close()
            self.setWindowTitle("Coral - " + self.filename)


if __name__ == "__main__":
    app = qtgui.QApplication(sys.argv)
    myapp = StartQt4()
    myapp.show()
    sys.exit(app.exec_())
