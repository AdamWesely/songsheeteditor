# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowwithtabs.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1047, 1169)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setMenuRole(QAction.MenuRole.NoRole)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1041, 1091))
        self.songEdit = QWidget()
        self.songEdit.setObjectName(u"songEdit")
        self.layoutWidget = QWidget(self.songEdit)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1031, 1061))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftPanel = QWidget(self.layoutWidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.verticalLayoutWidget_5 = QWidget(self.leftPanel)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 0, 261, 1061))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.searchEdit = QLineEdit(self.verticalLayoutWidget_5)
        self.searchEdit.setObjectName(u"searchEdit")

        self.verticalLayout_9.addWidget(self.searchEdit)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.actionNewSong = QPushButton(self.verticalLayoutWidget_5)
        self.actionNewSong.setObjectName(u"actionNewSong")

        self.horizontalLayout_6.addWidget(self.actionNewSong)

        self.actionDeleteSong = QPushButton(self.verticalLayoutWidget_5)
        self.actionDeleteSong.setObjectName(u"actionDeleteSong")

        self.horizontalLayout_6.addWidget(self.actionDeleteSong)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.songList = QListWidget(self.verticalLayoutWidget_5)
        self.songList.setObjectName(u"songList")

        self.verticalLayout_9.addWidget(self.songList)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.rightPanel = QWidget(self.layoutWidget)
        self.rightPanel.setObjectName(u"rightPanel")
        self.formLayoutWidget_5 = QWidget(self.rightPanel)
        self.formLayoutWidget_5.setObjectName(u"formLayoutWidget_5")
        self.formLayoutWidget_5.setGeometry(QRect(0, 0, 771, 1061))
        self.verticalLayout_10 = QVBoxLayout(self.formLayoutWidget_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.titleEdit = QLineEdit(self.formLayoutWidget_5)
        self.titleEdit.setObjectName(u"titleEdit")

        self.verticalLayout_10.addWidget(self.titleEdit)

        self.artistEdit = QLineEdit(self.formLayoutWidget_5)
        self.artistEdit.setObjectName(u"artistEdit")

        self.verticalLayout_10.addWidget(self.artistEdit)

        self.keyCombo = QComboBox(self.formLayoutWidget_5)
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

        self.verticalLayout_10.addWidget(self.keyCombo)

        self.lyricsEdit = QPlainTextEdit(self.formLayoutWidget_5)
        self.lyricsEdit.setObjectName(u"lyricsEdit")

        self.verticalLayout_10.addWidget(self.lyricsEdit)


        self.horizontalLayout.addWidget(self.rightPanel)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.tabWidget.addTab(self.songEdit, "")
        self.playlistEdit = QWidget()
        self.playlistEdit.setObjectName(u"playlistEdit")
        self.tabWidget.addTab(self.playlistEdit, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1047, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SongSheet Editor by Adam Vesely v0.1", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Otev\u0159\u00edt", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Ulo\u017eit jako", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"Ulo\u017eit jako", None))
#endif // QT_CONFIG(tooltip)
        self.searchEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hledat...", None))
        self.actionNewSong.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionDeleteSong.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
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

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.songEdit), QCoreApplication.translate("MainWindow", u"Songs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.playlistEdit), QCoreApplication.translate("MainWindow", u"Playlists", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

