# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\zhaomengyi\myproject\pyqt4dev\trytodo\matplotwithQTDesigner\qtdesigner.ui'
#
# Created: Fri Nov 07 09:48:41 2014
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_MplMainWindow(object):
    def setupUi(self, MplMainWindow):
        MplMainWindow.setObjectName(_fromUtf8("MplMainWindow"))
        MplMainWindow.resize(646, 600)
        self.centralWidget = QtGui.QWidget(MplMainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 581, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.mpllineEdit = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.mpllineEdit.setObjectName(_fromUtf8("mpllineEdit"))
        self.horizontalLayout.addWidget(self.mpllineEdit)
        self.mplpushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.mplpushButton.setObjectName(_fromUtf8("mplpushButton"))
        self.horizontalLayout.addWidget(self.mplpushButton)
        self.mpl = MplWidget(self.centralWidget)
        self.mpl.setGeometry(QtCore.QRect(20, 90, 571, 441))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mpl.sizePolicy().hasHeightForWidth())
        self.mpl.setSizePolicy(sizePolicy)
        self.mpl.setObjectName(_fromUtf8("mpl"))
        MplMainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MplMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 646, 23))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.mplmenuFile = QtGui.QMenu(self.menuBar)
        self.mplmenuFile.setObjectName(_fromUtf8("mplmenuFile"))
        MplMainWindow.setMenuBar(self.menuBar)
        self.mplactionOpen = QtGui.QAction(MplMainWindow)
        self.mplactionOpen.setObjectName(_fromUtf8("mplactionOpen"))
        self.mplactionQuit = QtGui.QAction(MplMainWindow)
        self.mplactionQuit.setObjectName(_fromUtf8("mplactionQuit"))
        self.mplmenuFile.addAction(self.mplactionOpen)
        self.mplmenuFile.addSeparator()
        self.mplmenuFile.addAction(self.mplactionQuit)
        self.menuBar.addAction(self.mplmenuFile.menuAction())

        self.retranslateUi(MplMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MplMainWindow)

    def retranslateUi(self, MplMainWindow):
        MplMainWindow.setWindowTitle(_translate("MplMainWindow", "MainWindow", None))
        self.mplpushButton.setText(_translate("MplMainWindow", "PushButton", None))
        self.mplmenuFile.setTitle(_translate("MplMainWindow", "File", None))
        self.mplactionOpen.setText(_translate("MplMainWindow", "Open", None))
        self.mplactionQuit.setText(_translate("MplMainWindow", "Quit", None))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MplMainWindow = QtGui.QMainWindow()
    ui = Ui_MplMainWindow()
    ui.setupUi(MplMainWindow)
    MplMainWindow.show()
    sys.exit(app.exec_())

