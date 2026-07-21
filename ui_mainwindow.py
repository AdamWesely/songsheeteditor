# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPlainTextEdit, QSizePolicy, QStatusBar, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 795)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setMenuRole(QAction.MenuRole.NoRole)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setMenuRole(QAction.MenuRole.NoRole)
        self.actionNewSong = QAction(MainWindow)
        self.actionNewSong.setObjectName(u"actionNewSong")
        self.actionNewSong.setMenuRole(QAction.MenuRole.NoRole)
        self.actionDeleteSong = QAction(MainWindow)
        self.actionDeleteSong.setObjectName(u"actionDeleteSong")
        self.actionDeleteSong.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 911, 711))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QWidget(self.layoutWidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.verticalLayoutWidget = QWidget(self.leftPanel)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 291, 711))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.searchEdit = QLineEdit(self.verticalLayoutWidget)
        self.searchEdit.setObjectName(u"searchEdit")

        self.verticalLayout.addWidget(self.searchEdit)

        self.songList = QListWidget(self.verticalLayoutWidget)
        self.songList.setObjectName(u"songList")

        self.verticalLayout.addWidget(self.songList)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.rightPanel = QWidget(self.layoutWidget)
        self.rightPanel.setObjectName(u"rightPanel")
        self.formLayoutWidget = QWidget(self.rightPanel)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(0, 0, 681, 711))
        self.verticalLayout_2 = QVBoxLayout(self.formLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.titleEdit = QLineEdit(self.formLayoutWidget)
        self.titleEdit.setObjectName(u"titleEdit")

        self.verticalLayout_2.addWidget(self.titleEdit)

        self.artistEdit = QLineEdit(self.formLayoutWidget)
        self.artistEdit.setObjectName(u"artistEdit")

        self.verticalLayout_2.addWidget(self.artistEdit)

        self.keyCombo = QComboBox(self.formLayoutWidget)
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.addItem("")
        self.keyCombo.setObjectName(u"keyCombo")

        self.verticalLayout_2.addWidget(self.keyCombo)

        self.lyricsEdit = QPlainTextEdit(self.formLayoutWidget)
        self.lyricsEdit.setObjectName(u"lyricsEdit")

        self.verticalLayout_2.addWidget(self.lyricsEdit)

        self.keyCombo.raise_()
        self.artistEdit.raise_()
        self.lyricsEdit.raise_()
        self.titleEdit.raise_()

        self.horizontalLayout.addWidget(self.rightPanel)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 918, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionNewSong)
        self.toolBar.addAction(self.actionDeleteSong)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SongSheet Editor by Adam Vesely v0.1", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Otev\u0159\u00edt", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit", None))
        self.actionNewSong.setText(QCoreApplication.translate("MainWindow", u"Nov\u00e1 skladba", None))
        self.actionDeleteSong.setText(QCoreApplication.translate("MainWindow", u"Smazat", None))
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hledat...", None))
        self.keyCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"C", None))
        self.keyCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"C#", None))
        self.keyCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"D", None))
        self.keyCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Eb", None))
        self.keyCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"E", None))
        self.keyCombo.setItemText(5, QCoreApplication.translate("MainWindow", u"F", None))
        self.keyCombo.setItemText(6, QCoreApplication.translate("MainWindow", u"F#", None))
        self.keyCombo.setItemText(7, QCoreApplication.translate("MainWindow", u"G", None))
        self.keyCombo.setItemText(8, QCoreApplication.translate("MainWindow", u"Ab", None))
        self.keyCombo.setItemText(9, QCoreApplication.translate("MainWindow", u"A", None))
        self.keyCombo.setItemText(10, QCoreApplication.translate("MainWindow", u"Bb", None))
        self.keyCombo.setItemText(11, QCoreApplication.translate("MainWindow", u"B", None))

        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

