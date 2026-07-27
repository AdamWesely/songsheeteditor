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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QToolBar,
    QVBoxLayout, QWidget)

from widgets.setlist_widget import SetlistWidget

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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.songEdit = QWidget()
        self.songEdit.setObjectName(u"songEdit")
        sizePolicy.setHeightForWidth(self.songEdit.sizePolicy().hasHeightForWidth())
        self.songEdit.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.songEdit)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.leftPanel = QWidget(self.songEdit)
        self.leftPanel.setObjectName(u"leftPanel")
        sizePolicy.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.leftPanel)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.searchEdit = QLineEdit(self.leftPanel)
        self.searchEdit.setObjectName(u"searchEdit")

        self.verticalLayout_9.addWidget(self.searchEdit)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.actionNewSong = QPushButton(self.leftPanel)
        self.actionNewSong.setObjectName(u"actionNewSong")

        self.horizontalLayout_6.addWidget(self.actionNewSong)

        self.actionDeleteSong = QPushButton(self.leftPanel)
        self.actionDeleteSong.setObjectName(u"actionDeleteSong")

        self.horizontalLayout_6.addWidget(self.actionDeleteSong)


        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.songList = QListWidget(self.leftPanel)
        self.songList.setObjectName(u"songList")

        self.verticalLayout_9.addWidget(self.songList)


        self.horizontalLayout_5.addLayout(self.verticalLayout_9)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.rightPanel = QWidget(self.songEdit)
        self.rightPanel.setObjectName(u"rightPanel")
        sizePolicy.setHeightForWidth(self.rightPanel.sizePolicy().hasHeightForWidth())
        self.rightPanel.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.rightPanel)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.titleEdit = QLineEdit(self.rightPanel)
        self.titleEdit.setObjectName(u"titleEdit")

        self.verticalLayout_10.addWidget(self.titleEdit)

        self.artistEdit = QLineEdit(self.rightPanel)
        self.artistEdit.setObjectName(u"artistEdit")

        self.verticalLayout_10.addWidget(self.artistEdit)

        self.keyCombo = QComboBox(self.rightPanel)
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

        self.lyricsEdit = QPlainTextEdit(self.rightPanel)
        self.lyricsEdit.setObjectName(u"lyricsEdit")

        self.verticalLayout_10.addWidget(self.lyricsEdit)


        self.verticalLayout_5.addLayout(self.verticalLayout_10)


        self.horizontalLayout.addWidget(self.rightPanel)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.songEdit, "")
        self.playlistEdit = QWidget()
        self.playlistEdit.setObjectName(u"playlistEdit")
        sizePolicy.setHeightForWidth(self.playlistEdit.sizePolicy().hasHeightForWidth())
        self.playlistEdit.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.playlistEdit)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.leftPanel_2 = QVBoxLayout()
        self.leftPanel_2.setObjectName(u"leftPanel_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.actionNewSetlist = QPushButton(self.playlistEdit)
        self.actionNewSetlist.setObjectName(u"actionNewSetlist")

        self.horizontalLayout_3.addWidget(self.actionNewSetlist)

        self.actionDeleteSetlist = QPushButton(self.playlistEdit)
        self.actionDeleteSetlist.setObjectName(u"actionDeleteSetlist")

        self.horizontalLayout_3.addWidget(self.actionDeleteSetlist)

        self.actionRenameSetlist = QPushButton(self.playlistEdit)
        self.actionRenameSetlist.setObjectName(u"actionRenameSetlist")

        self.horizontalLayout_3.addWidget(self.actionRenameSetlist)


        self.leftPanel_2.addLayout(self.horizontalLayout_3)

        self.setlistList = QListWidget(self.playlistEdit)
        self.setlistList.setObjectName(u"setlistList")

        self.leftPanel_2.addWidget(self.setlistList)


        self.horizontalLayout_2.addLayout(self.leftPanel_2)

        self.rightPanel_2 = QVBoxLayout()
        self.rightPanel_2.setObjectName(u"rightPanel_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.songLibrarySearch = QLineEdit(self.playlistEdit)
        self.songLibrarySearch.setObjectName(u"songLibrarySearch")

        self.verticalLayout_2.addWidget(self.songLibrarySearch)

        self.songLibraryList = QListWidget(self.playlistEdit)
        self.songLibraryList.setObjectName(u"songLibraryList")
        self.songLibraryList.setDragEnabled(True)
        self.songLibraryList.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)

        self.verticalLayout_2.addWidget(self.songLibraryList)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.setlistSongs = SetlistWidget(self.playlistEdit)
        self.setlistSongs.setObjectName(u"setlistSongs")
        self.setlistSongs.setAcceptDrops(True)
        self.setlistSongs.setDragEnabled(True)
        self.setlistSongs.setDragDropMode(QAbstractItemView.DragDropMode.DragDrop)
        self.setlistSongs.setDefaultDropAction(Qt.DropAction.MoveAction)

        self.verticalLayout.addWidget(self.setlistSongs)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.rightPanel_2.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_2.addLayout(self.rightPanel_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.playlistEdit, "")

        self.horizontalLayout_7.addWidget(self.tabWidget)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SongSheet Editor by Adam Vesely v0.2", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.actionOpen.setToolTip(QCoreApplication.translate("MainWindow", u"Open", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"Save as...", None))
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
        self.actionNewSetlist.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionDeleteSetlist.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionRenameSetlist.setText(QCoreApplication.translate("MainWindow", u"Rename", None))
        self.songLibrarySearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search songs...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.playlistEdit), QCoreApplication.translate("MainWindow", u"Playlists", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

