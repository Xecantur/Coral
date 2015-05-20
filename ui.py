# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coral2.0.ui'
#
# Created: Sun May 17 18:52:31 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.resize(567, 388)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/document-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(mainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 0))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.newButton = QtGui.QCommandLinkButton(self.widget)
        self.newButton.setMaximumSize(QtCore.QSize(100, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newButton.setIcon(icon1)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.horizontalLayout.addWidget(self.newButton)
        self.openButton = QtGui.QCommandLinkButton(self.widget)
        self.openButton.setMaximumSize(QtCore.QSize(100, 16777215))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openButton.setIcon(icon2)
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.horizontalLayout.addWidget(self.openButton)
        self.saveButton = QtGui.QCommandLinkButton(self.widget)
        self.saveButton.setMaximumSize(QtCore.QSize(100, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/document-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon3)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout.addWidget(self.widget)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(mainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtGui.QToolBar(mainWindow)
        self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        mainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionNew = QtGui.QAction(mainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(mainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(mainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionAbout = QtGui.QAction(mainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionQuit = QtGui.QAction(mainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "Coral", None))
        self.newButton.setText(_translate("mainWindow", "New", None))
        self.newButton.setShortcut(_translate("mainWindow", "Ctrl+N", None))
        self.openButton.setText(_translate("mainWindow", "Open", None))
        self.openButton.setShortcut(_translate("mainWindow", "Ctrl+O", None))
        self.saveButton.setText(_translate("mainWindow", "Save", None))
        self.saveButton.setShortcut(_translate("mainWindow", "Ctrl+S", None))
        self.menuFile.setTitle(_translate("mainWindow", "File", None))
        self.menuAbout.setTitle(_translate("mainWindow", "About", None))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar", None))
        self.toolBar_2.setWindowTitle(_translate("mainWindow", "toolBar_2", None))
        self.actionNew.setText(_translate("mainWindow", "New", None))
        self.actionNew.setToolTip(_translate("mainWindow", "New", None))
        self.actionNew.setShortcut(_translate("mainWindow", "Ctrl+N", None))
        self.actionOpen.setText(_translate("mainWindow", "Open", None))
        self.actionOpen.setShortcut(_translate("mainWindow", "Ctrl+O", None))
        self.actionSave.setText(_translate("mainWindow", "Save", None))
        self.actionSave.setShortcut(_translate("mainWindow", "Ctrl+S", None))
        self.actionAbout.setText(_translate("mainWindow", "About", None))
        self.actionQuit.setText(_translate("mainWindow", "Quit", None))
        self.actionQuit.setShortcut(_translate("mainWindow", "Ctrl+Q", None))

import coral_rc
